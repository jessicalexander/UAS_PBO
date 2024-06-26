from flask import Blueprint
from flask_restful import Api
from resource.eticket import ETicketAPI

eticket_blueprint = Blueprint("eticket_api", __name__)
eticket_blueprint_api = Api(eticket_blueprint)

eticket_blueprint_api.add_resource(
    ETicketAPI, "/eticket"
)
eticket_blueprint_api.add_resource(
    ETicketAPI, "/eticket/<string:id>"
)