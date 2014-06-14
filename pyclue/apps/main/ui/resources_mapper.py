# -*- coding: utf-8 -*-
__author__ = 'alex'
import os
from pyclue.appSettings import RESOURCES_DIR


def get_save_icon():
    img = "save.png"
    path =  os.path.abspath(os.path.join(RESOURCES_DIR,'img/%s'%img))
    return path


def get_exit_icon():
    img = "quit.png"
    path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    return path


def get_add_user_icon():
    img = "addUser.png"
    path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    return path


def get_locked_icon():
    img = "lock.png"
    path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    #path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/img/%s'%img))
    return path


def get_delete_icon():
    img = "delete.png"
    path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    return path


def get_view_pass_icon():
    img = "view_pass.png"
    path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    return path


def get_update_icon():
    img = "update.png"
    path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    return path


def get_add_icon():
    img = "key_add.png"
    path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    return path


def get_settings_icon():
    img = "settings.png"
    path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/%s'%img))
    return path