from project import db
from models import Blogpost

db.create_all()

db.session.add(Blogpost("postgresql","Elephant!", None))


db.session.commit()