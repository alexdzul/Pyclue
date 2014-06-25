__author__ = 'alex'
from peewee import *
import string, random
from pyclue.appSettings import get_data_path

"""
Key Object.
"""
class Key(Model):
    name = CharField()
    username = CharField()
    email = CharField()
    webpage = CharField()
    password = CharField()
    notes = TextField()

    class Meta:
        database = SqliteDatabase(get_data_path())

    def generate_password(self,size=8):
        chars = string.ascii_letters + str(random.random())
        password = ''.join(random.choice(chars) for _ in range(size))
        return password

