__author__ = 'alex'
from pyclue.appSettings import RESOURCES_DIR
from PyQt4 import QtGui
import os

def set_icon(self):
    img = 'key_add.png'
    APP_ICON = os.path.join(RESOURCES_DIR,"keys/%s"%img)
    self.setWindowIcon(QtGui.QIcon(APP_ICON))

def get_icon_random_btn(self):
    img = 'random.png'
    btnIcon = os.path.join(RESOURCES_DIR,"keys/%s"%img)
    return btnIcon