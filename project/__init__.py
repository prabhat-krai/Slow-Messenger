from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
key = os.urandom(33)
app.secret_key = key

#app.config.from_object(config.Dev)
from project.users.views import users_blueprint
from project.home.views import home_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)

from models import User

login_manager.login_view = "users.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()