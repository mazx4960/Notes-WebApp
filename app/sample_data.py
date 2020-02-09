"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

from app.models import User, Followers, Notes, Folders, Notes_Permissions, Notes_tag, Tags

from datetime import datetime
from werkzeug.security import generate_password_hash

#############
# Functions #
#############


def add_sample_data(db):
    data = get_sample_data()
    for single_data in data:
        db.session.add(single_data)
    db.session.commit()


def get_sample_data():

    data = []

    ################# Users #################

    test = User(
        username='test',
        email='test@example.com',
        password_hash=generate_password_hash('password'),
        date_created=datetime.now(),
        last_login=datetime.now()
    )
    guest = User(
        username='guest',
        email='guest@example.com',
        password_hash=generate_password_hash('password'),
        date_created=datetime.now(),
        last_login=datetime.now()
    )
    mazx = User(
        username='max',
        email='max@example.com',
        password_hash=generate_password_hash('password'),
        date_created=datetime.now(),
        last_login=datetime.now()
    )

    data.append(test)
    data.append(guest)
    data.append(mazx)

    ################# Followers #################

    test_follow_guest = Followers(
        date_followed=datetime.now(),
        follower=1,
        followed=2
    )

    data.append(test_follow_guest)

    ################# Notes #################

    test_note = Notes(
        date_created=datetime.now(),
        last_edited=datetime.now(),
        private=True,
        parent_folder_id=0,
        title='This is a test note',
        body='This is a test content',
        body_markdown='This is a test content',
        user_id=1
    )

    guest_note = Notes(
        date_created=datetime.now(),
        last_edited=datetime.now(),
        private=False,
        parent_folder_id=0,
        title='This is a guest note',
        body='This is a guest content',
        body_markdown='This is a guest content',
        user_id=2
    )

    data.append(test_note)
    data.append(guest_note)

    ################# Folders #################

    test_folder = Folders(
        folder_name='Test Folder',
        user_id=1
    )

    guest_folder = Folders(
        folder_name='Guest Folder',
        user_id=2
    )

    data.append(test_folder)
    data.append(guest_folder)

    ################# Notes_Permissions #################

    test_note_allow_mazx = Notes_Permissions(
        date_shared=datetime.now(),
        note_id=1,
        user_id=3
    )

    data.append(test_note_allow_mazx)

    ################# Notes_tag #################

    test_note_test_tag = Notes_tag(
        note_id=1,
        tag_id=1
    )

    guest_note_guest_tag = Notes_tag(
        note_id=2,
        tag_id=2
    )

    data.append(test_note_test_tag)
    data.append(guest_note_guest_tag)

    ################# Tags #################

    test_tag = Tags(
        user_id=1,
        tag='testtag'
    )

    guest_tag = Tags(
        user_id=2,
        tag='guesttag'
    )

    data.append(test_tag)
    data.append(guest_tag)

    ########################################

    return data

