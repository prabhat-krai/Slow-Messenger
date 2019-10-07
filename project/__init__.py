from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
import os
key = os.urandom(33)
app.secret_key = key

#app.config.from_object(config.Dev)
from project.users.views import users_blueprint
from project.home.views import home_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)
