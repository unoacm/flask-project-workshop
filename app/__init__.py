from flask import Flask

# this is how our app starts
app = Flask(__name__)


# we import our api routes to avoid circular imports
from app import routes