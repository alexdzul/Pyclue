__author__ = 'alex'
from peewee import *
from pyclue.appSettings import DB_NAME

class MainSettings(Model):
    period_backup = CharField()
    deactivate_backup = BooleanField()
    path_store = CharField(null=True)
    num_files_store = IntegerField()
    file_name_backup = CharField()
    user_fullName = CharField()
    user_password = CharField()
    version = CharField()

    class Meta:
        database = SqliteDatabase(DB_NAME)