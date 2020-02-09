"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from inspect import getmembers, isfunction
from app.utils import filters
from app.sample_data import add_sample_data

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

    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from app.models import db
    db.init_app(app)
    # logging.basicConfig(filename='logs/blog.log', level=logging.DEBUG)

    # development -> staging -> production -> testing
    if environment == 'testing':
        app.config.from_object("instance.config.TestingConfig")
    elif environment == 'production':
        app.config.from_object("instance.config.ProductionConfig")
    elif environment == 'staging':
        app.config.from_object("instance.config.StagingConfig")
    else:
        app.config.from_object("instance.config.DevelopmentConfig")

    if init:
        with app.app_context():
            db.create_all()
            add_sample_data(db)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    custom_filters = {name: function for name, function in getmembers(filters) if isfunction(function)}
    app.jinja_env.filters.update(custom_filters)

    return app
