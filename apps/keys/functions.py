# -*- coding: utf-8 -*-
__author__ = 'alex'
from apps.security.functions import encrypt_password
from apps.keys.models import Key

def save_key(key):
    try:
        new_pw = encrypt_password(key.password)
        key.password = new_pw
        key.save()
        return True
    except:
        return False

"""
Returns keys objects.
If return_list is True, the functions
return a list element.
"""
def get_user_keys(user):
    keys = Key.select().where(Key.user==user)
    return keys
