from flask import Blueprint
from flask_restful import Api

from resource.billing import BillingAPI, BillingListAPI

billing_blueprint = Blueprint("billing_api", __name__)
billing_blueprint_api = Api(billing_blueprint)

billing_blueprint_api.add_resource(
    BillingListAPI, "/billings"
)
billing_blueprint_api.add_resource(
    BillingAPI, "/billing/<string:student_name>"
)