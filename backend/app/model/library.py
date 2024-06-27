from utils import db
from model.user import User

class Library(db.Document):
    user = db.ReferenceField(User)
    type = db.StringField(required=True)#book or journal
    description = db.StringField(required=False)
    
class Book(db.Document):
    title = db.StringField(required=True)
    author =  db.StringField(required=True)
    publisher =  db.StringField(required=True)
    publication_year =  db.IntField(required=True)
    genre =  db.StringField(required=False)
    description = db.StringField(required=False)

class Journal(db.Document):
    title = db.StringField(required=True)
    author =  db.StringField(required=True)
    publication_year =  db.IntField(required=True)
    description = db.StringField(required=False)
