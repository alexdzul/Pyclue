# -*- coding: utf-8 -*-
__author__ = 'alex'
from PyQt4 import QtGui
from PyQt4 import QtCore
from pyclue.ui.generics.functions import Center, alert
from pyclue.apps.keys.ui.resources_mapper import set_icon,get_icon_random_btn
from pyclue.apps.keys.models import Key
from pyclue.apps.keys.functions import save_key
from pyclue.apps.keys.ui.ui_sizes import get_add_key_size
import os


class AddKeyForm(QtGui.QWidget):

    def __init__(self, MainWindows):
        """
        user = Object User that is logged in
        MainWindows = Main Windows that display all the keys
        """
        super(AddKeyForm,self).__init__()
        self.Main = MainWindows
        self.constructorUI()

    def constructorUI(self):
        self.drawUI()
        self.setConnector()

    def drawUI(self):
        # Set some basic settings to the form
        self.setWindowTitle('New')
        get_add_key_size(self)
        Center(self)
        set_icon(self)
        # Start the Vertical Layout
        self.verticalLayout = QtGui.QVBoxLayout(self)
        #1. Set group Box Name and added into a grid element
        self.gbName = QtGui.QGroupBox(self)
        self.gbName.setObjectName("gbName")
        self.gbName.setTitle("Name")
        self.gridLayout_gbName = QtGui.QGridLayout(self.gbName)
        self.gridLayout_gbName.setObjectName("gridLayout_gbName")
        # Start the txtName Element into the gbName object
        self.txtName = QtGui.QLineEdit(self.gbName)
        self.txtName.setObjectName("Name")
        self.gridLayout_gbName.addWidget(self.txtName, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.gbName)
        #2. Set group Box Info and added into a grid element
        self.gbInfo = QtGui.QGroupBox(self)
        self.gbInfo.setObjectName("gbInfo")
        self.gbInfo.setTitle("Info")
        self.gridLayout_gbInfo = QtGui.QGridLayout(self.gbInfo)
        self.gridLayout_gbInfo.setObjectName("gridLayout_gbInfo")
        # Start the txtWebPage and its Label into a grid element
        self.txtWebpage = QtGui.QLineEdit(self.gbInfo)
        self.txtWebpage.setObjectName("txtWebpage")
        self.gridLayout_gbInfo.addWidget(self.txtWebpage, 0,1,1,2)
        self.lblWebpage = QtGui.QLabel(self.gbInfo)
        self.lblWebpage.setObjectName("lblWebpage")
        self.lblWebpage.setText("Web Page:")
        self.gridLayout_gbInfo.addWidget(self.lblWebpage, 0,0,1,1)
        # Start the txtEmail and its Label into a grid element
        self.txtEmail = QtGui.QLineEdit(self.gbInfo)
        self.txtEmail.setObjectName("txtEmail")
        self.gridLayout_gbInfo.addWidget(self.txtEmail, 1, 1, 1, 2)
        self.lblEmail = QtGui.QLabel(self.gbInfo)
        self.lblEmail.setObjectName("lblEmail")
        self.lblEmail.setText("Email:")
        self.gridLayout_gbInfo.addWidget(self.lblEmail, 1,0,1,1)
        # Start the txtUsername and its Label into a grid element
        self.txtUsername = QtGui.QLineEdit(self.gbInfo)
        self.txtUsername.setObjectName("txtUsername")
        self.gridLayout_gbInfo.addWidget(self.txtUsername, 4,1,1,2)
        self.verticalLayout.addWidget(self.gbInfo)
        self.lblUsername = QtGui.QLabel(self.gbInfo)
        self.lblUsername.setObjectName("Username")
        self.lblUsername.setText("Username:")
        self.gridLayout_gbInfo.addWidget(self.lblUsername, 4,0,1,1)
        # Start the txtPassword and its Label into a grid element
        self.txtPassword = QtGui.QLineEdit(self.gbInfo)
        self.txtPassword.setMinimumSize(QtCore.QSize(0, 0))
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Normal)
        self.txtPassword.setObjectName("txtPassword")
        self.gridLayout_gbInfo.addWidget(self.txtPassword, 5, 1, 1, 1)
        self.lblPassword = QtGui.QLabel(self.gbInfo)
        self.lblPassword.setObjectName("lblPassword")
        self.lblPassword.setText("Password:")
        self.gridLayout_gbInfo.addWidget(self.lblPassword, 5,0,1,1)
        #Start the generate password button
        self.btnRandom = QtGui.QPushButton(self.gbInfo)
        self.btnRandom.setObjectName("btnRandom")
        self.btnRandom.setText("Random")
        self.btnRandom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon(get_icon_random_btn(self))
        self.btnRandom.setIcon(icon)
        self.gridLayout_gbInfo.addWidget(self.btnRandom, 5, 2, 1, 1)
        #3. Set group Box Notes and added into a grid element
        self.gbNotes = QtGui.QGroupBox(self)
        self.gbNotes.setObjectName("gbNotes")
        self.gbNotes.setTitle("Notes")
        self.gridLayout_gbNotes = QtGui.QGridLayout(self.gbNotes)
        self.gridLayout_gbNotes.setObjectName("gridLayout_gbNotes")
        #Start the txtNotes and added into a grid element
        self.txtNotes = QtGui.QTextEdit(self.gbNotes)
        self.txtNotes.setObjectName("txtNotes")
        self.gridLayout_gbNotes.addWidget(self.txtNotes, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.gbNotes)
        #3. Draw 2 buttons, the main action on this form
        self.btnSave = QtGui.QPushButton(self)
        self.btnSave.setObjectName("btnSave")
        self.btnSave.setText("Save")
        self.btnSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLayout.addWidget(self.btnSave)
        self.btnCancel = QtGui.QPushButton(self)
        self.btnCancel.setObjectName("btnCancel")
        self.btnCancel.setText("Cancel")
        self.btnCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLayout.addWidget(self.btnCancel)


    def run(self):
        self.show()

    def set_generate_pass(self):
        self.txtPassword.setText("")
        keys = Key()
        self.txtPassword.setText(keys.generate_password())

    def setConnector(self):
        self.btnCancel.clicked.connect(self.close)
        self.btnRandom.clicked.connect(self.set_generate_pass)
        self.btnSave.clicked.connect(self.save)

    def save(self):
        key = Key()
        key.name = self.txtName.text()
        key.username = self.txtUsername.text()
        key.email = self.txtEmail.text()
        key.password = self.txtPassword.text()
        key.webpage = self.txtWebpage.text()
        key.notes = self.txtNotes.toPlainText()
        success = save_key(key)
        if not success:
            alert(self, "Error","Error al escribir los datos")
            self.txtName.setFocus()
        else:
            #Clear all the elements and then, refresh the list.
            self.Main.clear_list_elements()
            self.Main.set_list_elements()
            # Close the windows.
            self.close()
