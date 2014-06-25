# -*- coding: utf-8 -*-
__author__ = 'alex'
import os, sys, traceback
from pyclue.apps.settings.models import MainSettings
from pyclue.apps.keys.models import Key


class database():

    def syncdb(self):
        try:
            Key.create_table()
            MainSettings.create_table()
        except:
            message = "Error" + str(sys.exc_info()[0]) + " " +\
                      str(sys.exc_info()[1]) + " " + \
                      str(sys.exc_info()[2])  + " " + traceback.format_exc()
            print message
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

