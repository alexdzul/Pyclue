# -*- coding: utf-8 -*-
__author__ = 'alex'
import base64, sys
from pyclue.apps.settings.models import MainSettings
from pyclue.appSettings import VERSION


def encrypt_password(pw):
    new_pw = base64.b64encode(pw)
    return new_pw


def decode_password(pw):
    new_pw = base64.b64decode(pw)
    new_pw = str(new_pw).replace("\x00","")
    return new_pw


def create_settings(user_fullName, user_password):
    print user_password
    print user_fullName
    try:
        main = MainSettings()
        main.user_fullName = user_fullName
        main.user_password = encrypt_password(user_password)
        #Default first settings
        main.period_backup = "Weekly"
        main.deactivate_backup = False
        main.num_files_store = 3
        main.file_name_backup = "keys_DD-MM-YY.bak"
        main.version = VERSION
        main.save()
        return True
    except:
        message = "Error" + str(sys.exc_info()[0]) + " " +\
                      str(sys.exc_info()[1]) + " " + \
                      str(sys.exc_info()[2])
        print message
        return False

def settings_exist():
    try:
        settings = MainSettings.select().count()
        if settings >= 1:
            return True
        else:
            return False
    except:
        return False

def get_settings():
    try:
        set = MainSettings.get()
        return set
    except:
        return None