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
    if OS_RUNING == "win32":
        self.resize(300, 316)
        self.setMinimumSize(QtCore.QSize(300, 316))
        self.setMaximumSize(QtCore.QSize(300, 316))


def get_main_size(self):
    if OS_RUNING == "linux2":
        self.resize(400, 472)
        self.setMinimumSize(QtCore.QSize(400, 472))
        self.setMaximumSize(QtCore.QSize(569, 511))
        self.resize(386, 400)
    if OS_RUNING == "darwin":
        self.resize(600, 550)
        self.setMinimumSize(QtCore.QSize(600, 550))
    if OS_RUNING == "win32":
        self.resize(600, 472)
        self.setMinimumSize(QtCore.QSize(600, 472))