# -*- coding: utf-8 -*-
__author__ = 'alex'
from peewee import SqliteDatabase
import os

SOFTWARE_NAME = "Pyclue"
VERSION = "0.1"
AUTHOR = "Alex Dzul"
AUTHOR_EMAIL = "alexexc2@gmail.com"
LICENCE = "GPL v2"



PROJECT_DIR = os.path.dirname(__file__)
RESOURCES_DIR = os.path.join(PROJECT_DIR,'resources')
APP_ICON = os.path.join(RESOURCES_DIR,'img/key.ico')
DB_NAME = 'pyclue/pyclue.db'





WELCOME_MESSAGE = "Before starting using this application, " \
                  "it is necessary that you enter some basic " \
                  "information"

ABOUT_MESSAGE = "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">PyClue.</span>" \
                "</p><p>Is an Open Source password manager which simplifies the task of </p><p>grouping secret " \
                "information in one place. </p><p>This software is cross-platform because it is written in Python." \
                "</p><p><span style=\" font-size:12pt; font-weight:600;\">Author.</span></p><p>Alex Dzul. Twitter: " \
                "<a href=\"http://www.twitter.com/alexjs88\"><span style=\" text-decoration: underline; color:#0000ff;\">" \
                "@alexjs88</span></a></p><p><span style=\" font-size:12pt; font-weight:600;\">Licence.</span></p><p>" \
                "This software is under the GPL v2 terms.</p><p>Copyright (C) 2014, version."+ VERSION +"</p><p><span style=\" font-size:12pt; " \
                "font-weight:600;\">Github.</span></p><p>View the code on <a href=\"https://github.com/alexdzul/Pyclue\">" \
                "<span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/alexdzul/Pyclue</span></a>" \
                "<br/></p></body></html>"
