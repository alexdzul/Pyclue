'''
Created on 26/06/2014
@author: alex
'''
__author__ = 'alex'
from PyQt4 import QtCore
from pyclue.appSettings import OS_RUNING

def get_login_size(self):
    if OS_RUNING == "darwin":
        self.resize(391, 130)
        self.setMinimumSize(QtCore.QSize(391, 130))
        self.setMaximumSize(QtCore.QSize(391, 130))
    if OS_RUNING == "win32":
        self.resize(391, 130)
        self.setMinimumSize(QtCore.QSize(391, 130))
        self.setMaximumSize(QtCore.QSize(391, 130))