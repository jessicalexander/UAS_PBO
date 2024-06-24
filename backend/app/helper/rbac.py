from functools import wraps
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request, get_jwt
from model.user import User
from flask import abort, current_app, jsonify
from mongoengine.errors import DoesNotExist

# def role_required(required_level):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             user_id = get_jwt_identity()
#             current_app.logger.info(f"User ID from JWT: {user_id}")
#             try:
#                 user = User.objects.get(id=user_id)
#                 current_app.logger.info(f"User found: {user.username}, Userlevel: {user.userlevel}")
#             except DoesNotExist:
#                 current_app.logger.error("User not found")
#                 abort(401, "User not found")
#             if user.userlevel > required_level:
#                 current_app.logger.error(f"Permission denied for user: {user.username}, Userlevel: {user.userlevel}, Required level: {required_level}")
#                 abort(403, "Permission denied")
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator

USER_LEVELS = {
    "super_admin": 0,
    "operator": 1,
    "professor": 2,
    "student": 3
}

def user_level_required(minimum_level):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get("user_level") is not None and claims["user_level"] <= minimum_level:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Access forbidden!. Insufficient user level"), 403
        return decorator
    return wrapper