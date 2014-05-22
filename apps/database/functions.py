# -*- coding: utf-8 -*-
__author__ = 'alex'
import os, sys, traceback
from settings import DB_NAME, PROJECT_DIR
from apps.database.models import database

def get_db_path():
    try:
        path = os.path.join(PROJECT_DIR,DB_NAME)
        path = os.path.normpath(path)
        return path
    except:
        message = "Error" + str(sys.exc_info()[0]) + " " +\
                      str(sys.exc_info()[1]) + " " + \
                      str(sys.exc_info()[2])
        print message
        return None

def create_db():
    try:
        path = get_db_path()
        db = database()
        db.syncdb()
    except:
        pass