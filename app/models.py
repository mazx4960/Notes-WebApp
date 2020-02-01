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


class Followers(db.Model):
    """Model for followers"""

    __tablename__ = 'followers'

    id = db.Column(db.Integer, primary_key=True)
    date_followed = db.Column(db.String(32))
    follower = db.Column(db.Integer)  # follower is the user who is following
    followed = db.Column(db.Integer)  # followed is the user who is being followed

    def __repr__(self):
        return '<Follower_id {}>'.format(self.id)


class Notes(db.Model):
    """Model for notes"""

    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.String(32))
    last_edited = db.Column(db.String(32))
    private = db.Column(db.Boolean)
    parent_folder_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    body = db.Column(db.String(255))
    body_markdown = db.Column(db.String(255))
    user_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Note {}>'.format(self.title)


class Folders(db.Model):
    """Model for Folder Names"""

    __tablename__ = 'folders'

    id = db.Column(db.Integer, primary_key=True)
    folder_name = db.Column(db.String(255))
    user_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Folder {}>'.format(self.folder_name)


class Notes_Permissions(db.Model):
    """Model for notes permissions"""

    __tablename__ = 'notes_permissions'

    id = db.Column(db.Integer, primary_key=True)
    date_shared = db.Column(db.String(32))
    note_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Note_permission {}>'.format(self.id)


class Notes_tag(db.Model):
    """Model for tags of notes"""

    __tablename__ = 'notes_tag'

    id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.Integer)
    tag_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Notes_tag {}>'.format(self.id)


class Tags(db.Model):
    """Model for notes permissions"""

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer) # to record down who started the tag
    tag = db.Column(db.String(255))

    def __repr__(self):
        return '<Note_permission {}>'.format(self.id)