"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

from flask import Flask
import logging

from app.models import db
from app.sample_data import init_db

##############
# Blueprints #
##############

from .main import main as main_blueprint
from .auth import auth as auth_blueprint

###########
# Factory #
###########


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
