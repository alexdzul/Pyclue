#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from pyclue.appSettings import create_data_path, create_default_backups_path
from pyclue.apps.security.ui.forms import LoginForm
from pyclue.apps.main.ui.forms import LaunchForm
from pyclue.apps.database.functions import create_db, generate_backup
from pyclue.apps.settings.functions import settings_exist

def main():
    app = QtGui.QApplication(sys.argv)
    create_data_path()
    create_default_backups_path()
    create_db() # Create the database if necessary
    generate_backup() # Generate backup if necessary
    if settings_exist():
        login = LoginForm()
        login.run()
    else:
        launch = LaunchForm()
        launch.run()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()