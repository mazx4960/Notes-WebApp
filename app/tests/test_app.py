"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

import os
import tempfile

import pytest

from app import create_app
from app import db
from app import init_db

#############
# Functions #
#############


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""

    # create the app with common test config
    app = create_app(environment='testing')

    # create the database and load test data
    with app.app_context():
        init_db()

    yield app


@pytest.fixture
def client(app):
    """A test client for the app"""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username="test", password="password"):
        return self._client.post(
            "/auth/login", data={"username": username, "password": password}
        )

    def logout(self):
        return self._client.get("/auth/logout")


@pytest.fixture
def auth(client):
    return AuthActions(client)
