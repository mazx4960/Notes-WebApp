"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

from flask import (
    request, render_template, redirect, session, flash, url_for
)
from . import main
from .forms import AddNoteForm
from ..utils.decorators import login_required
from ..utils.functions import generate_password_hash, datetime
from ..utils.functions import get_notes, get_note_by_id, validate_access_to_note
from ..models import db, User


#########
# Views #
#########

@main.route('/')
def index():
    """Home Page"""
    try:
        if session['username']:
            return render_template('main/index.html', username=session['username'])
        return render_template('main/index.html', username=None)
    except (KeyError, ValueError):
        return render_template('main/index.html', username=None)

@main.route('/home')
@login_required
def home_page():
    """Home Page"""

    return render_template('main/home_page.html', username=session['username'])


@main.route('/my_notes')
@login_required
def my_notes():
    """Notes Page"""

    notes = get_notes(session['user_id'])
    return render_template('main/my_notes.html', notes=notes, username=session['username'])


@main.route("/notes/<note_id>/")
@login_required
def view_note(note_id):
    '''
        App for viewing a specific note
    '''
    if validate_access_to_note(note_id, session['user_id']):
        note = get_note_by_id(note_id)
        return render_template('main/view_note.html', note=note, username=session['username'])
    else:
        return render_template('errors/401.html')


@main.route('/notes/add', methods=['GET','POST'])
@login_required
def add_note():
    """Adding Notes Page"""

    add_notes_form = AddNoteForm()
    if add_notes_form.validate_on_submit():
        pass

    return render_template('main/add_notes.html', form=add_notes_form, username=session['username'])


@main.route('/profile')
@login_required
def profile():
    """Profile Page"""

    return render_template('main/profile.html', username=session['username'])