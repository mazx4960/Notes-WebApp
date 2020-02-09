"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

from flask import (
    request, render_template, redirect, session, flash, url_for, make_response
)
from . import auth
from .forms import LoginForm, SignUpForm
from ..utils.functions import *
from ..models import db, User


#########
# Views #
#########


def login_user(user_id, username):
    session['username'] = username
    session['user_id'] = user_id
    update_last_login(user_id)

    response = make_response(redirect(url_for('main.today')))
    response.set_cookie(key='user_id', value=str(user_id), max_age=24 * 60 * 60)
    response.set_cookie(key='username', value=username, max_age=24 * 60 * 60)
    return response


@auth.route('/login/', methods=('GET', 'POST'))
def login():
    """Login Page"""
    if request.cookies.get('user_id') and request.cookies.get('username'):
        session['user_id'] = request.cookies.get('user_id')
        session['username'] = request.cookies.get('username')
        update_last_login(session['user_id'])
        return render_template('main/index.html', username=session['username'])

    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = request.form['username']
        password = (request.form['password'])
        user_id = check_user_exist(username, password)

        if user_id:
            response = login_user(user_id, username)
            return response
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

        # TODO: fix the sign up form error
        # TODO: use a web token to verify his email before adding him
        add_new_user(username, email, password_hash, date_created)

        user_id = check_user_exist(username, password_hash)
        response = login_user(user_id, username)
        return response

    return render_template('auth/signup.html', form=signup_form)


@auth.route("/logout/")
def logout():
    """Logging out"""

    response = make_response(redirect(url_for('auth.login')))

    if request.cookies.get('user_id'):
        response.set_cookie(key='user_id', value=str(session['user_id']), max_age=0)
        response.set_cookie(key='username', value=session['username'], max_age=0)

    session['username'] = None
    session['user_id'] = None

    return response
