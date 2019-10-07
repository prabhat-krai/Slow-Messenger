from flask import render_template, redirect, url_for, flash, session, Blueprint
from functools import wraps
from project import db
from project.models import Blogpost

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap

@home_blueprint.route('/')
@login_required
def home():
    posts = db.session.query(Blogpost).all()
    return render_template('index.html', posts = posts)
    #return "Searching for restaurants?"

@home_blueprint.route('/welcome')
def welcome():
    return render_template("welcome.html")