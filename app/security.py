#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'alex'
from app.models import User

def user_exist():
    num_users = User.select().count()
    if num_users > 1:
        return True
    else:
        return False