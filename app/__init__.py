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

##############
# Blueprints #
##############

from app.views import auth

###########
# Factory #
###########


def create_app(environment=None):
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

    app.register_blueprint(auth.bp)

    return app
