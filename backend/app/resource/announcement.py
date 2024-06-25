from flask import request, jsonify, abort, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import current_app as app
from marshmallow.exceptions import ValidationError
from mongoengine.errors import NotUniqueError
from werkzeug.exceptions import UnprocessableEntity, Conflict

import helper.validator as validator
from model.course import Course, User, Bulletin, Attendance, Course_Activity, Score, create_announcement,view_announcement
from helper.schema import CourseSchema, BulletinSchema, AttendanceSchema, Course_ActivitySchema, ScoreSchema,Create_announcementSchema, View_announcementSchema

class View_AnnouncementAPI(Resource):
    @jwt_required()
    def get(self, grade_annoucement, courses_announcement):
        grade_annoucement = grade_annoucement.objects()
        courses_announcement = courses_announcement.objects()
        serialized_payload = CourseSchema(many=True).dump(courses_announcement)
        serialized_payload = View_announcementSchema(many=True).dump(courses_announcement)
        return serialized_payload, 200
    

class Create_AnnouncementAPI(Resource):
    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            course_announcement = data["course_announcement"]
            grade_announcement = data["grade_announcement"]
            description = data["description"]
            
            # Simpan pengumuman ke dalam database menggunakan model create_announcement
            announcement = create_announcement(
                courses_announcement=course_announcement,
                grade_announcement=grade_announcement,
                description=description
            )
            announcement.save()

            # Serialize response using ScoreSchema (adjust based on your schema structure)
            serialized = ScoreSchema().dump(announcement)
            
            return serialized, 200
        except Exception as e:
            return {'message': str(e)}, 422