from utils import db
from mongoengine import Document, StringField, DateField

class ETicket(db.Document):
    judul_laporan = db.StringField(required=True)
    tanggal_laporan = db.DateField(required=True)
    deskripsi = db.StringField(required=True)
    pelapor = db.StringField(required=True)
    status = db.StringField(required=True, default="open")