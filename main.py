#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from ui.login import LoginForm
from ui.launch import LaunchForm
from apps.security.controller import user_exist

def main():
    app = QtGui.QApplication(sys.argv)
    if user_exist():
        login = LoginForm()
        login.run()
    else:
        launch = LaunchForm()
        launch.run()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()