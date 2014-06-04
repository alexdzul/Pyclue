__author__ = 'alex'
from PyQt4 import QtGui
from pyclue.appSettings import APP_ICON

def Center(uiForm):
        qr = uiForm.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        uiForm.move(qr.topLeft())

def SetIcon(uiForm):
        uiForm.setWindowIcon(QtGui.QIcon(APP_ICON))

def alert(uiForm, title, message):
    QtGui.QMessageBox.about(uiForm, title, message)