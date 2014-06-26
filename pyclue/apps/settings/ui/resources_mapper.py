__author__ = 'alex'
import os
from pyclue.appSettings import RESOURCES_DIR, PROJECT_DIR, OS_RUNING



def get_save_info_icon():
    img = "Save.png"    
    if OS_RUNING == "darwin":
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'settings/%s'%img))
    else:
        path =  os.path.abspath(os.path.join("%s/%s"%(PROJECT_DIR,RESOURCES_DIR),'settings/%s'%img))
    return path

def get_folder_icon():
    img = "folder.png"
    if OS_RUNING == "darwin":
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'settings/%s'%img))
    else:
        path =  os.path.abspath(os.path.join("%s/%s"%(PROJECT_DIR,RESOURCES_DIR),'settings/%s'%img))
    return path


def get_exit_icon():
    img = "cancel.png"
    if OS_RUNING == "darwin":
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'img/%s'%img))
    else:
        path =  os.path.abspath(os.path.join("%s/%s"%(PROJECT_DIR,RESOURCES_DIR),'img/%s'%img))
    return path