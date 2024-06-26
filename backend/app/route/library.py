from flask import Blueprint
from flask_restful import Api
from resource.library import BookListAPI, BookAPI,JournalListAPI,JournalAPI

billing_blueprint = Blueprint("library_api", __name__)
billing_blueprint_api = Api(billing_blueprint)

billing_blueprint_api.add_resource(
    BookListAPI, "/books"
)
billing_blueprint_api.add_resource(
    BookAPI, "/book/<string:book_id>"
)
billing_blueprint_api.add_resource(
    JournalListAPI, "/journal"
)
billing_blueprint_api.add_resource(
    JournalAPI, "/journal/<string:journal_id>"
)


