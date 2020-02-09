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


def delete_note_by_id(note_id):
    note = Notes.query.filter(Notes.id == note_id).first()

    db.session.delete(note)
    db.session.commit()


def update_note(note_id, private, parent_folder_id, title, body):
    note = Notes.query.filter(Notes.id == note_id).first()

    note.private = private
    note.parent_folder_id = parent_folder_id
    note.title = title
    note.body = body
    note.last_edited = datetime.now()

    db.session.commit()


def update_last_login(user_id):
    user = User.query.filter(User.id == user_id).first()

    user.last_login = datetime.now()
    db.session.commit()


""" ############# Retrieving from database ############# """


def get_search_result(search, category, user_id):
    """Getting the result based on the search term and category"""

    if category == 'Users':
        users = get_users_by_name(search)
        return users
    elif category == 'Notes':
        # The note must either be yours or public
        notes = get_notes_by_title(search)
        sieved_notes = sieve_public_notes(notes, user_id)
        sieved_notes.sort(key=lambda note: note.last_edited, reverse=True)
        return sieved_notes
    return []


def sieve_public_notes(notes, user_id):
    """Getting all notes that are public or yours or (shared with you)"""

    sieved_notes = []
    for note in notes:
        if not note.private:
            sieved_notes.append(note)
        elif note.user_id == int(user_id):
            sieved_notes.append(note)
    return sieved_notes


def get_usernames():
    """
    Returns a dictionary of all the username in the data base with their
    user_id as the key and the username as the value

    :return: dictionary of username
    """
    users = User.query.all()

    usernames = {}
    for user in users:
        usernames[user.id] = user.username
    return usernames

def get_users_by_name(username):
    """Getting all the users with username or has username as a substring"""

    users = User.query.filter(User.username.contains(username)).all()
    return list(users)


def get_user_by_id(user_id):
    """Getting all the users with username or has username as a substring"""

    user = User.query.filter(User.id == user_id).first()
    return user


def get_notes_by_title(title):
    """Getting all the notes with title or has title as a substring"""
    notes = Notes.query.filter(Notes.title.contains(title)).all()
    return list(notes)


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


def flatten_2d_list(lst):
    return reduce(lambda a, b: a+b, lst)


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
                Notes_Permissions.note_id == note_id,
                Notes_Permissions.user_id == user_id
            )
        ).all()
        if note_permission is None:
            return False

    return True


""" ############# Miscellaneous functions ############# """


def sort_notes_into_folders(notes, folders):
    """
    sorts notes into a dictionary with the folder names as the key

    :param notes:
        A list of notes objects
    :param folders:
        a list of tuples with each tuple holding (folder_id, folder_name)
    :return:
        a dictionary with all the notes, sorted into their folders as well
        as a all key which stores all the notes

    Note 1: the values in the keys is a list of note objects that is correlated
    to the folder name

    Eg. {
        'test_folder': [Note_obj_1, Note_obj_2, ...],
        'all': [all_note_objs]
    }
    """

    # so that when the note gets appended to the dictionary, it will already be sorted
    notes.sort(key=lambda note: note.last_edited, reverse=True)
    folders = dict(folders)
    notes_sorted_by_folders = {'All':[]}

    # to store all the folder_names even when it has no notes
    for folder_id in folders:
        folder_name = folders[folder_id]
        notes_sorted_by_folders.setdefault(folder_name, [])

    for note in notes:
        if note.parent_folder_id != 0: # note has a folder
            folder_name = folders[str(note.parent_folder_id)]
            notes_sorted_by_folders[folder_name].append(note)

        notes_sorted_by_folders['All'].append(note)

    return notes_sorted_by_folders
