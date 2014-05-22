# -*- coding: utf-8 -*-
__author__ = 'alex'
import sys
import traceback
import os
from apps.security.models import User
from apps.keys.models import Key


class database():

    def syncdb(self):
        try:
            Key.create_table()
            User.create_table()
        except:
            message = "Error" + str(sys.exc_info()[0]) + " " +\
                      str(sys.exc_info()[1]) + " " + \
                      str(sys.exc_info()[2]) + " " + \
                      traceback.format_exc()
            print message

    def exist(self, db_path):
        try:
            exist = os.path.isfile(db_path)
            if exist:
                print "existe"
                return True
            else:
                print "no existe"
                return False
        except:
            return False

