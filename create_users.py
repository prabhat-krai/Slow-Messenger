from project import db
from models import User
from bcrypt import hashpw
db.create_all()

db.session.add(User("master", "mast@min.com", "password"))
db.session.add(User("Pawan", "air@min.com", "water"))
db.session.add(User("Phoenix", "fire@min.com", "ice"))

db.session.commit()