# -*- coding: utf-8 -*-
__author__ = 'alex'
from apps.security.functions import encrypt_password

def save_key(key):
    try:
        new_pw = encrypt_password(key.password)
        key.password = new_pw
        key.save()
        return True
    except:
        return False
