from fastapi import FastAPI
from app.routers import auth, posts

app = FastAPI()

app.include_router(auth.router)
app.include_router(posts.router)
