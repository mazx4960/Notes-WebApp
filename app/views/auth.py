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
from app.utils.forms import LoginForm, SignUpForm
from app.utils.functions import generate_password_hash, datetime
from app.utils.functions import add_new_user, check_user_exist
from app.models import db, User


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

    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = request.form['username']
        password = (request.form['password'])
        user_id = check_user_exist(username, password)

        if user_id:
            session['username'] = username
            session['id'] = user_id
            return redirect('/profile/')
        else:
            flash('Username/Password Incorrect!')
    return render_template('auth/login.html', form=login_form)


@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    """Sign up page"""

    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        username = request.form['username']
        password_hash = generate_password_hash(request.form['password'])
        email = request.form['email']
        date_created = datetime.now()
        add_new_user(username, email, password_hash, date_created)

        user_id = check_user_exist(username, password_hash)
        session['username'] = username
        session['user_id'] = user_id

        return redirect('/profile/')

    return render_template('auth/signup.html', form=signup_form)


@bp.route("/logout/")
def logout():
    """Logging out"""

    session['username'] = None
    session['id'] = None
    return login()
