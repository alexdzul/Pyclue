# -*- coding: utf-8 -*-
__author__ = 'alex'
import os
from pyclue.apps.settings.models import MainSettings
from pyclue.apps.keys.models import Key


class database():

    def syncdb(self):
        try:
            Key.create_table()
            MainSettings.create_table()
        except:
            pass

    def exist(self, db_path):
        try:
            exist = os.path.isfile(db_path)
            if exist:
                return True
            else:
                return False
        except:
            return False
