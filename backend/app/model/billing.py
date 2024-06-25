from utils import db

class Billing(db.Document):
    student_id= db.StringField(required=True)
    billing = db.StringField(required=True)
    description = db.StringField(required=False)
    status = db.StringField(required=True)