# -*- coding: utf-8 -*-
__author__ = 'alex'
import sys
import traceback

from pyclue.apps.settings.models import MainSettings
from pyclue.appSettings import VERSION
from pyclue.apps.security.functions import encrypt_password


def create_settings(user_full_name, user_password):
    try:
        print(user_password)
        main = MainSettings()
        main.user_fullName = user_full_name
        main.user_password = encrypt_password(user_password)
        # Default first settings
        main.period_backup = "Weekly"
        main.deactivate_backup = False
        main.num_files_store = 3
        main.file_name_backup = "keys"
        main.file_name_sufix_backup = ".DDMMYY.bak"
        main.version = VERSION
        main.save()
        return True
    except:
        message = "Error" + str(sys.exc_info()[0]) + " " +\
                      str(sys.exc_info()[1]) + " " + \
                      str(sys.exc_info()[2]) + " " + traceback.format_exc()
        print(message)
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
        settings = MainSettings.get()
        return settings
    except:
        return None


def save_settings(period_backup, deactivate_backup, num_files_store, file_name_backup, user_fullName, user_password=None):
    try:
        my_set = get_settings()
        if my_set:
            my_set.period_backup = period_backup
            my_set.deactivate_backup = deactivate_backup
            my_set.num_files_store = num_files_store
            my_set.file_name_backup = file_name_backup
            my_set.user_fullName = user_fullName
            if user_password:  # Si se envia un password
                my_set.user_password = encrypt_password(user_password)
            my_set.save()
            return True
        else:
            return False
    except:
        return False


def get_random_string(length=12,
                      allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    """
    Returns a securely generated random string.

    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits.

    Taken from the django.utils.crypto module.
    """
    import random
    random = random.SystemRandom()
    return ''.join(random.choice(allowed_chars) for i in range(length))


def get_secret_key():
    """
    Create a random secret key.

    Taken from the Django project.
    """
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return get_random_string(50, chars)