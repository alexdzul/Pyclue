#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'alex'
from apps.security.models import User
from apps.security.functions import encrypt_password

def user_exist():
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
