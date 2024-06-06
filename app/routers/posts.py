from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import crud, schemas, auth, dependencies, database
from ..utils import cache

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)

@router.post("/add", response_model=schemas.Post)
def add_post(post: schemas.PostCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(dependencies.get_current_active_user)):
    return crud.create_post(db=db, post=post, user_id=current_user.id)

@router.get("/", response_model=list[schemas.Post])
def get_posts(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(dependencies.get_current_active_user)):
    user_posts = cache.get_cache(current_user.id)
    if user_posts:
        return user_posts
    user_posts = crud.get_posts(db=db, user_id=current_user.id)
    cache.set_cache(current_user.id, user_posts)
    return user_posts

@router.delete("/{post_id}", response_model=schemas.Post)
def delete_post(post_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(dependencies.get_current_active_user)):
    db_post = crud.get_post(db=db, post_id=post_id)
    if db_post is None or db_post.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Post not found")
    crud.delete_post(db=db, post_id=post_id)
    return db_post
