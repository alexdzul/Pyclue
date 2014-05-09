#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from ui.login import LoginForm

def main():
    app = QtGui.QApplication(sys.argv)
    login = LoginForm()
    login.run()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()