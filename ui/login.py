# -*- coding: utf-8 -*-
__author__ = 'alex'
from PyQt4 import QtGui
from PyQt4 import QtCore
from ui.main import MainForm
from generics.functions import Center, SetIcon
from apps.security.functions import is_user, decode_password


class LoginForm(QtGui.QWidget):

    def __init__(self):
        super(LoginForm,self).__init__()
        self.constructorUI()

    def constructorUI(self):
        self.drawUI()
        Center(self)
        self.setConnectors()
        self.setFocusOrder()

    def run(self):
        self.show()

    def exit(self):
        QtCore.QCoreApplication.instance().quit()


    def validateCredential(self):
        my_username = self.txtUser.text()
        my_password = self.txtPassword.text()
        my_user = is_user(my_username)
        if my_user:
            if decode_password(my_user.password) == my_password:
                self.createMain(my_user)
            else:
                self.alert("Error","Incorrect password for <b>%s</b>" % my_user.username)
                self.txtUser.setFocus()
        else:
            self.alert("Error","User does not exist")
            self.txtUser.setFocus()


    def createMain(self,my_user):
        loginForm = self
        self.main = MainForm(my_user, loginForm)
        self.txtPassword.setText("")
        self.txtUser.setText("")
        self.txtUser.setFocus()
        self.hide()
        self.main.run()

    def alert(self, title,  mensaje):
        QtGui.QMessageBox.about(self, title, mensaje)

    def setConnectors(self):
        self.btnExit.clicked.connect(self.exit)
        self.btnLogin.clicked.connect(self.validateCredential)
        self.txtPassword.returnPressed.connect(self.btnLogin.click)
        self.txtUser.returnPressed.connect(self.btnLogin.click)

    def setFocusOrder(self):
        self.setTabOrder(self.txtUser, self.txtPassword)
        self.setTabOrder(self.txtPassword, self.btnLogin)
        self.setTabOrder(self.btnLogin, self.btnExit)

    def drawUI(self):
        # Set some basic settings to the form
        self.setWindowTitle('Login')
        self.setMinimumSize(200,120)
        self.setGeometry(500,200,150,150)
        SetIcon(self)
        # Create the main elements
        lblUser = QtGui.QLabel('Username:')
        lblPassword = QtGui.QLabel('Password:')
        self.txtUser = QtGui.QLineEdit(self)
        self.txtPassword = QtGui.QLineEdit()
        self.txtPassword.setEchoMode(2)
        self.btnLogin = QtGui.QPushButton('Login', self)
        self.btnLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnExit = QtGui.QPushButton('Exit', self)
        self.btnExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Configure the elements in the grid
        grid = QtGui.QGridLayout()
        grid.addWidget(lblUser,0,0,1,1)
        grid.addWidget(self.txtUser,0,1,1,1)
        grid.addWidget(lblPassword,1,0,1,1)
        grid.addWidget(self.txtPassword,1,1,1,1)
        grid.addWidget(self.btnLogin,2,0,1,1)
        grid.addWidget(self.btnExit,2,1,1,1)
        self.setLayout(grid)