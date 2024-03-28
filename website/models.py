from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Diary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    notes = db.relationship('Note')
    shared_with = db.relationship('Shared', backref='diary')

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    edited = db.Column(db.Boolean, default=False)
    diary_id = db.Column(db.Integer, db.ForeignKey('diary.id'), nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    diaries = db.relationship('Diary')
    shared = db.relationship('Shared', backref='user')

class Shared(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    diary_id = db.Column(db.Integer, db.ForeignKey('diary.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

