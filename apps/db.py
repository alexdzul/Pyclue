# -*- coding: utf-8 -*-
__author__ = 'alex'
import sys
import traceback

from apps.security.models import Key, User


class Syncdb():
    try:
        Key.create_table()
        User.create_table()
    except:
        message = "Error" + str(sys.exc_info()[0]) + " " +\
                  str(sys.exc_info()[1]) + " " + \
                  str(sys.exc_info()[2]) + " " + \
                  traceback.format_exc()
        print message
