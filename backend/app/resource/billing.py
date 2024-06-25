from flask import request, jsonify, abort, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import current_app as app
from marshmallow.exceptions import ValidationError
from mongoengine.errors import NotUniqueError
from werkzeug.exceptions import UnprocessableEntity, Conflict

from model.billing import Billing, User
from helper.schema import BillingSchema

class BillingListAPI(Resource):
    @jwt_required()
    def get(self):
        billing = Billing.objects()
        serialized_payload = BillingSchema(many=True).dump(billing)
        return serialized_payload, 200

    @jwt_required()
    def get(self,status):
        try:
            status = Billing.objects.filter(status=status) #paid or unpaid
            serialized = BillingSchema(many=True).dump(status)
            return serialized, 200
        except Exception as e:
            return {'message': str(e)}, 422

class BillingAPI(Resource):
    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            student_name = data ["student_name"]
            billing = data["billing"]
            tahapan = Billing(student_name=student_name, billing=billing)
            tahapan.save()
            serialized = BillingSchema().dump(tahapan)
            return serialized, 200
        except Exception as e:
            return {'message': str(e)}, 422

    @jwt_required()
    def put(self, billing_id):
        billing = Billing.objects.get(id=billing_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.update_billing()
        for key, value in serialized_payload.items():
            setattr(billing, key, value)
        billing.save()
        serialized_payload = BillingSchema().dump(billing)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, billing_id):        
        billing = Billing.objects.get(id=billing_id)
        billing.delete()
        app.logger.info("Course with id %s deleted", billing_id)
        msg={"message": "Course: {} deleted".format(billing_id)}
        return msg, 200