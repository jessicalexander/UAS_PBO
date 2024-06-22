from flask import request
from datetime import timedelta
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from marshmallow.exceptions import ValidationError
from helper.schema import UserSchema, LoginSchema
from model.user import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from helper.rbac import role_required  # Import the decorator

from flask import current_app as app


class RegisterAPI(Resource):
    def post(self):
        try:
            data = request.get_json()
            result = UserSchema().load(data)
            user = User(**result)
            user.hash_password()
            user.save()
            return UserSchema().dump(user), 200
        except ValidationError as e:
            return {'errors': e.messages}, 400
        except FieldDoesNotExist:
            return {'error': 'Request is missing required fields'}, 400
        except NotUniqueError:
            return {'error': 'username address already exists'}, 400

class LoginAPI(Resource):
    def post(self):
        try:
            payload = LoginSchema().load(request.get_json())
            user = User.objects.get_or_404(username=payload['username'])
            authorized = user.check_password(payload['password'])
            if not authorized:
                return {'error': 'Email or password invalid'}, 401
            expires = timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            return {'token': access_token}, 200

        except Exception as e:
            app.logger.error("Error: {}".format(e))
            return {'message': "Server error"}, 500

class UserManagementAPI(Resource):
    @jwt_required()
    @role_required(0)  # Only super admin
    def post(self):
        data = request.get_json()
        user = User(**data)
        user.hash_password()
        user.save()
        return UserSchema().dump(user), 200

    @jwt_required()
    @role_required(0)  # Only super admin
    def put(self, user_id):
        data = request.get_json()
        user = User.objects.get(id=user_id)
        user.update(**data)
        return UserSchema().dump(user), 200
        


