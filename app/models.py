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


"""
Key Object.
"""
class Key(Model):
    user = ForeignKeyField(User)
    name = CharField()
    username = CharField()
    email = CharField()
    password = CharField()
    notes = TextField()

    class Meta:
        database = DB_NAME

    def generate_password(self,size=8):
        chars = string.ascii_letters + str(random.random())
        password = ''.join(random.choice(chars) for _ in range(size))
        return password


