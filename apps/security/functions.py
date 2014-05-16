# -*- coding: utf-8 -*-
__author__ = 'alex'
import base64

def encrypt_password(pw):
    new_pw = base64.b64encode(pw)
    return new_pw