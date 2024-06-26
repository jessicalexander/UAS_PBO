from flask import Blueprint
from flask_restful import Api
from resource.library import BookListAPI, BookAPI,JournalListAPI,JournalAPI

library_blueprint = Blueprint("library_api", __name__)
library_blueprint_api = Api(library_blueprint)

library_blueprint_api.add_resource(
    BookListAPI, "/book"
)
library_blueprint_api.add_resource(
    BookListAPI, "/book/<string:title>"
)
library_blueprint_api.add_resource(
    BookListAPI, "/book/string:author>"
)
library_blueprint_api.add_resource(
    BookAPI, "/book/<string:book_id>"
)
library_blueprint_api.add_resource(
    JournalListAPI, "/journal"
)
library_blueprint_api.add_resource(
    JournalListAPI, "/journal/<string:title>"
)
library_blueprint_api.add_resource(
    JournalListAPI, "/journal/<string:author>"
)
library_blueprint_api.add_resource(
    JournalAPI, "/journal/<string:journal_id>"
)