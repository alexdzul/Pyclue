# -*- coding: utf-8 -*-
__author__ = 'alex'
from PyQt4 import QtGui
from PyQt4 import QtCore
from generics.functions import Center, SetIcon
from apps.security.functions import create_user
import os
from settings import RESOURCES_DIR


class AddUserForm(QtGui.QWidget):

    def __init__(self):
        super(AddUserForm,self).__init__()
        self.constructorUI()

    def constructorUI(self):
        self.drawUI()
        self.setConnectors()
        SetIcon(self)
        Center(self)

    def drawUI(self):
        self.setObjectName("AddUserForm")
        self.setWindowTitle("New User")
        self.resize(268, 244)
        self.setMinimumSize(QtCore.QSize(268, 244))
        self.setMaximumSize(QtCore.QSize(504, 297))
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.gbBasicInfo = QtGui.QGroupBox(self)
        self.gbBasicInfo.setObjectName("gbBasicInfo")
        self.gridLayout_3 = QtGui.QGridLayout(self.gbBasicInfo)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblFirstName = QtGui.QLabel(self.gbBasicInfo)
        self.lblFirstName.setObjectName("lblFirstName")
        self.lblFirstName.setText("First Name:")
        self.gridLayout_3.addWidget(self.lblFirstName, 0, 0, 1, 1)
        self.txtFirstName = QtGui.QLineEdit(self.gbBasicInfo)
        self.txtFirstName.setObjectName("txtFirstName")
        self.gridLayout_3.addWidget(self.txtFirstName, 0, 1, 1, 1)
        self.lblLastName = QtGui.QLabel(self.gbBasicInfo)
        self.lblLastName.setObjectName("lblLastName")
        self.lblLastName.setText("Last Name:")
        self.gridLayout_3.addWidget(self.lblLastName, 1, 0, 1, 1)
        self.txtLastName = QtGui.QLineEdit(self.gbBasicInfo)
        self.txtLastName.setObjectName("txtLastName")
        self.gridLayout_3.addWidget(self.txtLastName, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.gbBasicInfo, 0, 0, 1, 1)
        self.gbLoginData = QtGui.QGroupBox(self)
        self.gbLoginData.setObjectName("gbLoginData")
        self.gridLayout_2 = QtGui.QGridLayout(self.gbLoginData)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblUsername = QtGui.QLabel(self.gbLoginData)
        self.lblUsername.setObjectName("lblUsername")
        self.lblUsername.setText("Username:")
        self.gridLayout_2.addWidget(self.lblUsername, 0, 0, 1, 1)
        self.txtUsername = QtGui.QLineEdit(self.gbLoginData)
        self.txtUsername.setObjectName("txtUsername")
        self.gridLayout_2.addWidget(self.txtUsername, 0, 1, 1, 1)
        self.lblPassword = QtGui.QLabel(self.gbLoginData)
        self.lblPassword.setObjectName("lblPassword")
        self.lblPassword.setText("Password:")
        self.gridLayout_2.addWidget(self.lblPassword, 1, 0, 1, 1)
        self.txtPassword = QtGui.QLineEdit(self.gbLoginData)
        self.txtPassword.setObjectName("txtPassword")
        self.gridLayout_2.addWidget(self.txtPassword, 1, 1, 1, 1)
        self.txtConfirmPassword = QtGui.QLineEdit(self.gbLoginData)
        self.txtConfirmPassword.setObjectName("txtConfirmPassword")
        self.gridLayout_2.addWidget(self.txtConfirmPassword, 2, 1, 1, 1)
        self.lblConfirmPassword = QtGui.QLabel(self.gbLoginData)
        self.lblConfirmPassword.setObjectName("lblConfirmPassword")
        self.lblConfirmPassword.setText("Confirm Password:")
        self.gridLayout_2.addWidget(self.lblConfirmPassword, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.gbLoginData, 1, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.btnSave = QtGui.QPushButton(self.splitter)
        self.btnSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap((self.get_save_icon())), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSave.setIcon(icon)
        self.btnSave.setText("Save")
        self.btnSave.setIconSize(QtCore.QSize(40, 40))
        self.btnSave.setAutoRepeat(False)
        self.btnSave.setAutoExclusive(False)
        self.btnSave.setAutoDefault(False)
        self.btnSave.setDefault(True)
        self.btnSave.setFlat(False)
        self.btnSave.setObjectName("btnSave")
        self.btnCancel = QtGui.QPushButton(self.splitter)
        self.btnCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap((self.get_cancel_icon())), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon1)
        self.btnCancel.setText("Cancel")
        self.btnCancel.setIconSize(QtCore.QSize(20, 20))
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 1)

    def run(self):
        self.show()

    def exit(self):
        QtCore.QCoreApplication.instance().quit()


    def get_save_icon(self):
        img = "Save.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'img/%s'%img))
        return path

    def get_cancel_icon(self):
        img = "cancel.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'img/%s'%img))
        return path

    def alert(self, title,  mensaje):
        QtGui.QMessageBox.about(self, title, mensaje)

    def construct_get_data(self):
        self.first_name = self.txtFirstName.text()
        self.last_name = self.txtLastName.text()
        self.password_one = self.txtPassword.text()
        self.password_two = self.txtConfirmPassword.text()
        self.username = self.txtUsername.text()

    def save_user(self):
        self.construct_get_data()
        if self.password_one == self.password_two :
            user = create_user(self.first_name,
                        self.last_name,
                        self.username,
                        self.password_one)
            if user:

                self.alert("Great!","User save correctly!")
                self.close()
            else:
                self.alert("Error!","Something was wrong! Try again.")
        else:
            self.alert("Error","Password doesn't match")
            self.txtUsername.setFocus()

    def setConnectors(self):
        QtCore.QObject.connect(self.btnCancel, QtCore.SIGNAL("clicked()"), self.close)
        self.btnSave.clicked.connect(self.save_user)