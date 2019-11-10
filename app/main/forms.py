"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import required, equal_to, length, ValidationError
from wtforms.validators import Email

from app.models import User


################
# Form Classes #
################

class AddNoteForm(FlaskForm):
    """Add Note Form"""

    username = StringField("Username*", [required('Please enter your '
                                                  'username')])
    password = PasswordField("Password*", [required('Please enter your '
                                                    'password')])
    submit = SubmitField('Login')


class SignUpForm(FlaskForm):
    """Sign Up Form"""

    username = StringField("Username*", [required('Please enter your '
                                                  'username')])
    email = EmailField("Email*", [
        required('Please enter your email'),
        Email(message='Please enter a valid email')
    ])
    password = PasswordField("Password*", [
        required('Please enter a password'),
        length(min=8, message='Password too short'),
        equal_to(fieldname='confirm_password', message='Password must match')
    ])
    confirm_password = PasswordField("Confirm Password*", [
        required('Please confirm your password')
    ])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """Check username does not already exist"""

        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username is taken.')

    def validate_email(self, email):
        """Check if email is not already being used"""

        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
