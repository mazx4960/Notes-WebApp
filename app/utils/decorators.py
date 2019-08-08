"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

from functools import wraps
from flask import redirect, session


#############
# Functions #
#############

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        try:
            if not session['username']:
                return redirect('/login/')
            else:
                return f(*args, **kwargs)
        except KeyError:
            return redirect('/login/')
    return wrap
