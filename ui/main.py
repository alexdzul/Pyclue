# -*- coding: utf-8 -*-
__author__ = 'alex'
import os
from PyQt4 import QtGui
from PyQt4 import QtCore
from generics.functions import Center, SetIcon
from settings import RESOURCES_DIR
from ui.keys import AddKeyForm
from apps.keys.functions import get_user_keys

class MainForm(QtGui.QMainWindow):
    def __init__(self,user):
        """
        Build the Form with the User information
        """
        self.user = user
        super(MainForm, self).__init__()
        self.constructorUI()


    def constructorUI(self):
        self.drawUI()
        message = "Welcome: %s %s"%(self.user.first_name,self.user.last_name)
        self.set_statusBar(message)
        self.set_list_elements()
        Center(self)


    def drawUI(self):
        # Nombre de la ventana
        self.setWindowTitle('Keys Python')
        self.resize(700, 511)
        self.setMinimumSize(QtCore.QSize(569, 511))
        self.setMaximumSize(QtCore.QSize(700, 700))
        # Status Bar
        message = "Welcome: %s %s" % (self.user.first_name,self.user.last_name)
        self.statusBar().showMessage(message)
        # Windows Size
        self.setMinimumSize(700,700)
        self.setGeometry(300,300,450,400)
        self.centralwidget = QtGui.QWidget(self)
        SetIcon(self)
        # Set the grid to show de keys list
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listKeys = QtGui.QListWidget(self.centralwidget)
        self.listKeys.setObjectName("listKeys")
        self.gridLayout_2.addWidget(self.listKeys, 0, 0, 1, 1)
        # Set the group box info and added into a grid element
        self.gbInformation = QtGui.QGroupBox(self.centralwidget)
        self.gbInformation.setObjectName("gbInformation")
        self.gbInformation.setTitle("Information")
        self.gridLayout = QtGui.QGridLayout(self.gbInformation)
        self.gridLayout.setObjectName("gridLayout")
        # Set a Horizontal Layout in order to set txt and View password together
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txtUsername = QtGui.QLineEdit(self.gbInformation)
        self.txtUsername.setMinimumSize(QtCore.QSize(0, 0))
        # Set the txtUsername and its Label into a grid element
        self.txtUsername.setObjectName("txtUsername")
        self.gridLayout.addWidget(self.txtUsername, 1, 0, 1, 1)
        self.lblUsername = QtGui.QLabel(self.gbInformation)
        self.lblUsername.setObjectName("lblUsername")
        self.lblUsername.setText("Username:")
        self.gridLayout.addWidget(self.lblUsername, 0, 0, 1, 1)
        # Set the txtEmail and its Label into a grid Element
        self.txtEmail = QtGui.QLineEdit(self.gbInformation)
        self.txtEmail.setObjectName("txtEmail")
        self.gridLayout.addWidget(self.txtEmail, 3, 0, 1, 1)
        self.lblEmail = QtGui.QLabel(self.gbInformation)
        self.lblEmail.setObjectName("lblEmail")
        self.lblEmail.setText("Email:")
        self.gridLayout.addWidget(self.lblEmail, 2, 0, 1, 1)
        # Set the txtWebPage and its Label into a grid Element
        self.txtWebPage = QtGui.QLineEdit(self.gbInformation)
        self.txtWebPage.setObjectName("txtWebPage")
        self.gridLayout.addWidget(self.txtWebPage, 5, 0, 1, 1)
        self.lblWebPage = QtGui.QLabel(self.gbInformation)
        self.lblWebPage.setObjectName("lblWebPage")
        self.lblWebPage.setText("WebPage:")
        self.gridLayout.addWidget(self.lblWebPage, 4, 0, 1, 1)
        # Set the txtPassword and its Label into a grid Element
        self.txtPassword = QtGui.QLineEdit(self.gbInformation)
        self.txtPassword.setObjectName("txtPassword")
        self.horizontalLayout_2.addWidget(self.txtPassword)
        self.lblPassword = QtGui.QLabel(self.gbInformation)
        self.lblPassword.setObjectName("lblPassword")
        self.lblPassword.setText("Password:")
        self.gridLayout.addWidget(self.lblPassword, 6, 0, 1, 1)
        # Set the Button View Password and added into a grid element
        self.btnViewPassword = QtGui.QPushButton(self.gbInformation)
        self.btnViewPassword.setObjectName("btnViewPassword")
        self.btnViewPassword.setText("View Pass")
        self.horizontalLayout_2.addWidget(self.btnViewPassword)
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)
        # Set the txtNotes and its Label into a grid element
        self.txtNotes = QtGui.QTextEdit(self.gbInformation)
        self.txtNotes.setObjectName("txtNotes")
        self.gridLayout.addWidget(self.txtNotes, 9, 0, 1, 1)
        self.lblNotes = QtGui.QLabel(self.gbInformation)
        self.lblNotes.setObjectName("lblNotes")
        self.lblNotes.setText("Notes:")
        self.gridLayout.addWidget(self.lblNotes, 8, 0, 1, 1)
        # Set another Group Box to show btn Delete and Save
        self.groupBox = QtGui.QGroupBox(self.gbInformation)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle("Actions")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnDelete = QtGui.QPushButton(self.groupBox)
        self.btnDelete.setObjectName("btnDelete")
        icon = QtGui.QIcon(self.get_delete_icon())
        self.btnDelete.setIcon(icon)
        self.btnDelete.setText("Delete")
        self.horizontalLayout.addWidget(self.btnDelete)
        self.btnSave = QtGui.QPushButton(self.groupBox)
        self.btnSave.setObjectName("btnSave")
        icon = QtGui.QIcon(self.get_update_icon())
        self.btnSave.setIcon(icon)
        self.btnSave.setText("Save")
        self.horizontalLayout.addWidget(self.btnSave)
        self.gridLayout.addWidget(self.groupBox, 10, 0, 1, 1)
        self.gridLayout_2.addWidget(self.gbInformation, 0, 1, 1, 1)
        self.setCentralWidget(self.centralwidget)
        #===================== START ToolBar =========================================
        # Add the Lock Button
        lockAction = QtGui.QAction(QtGui.QIcon(self.get_locked_icon()),'Locked',self)
        lockAction.setShortcut('Ctrl+L')
        # Add the Exit Button
        exitAction = QtGui.QAction(QtGui.QIcon(self.get_exit_icon()),'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)
        # Add the Add Button
        addKeyAction = QtGui.QAction(QtGui.QIcon(self.get_add_icon()),'Add Key',self)
        addKeyAction.setShortcut('Ctrl+A')
        # Add the Settings Button
        settingsAction = QtGui.QAction(QtGui.QIcon(self.get_settings_icon()),'Settings',self)
        settingsAction.setShortcut('Ctrl+S')
        # Create toolBar Element
        self.toolBar = self.addToolBar('Main')
        # Add the elements to the toolBar
        self.toolBar.addAction(addKeyAction)
        self.toolBar.addAction(settingsAction)
        self.toolBar.addAction(lockAction)
        self.toolBar.addAction(exitAction)
        # Add  Signals to the toolBar elements
        self.connect(addKeyAction,QtCore.SIGNAL("triggered()"),self.show_add_key_form)
        #====================== END ToolBar =============================================


    def run(self):
        self.show()

    def show_add_key_form(self):
        self.createAddForm()

    def get_exit_icon(self):
        img = "quit.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/img/%s'%img))
        return path

    def get_locked_icon(self):
        img = "lock.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/img/%s'%img))
        return path

    def get_delete_icon(self):
        img = "delete.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/img/%s'%img))
        return path

    def get_update_icon(self):
        img = "update.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/img/%s'%img))
        return path

    def get_add_icon(self):
        img = "key_add.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/img/%s'%img))
        return path

    def get_settings_icon(self):
        img = "settings.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/img/%s'%img))
        return path

    def set_list_elements(self):
        keys = get_user_keys(self.user)
        i = 0
        for key in keys:
            item = QtGui.QListWidgetItem()
            item.setText(key.name)
            self.listKeys.addItem(item)
            item = self.listKeys.item(i)
            i = i + 1

    def clear_list_elements(self):
        self.listKeys.clear()

    def createAddForm(self):
        self.addKey = AddKeyForm(self.user,self)
        self.addKey.show()

    def set_statusBar(self,message):
        self.statusBar().showMessage(message)