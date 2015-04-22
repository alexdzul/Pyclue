# -*- coding: utf-8 -*-
__author__ = 'alex'
import base64


def encrypt_password(pw):
    new_pw = base64.b64encode(pw.encode('ascii'))
    print(new_pw)
    return new_pw


def decode_password(pw):
    new_pw = base64.b64decode(pw).decode('ascii')
    new_pw = str(new_pw).replace("\x00", "")
    return new_pw