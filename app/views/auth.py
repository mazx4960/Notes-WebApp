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
from app.utils.forms import LoginForm
from app.utils import functions
from app.models import User


############
# Settings #
############

bp = Blueprint('auth', __name__)


#########
# Views #
#########

@bp.route('/')
def home_page():
    """Home Page"""
    try:
        if session['username']:
            return render_template('notes/homepage.html', username=session[
                'username'])
        return render_template('notes/homepage.html')
    except (KeyError, ValueError):
        return render_template('notes/homepage.html')


@bp.route('/login/', methods=('GET', 'POST'))
def login():
    """Login Page"""

    form = LoginForm()
    if form.validate_on_submit():
        username = request.form['username']
        password_hash = functions.generate_password_hash(request.form[
                                                           'password'])
        user = User.query.filter(User.username == username and
                                 User.password_hash == password_hash).first()
        if user:
            session['username'] = user.username
            session['id'] = user.id
            return redirect('/profile/')
        else:
            flash('Username/Password Incorrect!')
    return render_template('auth/login.html', form=form)


@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    """Sign up page"""

    pass


@bp.route("/logout/")
def logout():
    """Logging out"""

    session['username'] = None
    session['id'] = None
    return login()
