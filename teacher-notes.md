# Teacher Notes

This doc contains instructions for creating a starter flask app.

## Prerequisites:

- Python 3.6 or later installed
- Pip installed

## Part 1: Initial Project Setup - Hello World!

1. First, we want to make our project directory and create a virtual env, i.e.`python3 -m venv venv`. We can use this virtual environment to install packages into.
2. Active your virtual env (platform dependent).
3. Install flask with `pip install flask`. From now on, this is how we will add packages/dependencies to our project: `pip install [package-name]`.
4. Make `app/__init__.py` and first route in `index.py`.
5. `export FLASK_APP=tutorial.py` & `flask run`

## Part 2: User Logins

1. Make `models.py` with user models and `flask-sqlalchemy` and `flask-migrate`
2. `flask db init`, `flask db migrate`, `flask db upgrade`
3. `flask-wtf`
4. Signup route and form: have it redirect to home only for now
5. change successful signup to create and insert a user
