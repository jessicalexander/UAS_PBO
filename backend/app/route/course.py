from flask import Blueprint
from flask_restful import Api
from resource.course import CourseAPI, CourseListAPI,BulletinAPI, BulletinListAPI, AttendanceAPI, AttendanceListAPI, Course_ActivityAPI, Course_ActivityListAPI, ScoreAPI, ScoreListAPI, ScoreStudentListAPI, ScoreCourseListAPI 
from resource.announcement import AnnouncementAPI

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
    AttendanceListAPI, "/attendance/<string:student_name>"
)

course_blueprint_api.add_resource(
    Course_ActivityAPI, "/course_activity"
)
course_blueprint_api.add_resource(
    Course_ActivityListAPI, "/course_activity/<string:course_name>"
)
course_blueprint_api.add_resource(
    ScoreAPI, "/Score"
)
course_blueprint_api.add_resource(
    ScoreListAPI, "/Score/<string:score_id>"
)
course_blueprint_api.add_resource(
    ScoreStudentListAPI, "/Score/<string:student_name>"
)

course_blueprint_api.add_resource(
    ScoreCourseListAPI, "/Score/<string:course_name>"
)

course_blueprint_api.add_resource(
    AnnouncementAPI, "/announcement"
)
course_blueprint_api.add_resource(
    AnnouncementAPI, "/announcement/<string:content_announcement>"
)
course_blueprint_api.add_resource(
    AnnouncementAPI, "/announcement/<string:calender_announcement>"
)