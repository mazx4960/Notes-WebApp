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
from . import auth
from .forms import LoginForm, SignUpForm
from ..utils.functions import generate_password_hash, datetime
from ..utils.functions import add_new_user, check_user_exist
from ..models import db, User


#########
# Views #
#########


@auth.route('/login/', methods=('GET', 'POST'))
def login():
    """Login Page"""

    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = request.form['username']
        password = (request.form['password'])
        user_id = check_user_exist(username, password)

        if user_id:
            session['username'] = username
            session['user_id'] = user_id
            # TODO: add cookies to user's browser
            return redirect(url_for('main.today'))
        else:
            flash('Username/Password Incorrect!')
    return render_template('auth/login.html', form=login_form)


@auth.route('/signup/', methods=('GET', 'POST'))
def signup():
    """Sign up page"""

    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        username = request.form['username']
        password_hash = generate_password_hash(request.form['password'])
        email = request.form['email']
        date_created = datetime.now()
        # TODO: use a web token to verify his email before adding him
        add_new_user(username, email, password_hash, date_created)

        user_id = check_user_exist(username, password_hash)
        session['username'] = username
        session['user_id'] = user_id
        # TODO: add cookies to user's browser

        return redirect(url_for('main.today'))

    return render_template('auth/signup.html', form=signup_form)


@auth.route("/logout/")
def logout():
    """Logging out"""

    session['username'] = None
    session['user_id'] = None
    return login()
