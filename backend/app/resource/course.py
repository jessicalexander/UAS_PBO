from flask import request, jsonify, abort, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import current_app as app
from marshmallow.exceptions import ValidationError
from mongoengine.errors import NotUniqueError
from werkzeug.exceptions import UnprocessableEntity, Conflict

import helper.validator as validator
from model.course import Course, User, Bulletin, Attendance, Course_Activity, Score
from helper.schema import CourseSchema, BulletinSchema, AttendanceSchema, Course_ActivitySchema, ScoreSchema

class CourseListAPI(Resource):
    @jwt_required()
    def get(self):
        courses = Course.objects()
        serialized_payload = CourseSchema(many=True).dump(courses)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_course()
        course = Course(**serialized_payload)
        course.save()
        serialized_payload = CourseSchema().dump(course)
        return serialized_payload, 200

class CourseAPI(Resource):
    @jwt_required()
    def get(self, course_id):
        course = Course.objects.get(id=course_id)
        serialized_payload = CourseSchema().dump(course)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, course_id):
        course = Course.objects.get(id=course_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_course()
        for key, value in serialized_payload.items():
            setattr(course, key, value)
        course.save()
        serialized_payload = CourseSchema().dump(course)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, course_id):        
        course = Course.objects.get(id=course_id)
        course.delete()
        app.logger.info("Course with id %s deleted", course_id)
        msg={"message": "Course: {} deleted".format(course_id)}
        return msg, 200
    
class BulletinListAPI(Resource):
    @jwt_required()
    def get(self):
        bulletin = Bulletin.objects()
        serialized_payload = BulletinSchema(many=True).dump(bulletin)
        return serialized_payload, 200

class BulletinAPI(Resource):
    @jwt_required()
    def get(self, bulletin_id):
        app.logger.info("bulletin id: {}".format(bulletin_id))
        bulletin = Bulletin.objects.get(id=bulletin_id)
        serialized_payload = BulletinSchema().dump(bulletin)
        return serialized_payload, 200
    #TODO:
    # CRUD

class AttendanceAPI(Resource):
    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            course_name = data["course_name"]
            student_name = data ["student_name"]
            attendance = data["attendance"]
            tahapan = Attendance(course_name=course_name, student_name=student_name, attendance=attendance)
            tahapan.save()
            serialized = AttendanceSchema().dump(tahapan)
            return serialized, 200
        except Exception as e:
            return {'message': str(e)}, 422

class AttendanceListAPI(Resource):    
    @jwt_required()
    def get(self, student_name):
        attendance = Attendance.objects.get(student_name=student_name)
        serialized_payload = AttendanceSchema().dump(attendance)
        return serialized_payload, 200 
    
    @jwt_required()
    def put(self, student_name):
        attendance = Attendance.objects.get(student_name=student_name)
        payload = request.get_json()
        schema = AttendanceSchema()
        try:
            validated_data = schema.load(payload, partial=True)
        except ValidationError as err:
            return err.messages, 400\
            
        for key, value in validated_data.items():
            setattr(attendance, key, value)
        attendance.save()
        
        serialized_payload = schema.dump(attendance)
        return serialized_payload, 200

class Course_ActivityAPI(Resource):
    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            course_name = data["course_name"]
            activity_type = data ["activity_type"]
            deadline = data["deadline"]
            tahapan = Course_Activity(course_name=course_name, activity_type=activity_type, deadline=deadline)
            tahapan.save()
            serialized = Course_ActivitySchema().dump(tahapan)
            return serialized, 200
        except Exception as e:
            return {'message': str(e)}, 422
        
class Course_ActivityIdAPI(Resource):
    @jwt_required()
    def put(self, course_activity_id):
        try:
            data = request.get_json()
            course_activity = Course_Activity.objects.get(id=course_activity_id)

            if 'activity_type' in data:
                course_activity.activity_type = data['activity_type']
            
            if 'deadline' in data:
                course_activity.deadline = data['deadline']
            
            course_activity.save()
            serialized = Course_ActivitySchema().dump(course_activity)
            return serialized, 200
        except Course_Activity.DoesNotExist:
            return {'message': 'Course activity not found'}, 404
        except Exception as e:
            return {'message': str(e)}, 422
        
    def delete(self, course_activity_id):
        try:
            course_activity = Course_Activity.objects.get(id=course_activity_id)
            course_activity.delete()
            return {'message': 'Course activity deleted successfully'}, 200
        except Course_Activity.DoesNotExist:
            return {'message': 'Course activity not found'}, 404
        except Exception as e:
            return {'message': str(e)}, 422
        
class Course_ActivityListAPI(Resource):
    @jwt_required()
    def get(self, course_name):
        course_name = Course_Activity.objects.get(course_name=course_name)
        serialized_payload = Course_ActivitySchema().dump(course_name)
        return serialized_payload, 200

class ScoreAPI(Resource):
    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            course_name = data["course_name"]
            activity_type = data ["activity_type"]
            student_name = data ["student_name"]
            score = data ["score"]
            tahapan = Score(course_name=course_name, activity_type=activity_type, student_name=student_name, score=score)
            tahapan.save()
            serialized = ScoreSchema().dump(tahapan)
            return serialized, 200
        except Exception as e:
            return {'message': str(e)}, 422

class ScoreListAPI(Resource):        
    @jwt_required()
    def put(self, score_id):
        try:
            score = Score.objects.get(id=score_id)
            user = User.objects.get(id=get_jwt_identity())
            serialized_payload = validator.update_score()
            for key, value in serialized_payload.items():
                setattr(score, key, value)
            score.save()
            serialized_payload = ScoreSchema().dump(score)
            return serialized_payload, 200
        except Exception as e:
            return {'message': str(e)}, 422
        
class ScoreStudentListAPI(Resource):        
    def get(self, student_name): #search score by student
        try:
            scores = Score.objects.filter(student_name=student_name)
            serialized = ScoreSchema(many=True).dump(scores)
            return serialized, 200
        except Exception as e:
            return {'message': str(e)}, 422

class ScoreCourseListAPI(Resource):         
    def get(self, course_name): #search score by course
        try:
            scores = Score.objects.filter(course_name=course_name)
            serialized = ScoreSchema(many=True).dump(scores)
            return serialized, 200
        except Exception as e:
            return {'message': str(e)}, 422    