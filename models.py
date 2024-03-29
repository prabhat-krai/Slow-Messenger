from project import db
from project import bcrypt
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Blogpost(db.Model):

    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, primary_key = False)
    description = db.Column(db.String, primary_key = False)
    author_id = db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, title, description, author_id):
        self.title = title
        self.description = description
        self.author_id = author_id

    def __repr__(self):
        return '<{}>, <{}>'.format(self.title, self.description)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    posts = relationship("Blogpost", backref="author")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        password = bcrypt.generate_password_hash(password.encode('utf8'))
        self.password = password.decode('utf8') 

    def __repr__(self):
        return '<name {}'.format(self.name)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)