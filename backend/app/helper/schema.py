from utils import ma
from marshmallow import fields, validate, validates, validates_schema, ValidationError, post_load, pre_load, post_dump
from marshmallow.validate import ContainsOnly
from flask import current_app as app
import config

class UserSchema(ma.Schema):
    id = fields.String(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(max=64))
    password = fields.String(required=True, load_only=True, validate=validate.Length(min=6, max=64))
    userlevel = fields.Integer(default=0)
    description = fields.String()

    @validates_schema
    def validate_username(self, data, **kwargs):
        if not data["username"]:
            raise ValidationError("Username is required")
        if not isinstance(data["username"], str):
            raise ValidationError("Username must be a string")
        
    class Meta:
        ordered = True

class LoginSchema(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

class RegisterSchema(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=64))
    userlevel = fields.Integer(default=0)
    description = fields.String()


class CourseSchema(ma.Schema):
    id = fields.String(dump_only=True)
    kode_mk = fields.String(required=True)
    semester = fields.String(required=True)
    nama_mk = fields.String(required=False)
    sks = fields.Integer(required=False)
    nama_prof = fields.Integer(required=False)
    description = fields.String(required=False)
    user = fields.Nested(UserSchema, required=True, dump_only=True)
    

#TODO: add any schema here

class BulletinSchema(ma.Schema):
    id = fields.String(dump_only=True)
    name = fields.String(required=True)
    content = fields.String(required=False)
    # course = fields.Nested(Course, dump_only=True)

class AttendanceSchema(ma.Schema):
    id = fields.String(dump_only=True)
    course_name = fields.String(required=True)
    student_name= fields.String(required=True)
    attendance= fields.Bool(required=False, default=True)

class Course_ActivitySchema(ma.Schema):
    id = fields.String(dump_only=True)
    course_name=fields.String(required=True)
    activity_type=fields.String(required=True)
    deadline=fields.String(required=True)

class ScoreSchema(ma.Schema):
    id = fields.String(dump_only=True)
    course_name = fields.String(required=True)
    activity_type=fields.String(required=True)
    student_name= fields.String(required=True)
    score=fields.Integer(blank=True, null=True)

class AnnouncementSchema(ma.Schema):
    content_announcement = fields.String(required=True)
    calender_announcement = fields.Date(required=True)
    description = fields.String(required=True)

class BillingSchema(ma.Schema):
    id = fields.String(dump_only=True)
    student_name= fields.String(required=True)
    billing = fields.Integer(blank=True, null=True)
    description = fields.String(required=False)
    status = fields.String(required=False)

class ETicketSchema(ma.Schema):
    judul_laporan = fields.String(required=True)
    tanggal_laporan = fields.Date(required=True)
    deskripsi = fields.String(required=True)
    pelapor = fields.String(required=True)
    status = fields.String(required=True)

class LibrarySchema(ma.Schema):
    id = fields.String(dump_only=True)
    type= fields.String(required=True)
    description= fields.String(required=False)
    
class BookSchema(ma.Schema):
    id = fields.String(dump_only=True)
    title= fields.String(required=True)
    author= fields.String(required=True)
    publisher= fields.String(required=True)
    publication_year = fields.Integer(equired=True)
    genre= fields.String(blank=True, null=True)
    description= fields.String(required=False)

class JournalSchema(ma.Schema):
    id = fields.String(dump_only=True)
    title= fields.String(required=True)
    author= fields.String(required=True)
    publication_year = fields.Integer(rquired=True)
    description= fields.String(required=False)