from utils import db
from model.user import User

class Billing(db.Document):
    student_name= db.StringField(required=True)
    billing = db.StringField(required=True)
    description = db.StringField(required=False)
    status = db.StringField(required=True)
    