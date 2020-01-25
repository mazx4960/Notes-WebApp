"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

from datetime import datetime

###########
# Filters #
###########

def datetimeformat(value, format="%m %b %Y, %I:%M %p"):
    datetime_obj = datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
    return datetime_obj.strftime(format)
