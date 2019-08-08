"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators


################
# Form Classes #
################

class LoginForm(FlaskForm):
    username = StringField("username", [validators.required('Please enter '
                                                            'your username')])
    password = PasswordField("password", [validators.required('Please enter '
                                                              'your password'
                                                              '')])
    submit = SubmitField('Login')
