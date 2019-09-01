"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

from flask import (
    Blueprint, request, render_template,
    redirect, session, flash
)
from app.utils.decorators import login_required
from app.utils.functions import generate_password_hash, datetime
from app.utils.functions import get_notes
from app.models import db, User


############
# Settings #
############

bp = Blueprint('notes', __name__)


#########
# Views #
#########

@bp.route('/my_notes')
@login_required
def my_notes():
    """Notes Page"""

    notes = get_notes(session['user_id'])
    return render_template('notes/my_notes.html', notes=notes, username=session['username'])


@bp.route('/add_notes')
@login_required
def add_notes():
    """Adding Notes Page"""

    pass
