from utils import db
from model.user import User

class Course(db.Document):
    user = db.ReferenceField(User)
    kode_mk = db.StringField(required=True, unique=True)
    semester = db.StringField(required=True)
    nama_mk = db.StringField(required=False)
    sks = db.IntField(required=False)
    nama_prof = db.IntField(required=False)
    description = db.StringField(required=False)
    
class create_announcement(db.Document):
    courses_announcement = db.StringField(required=True)
    grade_announcement = db.StringField(required=True)
    description = db.Stringfield(required=True)#you have to input the descrip so you can post the announcement.

class view_announcement(db.Document):
    courses_announcement = db.StringField(required=True)
    grade_announcement = db.StringField(required=True)
    