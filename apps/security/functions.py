# -*- coding: utf-8 -*-
__author__ = 'alex'
from apps.security.models import User
import base64


def encrypt_password(pw):
    new_pw = base64.b64encode(pw)
    return new_pw

def decode_password(pw):
    new_pw = base64.b64decode(pw)
    new_pw = str(new_pw).replace("\x00","")
    return new_pw


"""
Obtain 2 variables.
Returns True if user exist
Returns False if user does not exist
"""
def is_user(username):
    user = get_user(username)
    return user



def user_exist_elements():
    num_users = User.select().count()
    if num_users >= 1:
        return True
    else:
        return False


def create_user(first_name, last_name, username, password):
    try:
        new_password = encrypt_password(password)
        user = User(first_name=first_name,
                    last_name = last_name,
                    username = username,
                    password=new_password)
        user.save()
        return True
    except:
        return False


def get_user(username):
    try:
        user = User.get(username=username)
    except:
        user = None
    return user