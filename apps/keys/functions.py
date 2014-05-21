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


def delete_key(key):
    try:
        key.delete_instance()
        return True
    except:
        return False


def update_key(key_obj, new_data_dict):
    try:
        key_obj.name =  new_data_dict['name']
        key_obj.username = new_data_dict['username']
        key_obj.email = new_data_dict['email']
        key_obj.password = encrypt_password(new_data_dict['password'])
        key_obj.notes = new_data_dict['notes']
        key_obj.webpage = new_data_dict['webpage']
        key_obj.save()
        return key_obj
    except:
        return None

"""
Returns keys objects.
If return_list is True, the functions
return a list element.
"""
def get_user_keys(user):
    keys = Key.select().where(Key.user==user)
    return keys
