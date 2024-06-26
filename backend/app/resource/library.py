from flask import request, jsonify, abort, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import current_app as app
from marshmallow.exceptions import ValidationError
from mongoengine.errors import NotUniqueError
from werkzeug.exceptions import UnprocessableEntity, Conflict

from model.library import Book, Journal, User
from helper.schema import BookSchema,JournalSchema
class BookListAPI(Resource):
    @jwt_required()
    def get(self):
        book = Book.objects()
        serialized_payload = BookSchema(many=True).dump(book)
        return serialized_payload, 200

    @jwt_required()
    def get(self,title): 
        try:
            title = Book.objects.filter(title=title) 
            serialized = BookSchema(many=True).dump(title)
            return serialized, 200
        except Exception as e:
            return {'message': str(e)}, 422
    @jwt_required()
    def get(self,author): 
        try:
            author = Book.objects.filter(author=author) 
            serialized = BookSchema(many=True).dump(author)
            return serialized, 200
        except Exception as e:
            return {'message': str(e)}, 422

class BookAPI(Resource):
    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            title = data ["title"]
            author = data["author"]
            publisher = data["publisher"]
            publication_year = data["publication_year"]
            genre = data["genre"]
            tahapan = Book(title=title, author=author, publisher=publisher, publication_year=publication_year, genre=genre)
            tahapan.save()
            serialized = BookSchema().dump(tahapan)
            return serialized, 200
        except Exception as e:
            return {'message': str(e)}, 422

    @jwt_required()
    def put(self, book_id):
        book = Book.objects.get(id=book_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.update_book()
        for key, value in serialized_payload.items():
            setattr(book, key, value)
        book.save()
        serialized_payload = BookSchema().dump(book)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, book_id):        
        billing = Book.objects.get(id=book_id)
        billing.delete()
        app.logger.info("Book with id %s deleted", book_id)
        msg={"message": "Book: {} deleted".format(book_id)}
        return msg, 200

class JournalListAPI(Resource):
    @jwt_required()
    def get(self):
        journal = Journal.objects()
        serialized_payload = JournalSchema(many=True).dump(journal)
        return serialized_payload, 200

    @jwt_required()
    def get(self,title): 
        try:
            title = Journal.objects.filter(title=title) 
            serialized = JournalSchema(many=True).dump(title)
            return serialized, 200
        except Exception as e:
            return {'message': str(e)}, 422
    @jwt_required()
    def get(self,author): 
        try:
            author = Journal.objects.filter(author=author) 
            serialized = JournalSchema(many=True).dump(author)
            return serialized, 200
        except Exception as e:
            return {'message': str(e)}, 422

class JournalAPI(Resource):
    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            title = data ["title"]
            author = data["author"]
            publication_year = data["publication_year"]
            tahapan = Journal(title=title, author=author, publication_year=publication_year)
            tahapan.save()
            serialized = JournalSchema().dump(tahapan)
            return serialized, 200
        except Exception as e:
            return {'message': str(e)}, 422

    @jwt_required()
    def put(self, journal_id):
        journal = Journal.objects.get(id=journal_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.update_journal()
        for key, value in serialized_payload.items():
            setattr(journal, key, value)
        journal.save()
        serialized_payload = JournalSchema().dump(journal)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, journal_id):        
        billing = Journal.objects.get(id=journal_id)
        billing.delete()
        app.logger.info("Journal with id %s deleted", journal_id)
        msg={"message": "Journal: {} deleted".format(journal_id)}
        return msg, 200