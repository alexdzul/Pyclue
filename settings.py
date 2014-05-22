# -*- coding: utf-8 -*-
__author__ = 'alex'
from peewee import SqliteDatabase
import os

PROJECT_DIR = os.path.dirname(__file__)
RESOURCES_DIR = os.path.join(PROJECT_DIR,'resources')
APP_ICON = os.path.join(RESOURCES_DIR,'img/key.ico')
DB_NAME = 'pyclue.db'



WELCOME_MESSAGE = "Before starting using this application, " \
                  "it is necessary that you enter some basic " \
                  "information"
