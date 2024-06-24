from flask import Blueprint
from flask_restful import Api
from resource.course import CourseAPI, CourseListAPI,BulletinAPI, BulletinListAPI, AttendanceAPI, Course_ActivityAPI, ScoreAPI


course_blueprint = Blueprint("course_api", __name__)
course_blueprint_api = Api(course_blueprint)

course_blueprint_api.add_resource(
    CourseAPI, "/courses/<string:course_id>"
)
course_blueprint_api.add_resource(
    CourseListAPI, "/courses"
)

course_blueprint_api.add_resource(
    BulletinListAPI, "/bulletin"
)

course_blueprint_api.add_resource(
    BulletinAPI, "/bulletin/<string:bulletin_id>"
)

course_blueprint_api.add_resource(
    AttendanceAPI, "/attendance"
)

course_blueprint_api.add_resource(
    AttendanceAPI, "/attendance/<string:student_name>"
)

course_blueprint_api.add_resource(
    Course_ActivityAPI, "/course_activity"
)

course_blueprint_api.add_resource(
    ScoreAPI, "/Score"
)
course_blueprint_api.add_resource(
    ScoreAPI, "/Score/<string:student_name>"
)

course_blueprint_api.add_resource(
    ScoreAPI, "/Score/<string:course_name>"
)
