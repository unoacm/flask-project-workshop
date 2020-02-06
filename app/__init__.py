from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# this is how our app starts
app = Flask(__name__)

# this is how our config and database works
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.create_all()

#login
login = LoginManager(app)

# we import our other stuff to avoid circular imports
from app import routes, models