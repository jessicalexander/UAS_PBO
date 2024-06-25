from flask import Blueprint
from flask_restful import Api

from resource.announcement import AnnouncementAPI


announcement_blueprint = Blueprint("announcemente_api", __name__)
announcement_blueprint_api = Api(announcement_blueprint)

announcement_blueprint_api.add_resource(
    AnnouncementAPI, "/announcement"
)
announcement_blueprint_api.add_resource(
    AnnouncementAPI, "/announcement/<string:content_announcement>"
)
announcement_blueprint_api.add_resource(
    AnnouncementAPI, "/announcement/<string:calender_announcement>"
)