# -*- coding: utf-8 -*-
__author__ = 'alex'
import os
from pyclue.appSettings import RESOURCES_DIR, OS_RUNING, PROJECT_DIR


def get_save_icon():
    img = "save.png"
    if OS_RUNING == "darwin":
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'img/%s'%img))
    else:
        path =  os.path.abspath(os.path.join("%s/%s"%(PROJECT_DIR,RESOURCES_DIR),'img/%s'%img))
    print path
    return path


def get_exit_icon():
    img = "quit.png"
    if OS_RUNING == "darwin":
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    else:
        path =  os.path.abspath(os.path.join("%s/%s"%(PROJECT_DIR,RESOURCES_DIR),'main/%s'%img))
    return path


def get_add_user_icon():
    img = "addUser.png"
    if OS_RUNING == "darwin":
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    else:
        path =  os.path.abspath(os.path.join("%s/%s"%(PROJECT_DIR,RESOURCES_DIR),'main/%s'%img))
    return path


def get_locked_icon():
    img = "lock.png"
    if OS_RUNING == "darwin":
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    else:
        path =  os.path.abspath(os.path.join("%s/%s"%(PROJECT_DIR,RESOURCES_DIR),'main/%s'%img))
    print "the lock path is:"
    print path
    return path


def get_delete_icon():
    img = "delete.png"
    if OS_RUNING == "darwin":
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    else:
        path =  os.path.abspath(os.path.join("%s/%s"%(PROJECT_DIR,RESOURCES_DIR),'main/%s'%img))
    return path


def get_view_pass_icon():
    img = "view_pass.png"
    if OS_RUNING == "darwin":
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    else:
        path =  os.path.abspath(os.path.join("%s/%s"%(PROJECT_DIR,RESOURCES_DIR),'main/%s'%img))
    return path


def get_update_icon():
    img = "update.png"
    if OS_RUNING == "darwin":
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    else:
        path =  os.path.abspath(os.path.join("%s/%s"%(PROJECT_DIR,RESOURCES_DIR),'main/%s'%img))
    return path


def get_add_icon():
    img = "key_add.png"
    if OS_RUNING == "darwin":
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    else:
        path =  os.path.abspath(os.path.join("%s/%s"%(PROJECT_DIR,RESOURCES_DIR),'main/%s'%img))
    return path


def get_settings_icon():
    img = "settings.png"
    if OS_RUNING == "darwin": 
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    else:
        path =  os.path.abspath(os.path.join("%s/%s"%(PROJECT_DIR,RESOURCES_DIR),'main/%s'%img))
    return path