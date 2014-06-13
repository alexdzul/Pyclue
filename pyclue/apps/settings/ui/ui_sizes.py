# -*- coding: utf-8 -*-
__author__ = 'alex'
from PyQt4 import QtCore
from pyclue.appSettings import OS_RUNING



def get_size(self):
    if OS_RUNING == "linux2":
        self.resize(386, 400)
        self.setMinimumSize(QtCore.QSize(386, 400))
    if OS_RUNING == "darwin":
        self.resize(500, 500)
        self.setMinimumSize(QtCore.QSize(500, 500))
    else:
        self.resize(386, 363)
        self.setMinimumSize(QtCore.QSize(386, 363))