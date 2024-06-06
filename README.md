# FastAPI Web Application with SQLAlchemy and Pydantic

This is a web application built using FastAPI, SQLAlchemy, and Pydantic. It follows the MVC design pattern and includes features such as token-based authentication, request validation, and caching.

## Features

- Sign up: Allows users to sign up with their email and password.
- Login: Allows users to log in with their email and password and obtain a token for authentication.
- AddPost: Allows authenticated users to add posts with text content. Validates payload size and authenticates with a token.
- GetPosts: Retrieves all posts for the authenticated user, implementing response caching for up to 5 minutes.
- DeletePost: Allows authenticated users to delete their posts.

## Installation

1. Clone the repository:

   git clone https://github.com/0saurabh0/fast_api_mvp.git

2. It would be better if you work with virtual environment. refer [HERE](https://docs.python.org/3/library/venv.html) for more details.

3. `cd fast_api_mvp` then `pip install -r requirements.txt`

4. Set up the MySQL database and update the database URL in database.py.

5. Run the application:
  `uvicorn main:app --reload` Your development server is running at `http://localhost:8000/`


## Documentation
   Since, FastAPI provides automatic API documentation. Open http://localhost:8000/docs to view and test the endpoints interactively.


