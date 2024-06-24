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
    
class Bulletin(db.Document):
    name = db.StringField(required=True)
    content =  db.StringField(required=False)
    # course = db.ReferenceField(Course)

class Attendance(db.Document):
    course_name = db.StringField(required=True)
    student_name= db.StringField(required=True)
    attendance= db.BooleanField(required=False, default=True)


class Course_Activity(db.Document):
    course_name=db.StringField(required=True) 
    activity_type=db.StringField(required=True) #could be assignment, could be exam (UAS/UTS)
    deadline=db.StringField(required=True)

class Score(db.Document):
    course_name = db.StringField(required=True)
    activity_type=db.StringField(required=True)
    student_name= db.StringField(required=True)
    score = db.IntField(blank=True, null=True) #so that the field is provided but we can leave it as blank/null before updating
