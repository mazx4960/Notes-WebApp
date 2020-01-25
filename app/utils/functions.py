"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from functools import reduce

from app.models import db
from app.models import User, Followers, Notes, Folders, Notes_Permissions, Notes_tag, Tags

from sqlalchemy import and_

#############
# Functions #
#############


""" ############# Adding to database ############# """


def add_new_user(username, email, password_hash, date_created):
    """Add a new user to the database"""

    new_user = User(username=username,
                    email=email,
                    password_hash=password_hash,
                    date_created=date_created,
                    last_login=date_created)
    db.session.add(new_user)
    db.session.commit()


def add_new_note(private, parent_folder_id, title, body, user_id):
    """Add a new note to the database"""

    new_note = Notes(date_created=datetime.now(),
                     last_edited=datetime.now(),
                     private=private,
                     parent_folder_id=parent_folder_id,
                     title=title,
                     body=body,
                     body_markdown=body,
                     user_id=user_id)

    db.session.add(new_note)
    db.session.commit()


""" ############# Updating or deleting from database ############# """


def delete_note(note_id):
    pass


def update_note(note_id):
    pass


""" ############# Retrieving from database ############# """


def get_note_by_id(note_id):
    """Get the notes data"""

    note = Notes.query.filter(Notes.id == note_id).first()
    return note


def get_notes(user_id):
    """Returns a list of the notes title written by the user"""

    notes = Notes.query.filter(Notes.user_id == user_id).all()
    return notes


def get_folder_names_ids(user_id):
    """Returns a list of all the folder names created by the user"""

    folder_ids = flatten_2d_list(Folders.query.filter(Folders.user_id == user_id).values('id'))
    folder_names = flatten_2d_list(Folders.query.filter(Folders.user_id == user_id).values('folder_name'))
    folders = zip(map(str, folder_ids), folder_names)
    return folders


def flatten_2d_list(list):
    return reduce(lambda a, b: a+b, list)


""" ############# Validation functions ############# """


def check_user_exist(username, password):
    """Checking user credentials. Returns user_id if found"""

    user = User.query.filter(User.username == username).first()

    if user is not None and check_password_hash(user.password_hash, password):
        return user.id
    else:
        return False


def validate_access_to_note(note_id, user_id):
    """Check if a particular user has access to the note"""

    note = Notes.query.filter(Notes.id == note_id).first()

    if note is None:
        return False

    if note.private:
        note_permission = Notes_Permissions.query.filter(
            and_(
                Notes_Permissions.note_id==note_id,
                Notes_Permissions.user_id==user_id
            )
        ).all()
        if note_permission is None:
            return False

    return True

