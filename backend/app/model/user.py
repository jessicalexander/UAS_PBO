from flask_bcrypt import generate_password_hash, check_password_hash
from utils import db

class User(db.Document):
    """
    level:
        0=superadmin
        1=operator
        2=professor
        3=student
    """
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    userlevel = db.IntField(default=3) # Default to student
    description = db.StringField(requuired=False)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    def check_password(self, password):
        return check_password_hash(self.password, password)


