"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

import os
from app import create_app, db
from app.models import User, Notes
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


###################
# Running the app #
###################

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Notes=Notes)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


@manager.command
def test(coverage=False):
    """Run the unit tests."""
    pass


if __name__ == '__main__':
    manager.run()
