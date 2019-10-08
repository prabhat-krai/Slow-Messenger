from flask import render_template, redirect, url_for, flash, session, Blueprint
from functools import wraps
from project import db
from models import Blogpost
from flask_login import login_required

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)




@home_blueprint.route('/')
@login_required
def home():
    posts = db.session.query(Blogpost).all()
    return render_template('index.html', posts = posts)

@home_blueprint.route('/welcome')
def welcome():
    return render_template("welcome.html")