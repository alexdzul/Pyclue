__author__ = 'alex'
from peewee import *
from apps.security.models import User
import string, random
from settings import DB_NAME
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
