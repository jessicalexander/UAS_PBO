from flask import request, jsonify, abort, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import current_app as app
from marshmallow.exceptions import ValidationError
from mongoengine.errors import NotUniqueError
from werkzeug.exceptions import UnprocessableEntity, Conflict

from model.eticket import ETicket
from helper.schema import ETicketSchema

class ETicketAPI(Resource):
    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            if "judul_laporan" in data:
                etickets = ETicket.objects(judul_laporan=data["judul_laporan"])
            elif "tanggal_laporan" in data:
                etickets = ETicket.objects(tanggal_laporan=data["tanggal_laporan"])
            else:
                etickets = ETicket.objects()
                
            serialized_payload = ETicketSchema(many=True).dump(etickets)
            return serialized_payload, 200
        except Exception as e:
            return {'message': str(e)}, 422

    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            judul_laporan = data["judul_laporan"]
            tanggal_laporan = data["tanggal_laporan"]
            deskripsi = data["deskripsi"]
            pelapor = data["pelapor"]
            eticket = ETicket(judul_laporan=judul_laporan, tanggal_laporan=tanggal_laporan, deskripsi=deskripsi, pelapor=pelapor)
            eticket.save()
            serialized = ETicketSchema().dump(eticket)
            return serialized, 200
        except Exception as e:
            return {'message': str(e)}, 422

    @jwt_required()
    def delete(self, id):
        try:
            eticket = ETicket.objects(id=id).first()
            if eticket:
                eticket.delete()
                return {"message": "ETicket deleted successfully"}, 200
            else:
                return {"message": "ETicket not found"}, 404
        except Exception as e:
            return {'message': str(e)}, 422