# -*- coding: utf-8 -*-
__author__ = 'alex'
import string
import random
from peewee import *
from settings import DB_NAME



"""
User object
"""
class User(Model):
    username = CharField()
    first_name = CharField()
    last_name = CharField()
    password = CharField()

    class Meta:
        database = DB_NAME





