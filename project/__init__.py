from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://azlzirukfpmlyz:c8db339a4c85fd31cb055ff1bc7b32704838a224992e100f9c11d4bf8594ecd1@ec2-50-17-233-158.compute-1.amazonaws.com:5432/d70jjn3c34fr41'
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