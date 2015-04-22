__author__ = 'alex'
from pyclue.appSettings import RESOURCES_DIR, PROJECT_DIR, OS_RUNING
from PyQt5 import QtGui
import os

def set_icon(self):
    img = 'key_add.png'
    APP_ICON = os.path.join(RESOURCES_DIR,"keys/%s"%img)
    self.setWindowIcon(QtGui.QIcon(APP_ICON))

def get_icon_random_btn(self):
    img = 'random.png'
    if OS_RUNING == "darwin":
        btnIcon = os.path.join(RESOURCES_DIR,"keys/%s"%img)
    else:
        btnIcon = os.path.join("%s/%s"%(PROJECT_DIR,RESOURCES_DIR),"keys/%s"%img)
    return btnIcon