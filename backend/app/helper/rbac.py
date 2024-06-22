from functools import wraps
from flask_jwt_extended import get_jwt_identity
from model.user import User
from flask import abort

def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_id = get_jwt_identity()
            user = User.objects.get(id=user_id)
            if user.userlevel > role:
                abort(403, "Permission denied")
            return func(*args, **kwargs)
        return wrapper
    return decorator
