"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

from app.models import db
from app.models import User, Followers, Notes, Folders, Notes_Permissions, Notes_tag, Tags

from datetime import datetime
from werkzeug.security import generate_password_hash


def init_db():
    db.create_all()


def add_sample_data():

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

    db.session.add(test)
    db.session.add(guest)
    db.session.add(mazx)

    db.session.commit()

    ################# Followers #################

    test_follow_guest = Followers(
        date_followed=datetime.now(),
        follower=1,
        followed=2
    )

    db.session.add(test_follow_guest)

    db.session.commit()

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

    db.session.add(test_note)
    db.session.add(guest_note)

    db.session.commit()

    ################# Folders #################

    test_folder = Folders(
        folder_name='test_folder',
        user_id=1
    )

    guest_folder = Folders(
        folder_name='guest_folder',
        user_id=2
    )

    db.session.add(test_folder)
    db.session.add(guest_folder)

    db.session.commit()

    ################# Notes_Permissions #################

    test_note_allow_mazx = Notes_Permissions(
        date_shared=datetime.now(),
        note_id=1,
        user_id=3
    )

    db.session.add(test_note_allow_mazx)

    db.session.commit()

    ################# Notes_tag #################

    test_note_test_tag = Notes_tag(
        note_id=1,
        tag_id=1
    )

    guest_note_guest_tag = Notes_tag(
        note_id=2,
        tag_id=2
    )

    db.session.add(test_note_test_tag)
    db.session.add(guest_note_guest_tag)

    db.session.commit()

    ################# Tags #################

    test_tag = Tags(
        user_id=1,
        tag='testtag'
    )

    guest_tag = Tags(
        user_id=2,
        tag='guesttag'
    )

    db.session.add(test_tag)
    db.session.add(guest_tag)

    db.session.commit()