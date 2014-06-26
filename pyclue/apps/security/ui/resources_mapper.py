'''
Created on 26/06/2014

@author: edzul
'''
import os
from pyclue.appSettings import RESOURCES_DIR, OS_RUNING, PROJECT_DIR


def get_login_icon():
    img = "login.png"
    if OS_RUNING == "darwin":
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    else:
        path =  os.path.abspath(os.path.join("%s/%s"%(PROJECT_DIR,RESOURCES_DIR),'main/%s'%img))
    return path


def get_quit_icon():
    img = "quit.png"
    if OS_RUNING == "darwin":
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    else:
        path =  os.path.abspath(os.path.join("%s/%s"%(PROJECT_DIR,RESOURCES_DIR),'main/%s'%img))
    return path