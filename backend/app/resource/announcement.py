from flask import request, jsonify, abort, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import current_app as app
from marshmallow.exceptions import ValidationError
from mongoengine.errors import NotUniqueError
from werkzeug.exceptions import UnprocessableEntity, Conflict

import helper.validator as validator
from model.course import Course, User, Bulletin, Attendance, Course_Activity, Score
from model.announcement import Announcement
from helper.schema import CourseSchema, BulletinSchema, AttendanceSchema, Course_ActivitySchema, ScoreSchema, AnnouncementSchema

class AnnouncementAPI(Resource):
    @jwt_required()
    def get(self, content_announcement, calender_announcement):
        content_announcement = content_announcement.objects()
        calender_announcement = calender_announcement.objects()
        serialized_payload = AnnouncementSchema(many=True).dump(content_announcement)
        serialized_payload = AnnouncementSchema(many=True).dump(calender_announcement)
        return serialized_payload, 200
    def post(self):
        try:
            data = request.get_json()
            content_announcement = data ["content_announcement"]
            calender_announcement = data ["calender_announcement"]
            description = data ["description"]
            tahapan = Announcement(content_announcement=content_announcement, calender_announcement = calender_announcement, description=description)
            tahapan.save()
            serialized = AnnouncementSchema().dump(tahapan)
            return serialized, 200
        except Exception as e:
            return {'message': str(e)}, 422
        
    
