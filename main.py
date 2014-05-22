#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from ui.login import LoginForm
from ui.launch import LaunchForm
from apps.security.functions import user_exist_elements
from apps.database.functions import create_db

def main():
    app = QtGui.QApplication(sys.argv)
    create_db() # Create the database if necesary
    if user_exist_elements():
        login = LoginForm()
        login.run()
    else:
        launch = LaunchForm()
        launch.run()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()