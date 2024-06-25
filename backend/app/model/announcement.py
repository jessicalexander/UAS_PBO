from utils import db
from model.user import User

class Announcement(db.Document):
    content_announcement = db.StringField(required=True)
    calender_announcement = db.DateField(required=True)
    description = db.Stringfield(required=True)

    