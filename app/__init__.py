"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

from flask import Flask
import logging

from app.models import db, User, Notes

from datetime import datetime
from werkzeug.security import generate_password_hash
import hashlib, base64

##############
# Blueprints #
##############

from .main import main as main_blueprint
from .auth import auth as auth_blueprint

###########
# Factory #
###########


def init_db():
    db.create_all()

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

    test_note = Notes(
        user_id = 1,
        title = 'This is a test note',
        parent_subject = 'None',
        notes_hash=(base64.b64encode(hashlib.md5(b'This is a test note').digest())).decode('ascii'),
        date_created=datetime.now(),
        last_edited=datetime.now(),
        last_accessed=datetime.now()
    )

    guest_note = Notes(
        user_id = 2,
        title = 'This is a guest note',
        parent_subject = 'None',
        notes_hash=(base64.b64encode(hashlib.md5(b'This is a guest note').digest())).decode('ascii'),
        date_created=datetime.now(),
        last_edited=datetime.now(),
        last_accessed=datetime.now()
    )

    db.session.add(test)
    db.session.add(guest)

    db.session.add(test_note)
    db.session.add(guest_note)

    db.session.commit()


def create_app(environment=None, init=False):
    """Factory method to create app instance"""

    app = Flask(__name__)
    # logging.basicConfig(filename='logs/blog.log', level=logging.DEBUG)

    # development -> staging -> production -> testing
    if environment == 'testing':
        app.config.from_object("config.TestingConfig")
    elif environment == 'production':
        app.config.from_object("config.ProductionConfig")
    elif environment == 'staging':
        app.config.from_object("config.StagingConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)

    if init:
        with app.app_context():
            init_db()

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
