__author__ = 'alex'
from peewee import *
from pyclue.appSettings import get_data_path


class MainSettings(Model):
    period_backup = CharField()
    deactivate_backup = BooleanField()
    num_files_store = IntegerField()
    file_name_backup = CharField()
    file_name_sufix_backup = CharField()
    user_fullName = CharField()
    user_password = CharField()
    version = CharField()

    class Meta:
        database = SqliteDatabase(get_data_path())