__author__ = 'alex'
from PyQt5 import QtGui, QtWidgets
from pyclue.appSettings import APP_ICON

def Center(uiForm):
        qr = uiForm.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        uiForm.move(qr.topLeft())


def SetIcon(uiForm):
        uiForm.setWindowIcon(QtGui.QIcon(APP_ICON))


def alert(uiForm, title, message):
    QtWidgets.QMessageBox.about(uiForm, title, message)