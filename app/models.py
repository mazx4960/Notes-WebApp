"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

from flask_sqlalchemy import SQLAlchemy


#################
# Model Classes #
#################

db = SQLAlchemy()


class User(db.Model):
    """Model for users"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    date_created = db.Column(db.String(32))
    last_login = db.Column(db.String(32))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Notes(db.Model):
    """Model for notes"""

    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    parent_subject = db.Column(db.String(255))
    notes_hash = db.Column(db.String(100))
    date_created = db.Column(db.String(32))
    last_edited = db.Column(db.String(32))
    last_accessed = db.Column(db.String(32))

    def __repr__(self):
        return '<Note {}>'.format(self.title)
