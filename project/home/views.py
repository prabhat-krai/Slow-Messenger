from flask import render_template, redirect, url_for, flash, session, Blueprint, request
from project import db
from models import Blogpost
from flask_login import login_required, current_user
from .forms import MessageForm

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)




@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    error = None
    form = MessageForm(request.form)
    if form.validate_on_submit():
        new_message = Blogpost(
            form.title.data,
            form.description.data,
            current_user.id
        )
        db.session.add(new_message)
        db.session.commit()
        flash('New entry was successfully posted. Thanks.')
        return redirect(url_for('home.home'))
    else:
        posts = db.session.query(Blogpost).all()
        return render_template(
            'index.html', posts=posts, form=form, error=error)



@home_blueprint.route('/welcome')
def welcome():
    return render_template("welcome.html")