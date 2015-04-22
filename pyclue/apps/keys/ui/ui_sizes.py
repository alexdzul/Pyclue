__author__ = 'alex'
from PyQt5 import QtCore
from pyclue.appSettings import OS_RUNING



def get_add_key_size(self):
    if OS_RUNING == "linux2":
        self.resize(450, 480)
        self.setMinimumSize(QtCore.QSize(450, 480))
        self.setMaximumSize(QtCore.QSize(450, 480))
    if OS_RUNING == "darwin":
        self.resize(450, 480)
        self.setMinimumSize(QtCore.QSize(450, 480))
        self.setMaximumSize(QtCore.QSize(450, 480))
    else:
        self.resize(500, 439)
        self.setMinimumSize(QtCore.QSize(500, 480))
        self.setMaximumSize(QtCore.QSize(500, 480))