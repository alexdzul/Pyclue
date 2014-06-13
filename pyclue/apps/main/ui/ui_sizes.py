# -*- coding: utf-8 -*-
__author__ = 'alex'
from PyQt4 import QtCore
from pyclue.appSettings import OS_RUNING


def get_launch_size(self):
    if OS_RUNING == "linux2":
        self.resize(300, 316)
        self.setMinimumSize(QtCore.QSize(300, 316))
        self.setMaximumSize(QtCore.QSize(300, 316))
    if OS_RUNING == "darwin":
        self.resize(300, 360)
        self.setMinimumSize(QtCore.QSize(300, 360))
        self.setMaximumSize(QtCore.QSize(300, 360))
    else:
        self.resize(300, 316)
        self.setMinimumSize(QtCore.QSize(300, 316))
        self.setMaximumSize(QtCore.QSize(300, 316))


def get_main_size(self):
    if OS_RUNING == "linux2":
        self.resize(400, 472)
        self.setMinimumSize(QtCore.QSize(400, 472))
        self.setMaximumSize(QtCore.QSize(569, 511))
        self.resize(386, 400)
        self.setMinimumSize(QtCore.QSize(386, 400))
    if OS_RUNING == "darwin":
        self.resize(400, 512)
        self.setMinimumSize(QtCore.QSize(400, 500))
        self.setMaximumSize(QtCore.QSize(569, 512))
    else:
        self.resize(400, 472)
        self.setMinimumSize(QtCore.QSize(400, 472))
        self.setMaximumSize(QtCore.QSize(569, 511))