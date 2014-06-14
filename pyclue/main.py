#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from pyclue.apps.security.ui import LoginForm
from pyclue.apps.main.ui.forms import LaunchForm
from pyclue.apps.database.functions import create_db
from pyclue.apps.settings.functions import settings_exist

def main():
    app = QtGui.QApplication(sys.argv)
    create_db() # Create the database if necesary
    if settings_exist():
        login = LoginForm()
        login.run()
    else:
        launch = LaunchForm()
        launch.run()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()