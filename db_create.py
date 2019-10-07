from app import db
from models import Blogpost

db.create_all()

db.session.add(Blogpost("Good","This is a fine day"))
db.session.add(Blogpost("Woah","This is a different day"))
db.session.add(Blogpost("Post","This is a testing ground"))
db.session.add(Blogpost("Test","YooHoo!"))
db.session.add(Blogpost("postgresql","Elephant!"))


db.session.commit()