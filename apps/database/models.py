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

