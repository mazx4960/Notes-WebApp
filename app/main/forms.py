"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

from flask_wtf import FlaskForm
from flask_pagedown.fields import PageDownField
from wtforms.fields.html5 import EmailField
from wtforms import StringField, PasswordField, SubmitField, RadioField, SelectField
from wtforms.validators import required, equal_to, length, ValidationError
from wtforms.validators import Email

from app.models import User


################
# Form Classes #
################

class AddNoteForm(FlaskForm):
    """Add Note Form"""
    private_radio_style = {
        'style': 'list-style: none; margin: 0; padding: 0;'
    }

    title = StringField('Note Title:', [required("Please enter a note title.")])
    note = PageDownField('Your Note:', [required('Please enter notes contents.')])
    # tags = SelectMultipleField('Note Tags:')
    private = RadioField('Private:', choices=[('on', 'on'), ('off', 'off')], render_kw=private_radio_style)
    folder = SelectField('Folder:', choices=[('0', 'All')], default='0')
    submit = SubmitField('Add Note')


class SearchForm(FlaskForm):
    """Search notes and users form"""
    choices = [
        ('Users', 'Users'),
        ('Notes', 'Notes')
    ]

    search = StringField("Search Note/Users", [required("Unable to search empty string.")])
    category = SelectField('Category', choices=choices, default='Notes')
