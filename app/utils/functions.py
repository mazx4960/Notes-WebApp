"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from app.models import db, User, Notes

#############
# Functions #
#############


def add_new_user(username, email, password_hash, date_created):
    """Add a new user to the database"""

    new_user = User(username=username,
                    email=email,
                    password_hash=password_hash,
                    date_created=date_created,
                    last_login=date_created)
    db.session.add(new_user)
    db.session.commit()


def check_user_exist(username, password):
    """Checking user credentials. Returns user_id if found"""

    user = User.query.filter(User.username == username).first()

    if user is not None and check_password_hash(user.password_hash, password):
        return user.id
    else:
        return False


def get_notes(user_id):
    """Returns a list of of the notes title written by the user"""

    notes = Notes.query.filter(Notes.user_id == user_id).all()
    return notes
