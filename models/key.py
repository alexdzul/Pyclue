# -*- coding: utf-8 -*-
__author__ = 'alex'
import string, random

class Key():
    def __init__(self):
        self.name = ""
        self.username = ""
        self.email = ""
        self.password = ""
        self.notes = ""

    def generate_password(self,size=8):
        chars = string.ascii_letters + str(random.random())
        password = ''.join(random.choice(chars) for _ in range(size))
        return password
