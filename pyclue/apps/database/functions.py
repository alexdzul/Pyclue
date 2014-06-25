# -*- coding: utf-8 -*-
__author__ = 'alex'
import os, sys, traceback
from pyclue.appSettings import DB_NAME, PROJECT_DIR
from pyclue.apps.database.models import database

def get_db_path():
    try:
        path = os.path.join(PROJECT_DIR,DB_NAME)
        path = os.path.normpath(path)
        print path
        return path
    except:
        message = "Error" + str(sys.exc_info()[0]) + " " +\
                      str(sys.exc_info()[1]) + " " + \
                      str(sys.exc_info()[2])  + " " + traceback.format_exc()
        print message
        return None

def create_db():
    try:
        db = database()
        db.syncdb()
    except:
        pass