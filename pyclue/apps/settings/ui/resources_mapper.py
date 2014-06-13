__author__ = 'alex'
import os
from pyclue.appSettings import RESOURCES_DIR



def get_save_info_icon():
        img = "Save.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'settings/%s'%img))
        return path

def get_folder_icon():
        img = "folder.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'settings/%s'%img))
        return path


def get_exit_icon():
        img = "cancel.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'img/%s'%img))
        return path