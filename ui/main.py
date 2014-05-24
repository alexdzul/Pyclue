# -*- coding: utf-8 -*-
__author__ = 'alex'
import os
from PyQt4 import QtGui
from PyQt4 import QtCore
from generics.functions import Center, SetIcon
from settings import RESOURCES_DIR
from ui.keys import AddKeyForm
from ui.users import AddUserForm
from apps.keys.functions import get_user_keys, delete_key, update_key
from apps.security.functions import decode_password

class MainForm(QtGui.QMainWindow):
    def __init__(self,user, loginForm):
        """
        Build the Form with the User information
        """
        self.loginForm = loginForm
        self.user = user
        super(MainForm, self).__init__()
        self.constructorUI()


    def constructorUI(self):
        self.drawUI()
        message = "Welcome: %s %s"%(self.user.first_name,self.user.last_name)
        self.set_statusBar(message)
        self.set_list_elements()
        self.setConnectors()
        Center(self)


    def drawUI(self):
        # Nombre de la ventana
        self.setWindowTitle('Keys Python')
        # Windows Size
        self.resize(400, 472)
        self.setMinimumSize(QtCore.QSize(400, 472))
        self.setMaximumSize(QtCore.QSize(569, 511))
        # Status Bar
        message = "Welcome: %s %s" % (self.user.first_name,self.user.last_name)
        self.statusBar().showMessage(message)
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

        # Set the txtNameKey and its Label into a grid element
        self.lblNameKey = QtGui.QLabel(self.gbInformation)
        self.lblNameKey.setObjectName("lblNameKey")
        self.lblNameKey.setText("Name of the Key:")
        self.gridLayout.addWidget(self.lblNameKey, 0, 0, 1, 1)
        self.txtNameKey = QtGui.QLineEdit(self.gbInformation)
        self.txtNameKey.setObjectName("txtNameKey")
        self.gridLayout.addWidget(self.txtNameKey, 1, 0, 1, 1)
        # Set the txtUsername and its Label into a grid element
        self.lblUsername = QtGui.QLabel(self.gbInformation)
        self.lblUsername.setObjectName("lblUsername")
        self.lblUsername.setText("Username:")
        self.gridLayout.addWidget(self.lblUsername, 2, 0, 1, 1)
        self.txtUsername = QtGui.QLineEdit(self.gbInformation)
        self.txtUsername.setMinimumSize(QtCore.QSize(0, 0))
        self.txtUsername.setObjectName("txtUsername")
        self.gridLayout.addWidget(self.txtUsername, 3, 0, 1, 1)
        # Set the txtEmail and its Label into a grid Element
        self.lblEmail = QtGui.QLabel(self.gbInformation)
        self.lblEmail.setObjectName("lblEmail")
        self.lblEmail.setText("Email:")
        self.gridLayout.addWidget(self.lblEmail, 4, 0, 1, 1)
        self.txtEmail = QtGui.QLineEdit(self.gbInformation)
        self.txtEmail.setObjectName("txtEmail")
        self.gridLayout.addWidget(self.txtEmail, 5, 0, 1, 1)
        # Set the txtWebPage and its Label into a grid Element
        self.lblWebPage = QtGui.QLabel(self.gbInformation)
        self.lblWebPage.setObjectName("lblWebPage")
        self.lblWebPage.setText("WebPage:")
        self.gridLayout.addWidget(self.lblWebPage, 6, 0, 1, 1)
        self.txtWebPage = QtGui.QLineEdit(self.gbInformation)
        self.txtWebPage.setObjectName("txtWebPage")
        self.gridLayout.addWidget(self.txtWebPage, 7, 0, 1, 1)
        # Set a Horizontal Layout in order to set txt and View password together
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # Set the txtPassword and its Label into a grid Element
        self.lblPassword = QtGui.QLabel(self.gbInformation)
        self.lblPassword.setObjectName("lblPassword")
        self.lblPassword.setText("Password:")
        self.gridLayout.addWidget(self.lblPassword, 8, 0, 1, 1)
        self.txtPassword = QtGui.QLineEdit(self.gbInformation)
        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.horizontalLayout_2.addWidget(self.txtPassword)
        # Set the Button View Password and added into a grid element
        self.btnViewPassword = QtGui.QPushButton(self.gbInformation)
        self.btnViewPassword.setObjectName("btnViewPassword")
        self.btnViewPassword.setText("View Pass")
        icon = QtGui.QIcon(self.get_view_pass_icon())
        self.btnViewPassword.setIcon(icon)
        self.horizontalLayout_2.addWidget(self.btnViewPassword)
        self.gridLayout.addLayout(self.horizontalLayout_2, 9, 0, 1, 1)
        # Set the txtNotes and its Label into a grid element
        self.lblNotes = QtGui.QLabel(self.gbInformation)
        self.lblNotes.setObjectName("lblNotes")
        self.lblNotes.setText("Notes:")
        self.gridLayout.addWidget(self.lblNotes, 10, 0, 1, 1)
        self.txtNotes = QtGui.QTextEdit(self.gbInformation)
        self.txtNotes.setObjectName("txtNotes")
        self.gridLayout.addWidget(self.txtNotes, 11, 0, 1, 1)
        # Set another Group Box to show btn Delete and Save
        self.groupBox = QtGui.QGroupBox(self.gbInformation)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle("Actions")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # Add the Delete Button ===========================
        self.btnDelete = QtGui.QPushButton(self.groupBox)
        self.btnDelete.setObjectName("btnDelete")
        icon = QtGui.QIcon(self.get_delete_icon())
        self.btnDelete.setIcon(icon)
        self.btnDelete.setText("Delete")
        self.btnDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.btnDelete)
        #Add the Save Button ============================
        self.btnSave = QtGui.QPushButton(self.groupBox)
        self.btnSave.setObjectName("btnSave")
        icon = QtGui.QIcon(self.get_update_icon())
        self.btnSave.setIcon(icon)
        self.btnSave.setText("Save")
        self.btnSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.btnSave)
        self.gridLayout.addWidget(self.groupBox, 12, 0, 1, 1)
        self.gridLayout_2.addWidget(self.gbInformation, 0, 1, 1, 1)
        self.setCentralWidget(self.centralwidget)
        #===================== START ToolBar =========================================
        # Add the Lock Button
        self.lockAction = QtGui.QAction(QtGui.QIcon(self.get_locked_icon()),'Lock the Windows',self)
        self.lockAction.setShortcut('Ctrl+L')
        # Add the Exit Button
        self.exitAction = QtGui.QAction(QtGui.QIcon(self.get_exit_icon()),'Exit',self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.triggered.connect(QtGui.qApp.quit)
        # Add the Add Button
        self.addKeyAction = QtGui.QAction(QtGui.QIcon(self.get_add_icon()),'Add Key',self)
        self.addKeyAction.setShortcut('Ctrl+A')
        # Add the Settings Button
        self.settingsAction = QtGui.QAction(QtGui.QIcon(self.get_settings_icon()),'Settings',self)
        self.settingsAction.setShortcut('Ctrl+S')
        # Add the Add User Button
        self.addUserAction = QtGui.QAction(QtGui.QIcon(self.get_add_user_icon()),'Add User',self)
        self.addUserAction.setShortcut('Ctrl+U')
        # Create toolBar Element
        self.toolBar = self.addToolBar('Main')
        # Add the elements to the toolBar
        self.toolBar.addAction(self.addKeyAction)
        self.toolBar.addAction(self.addUserAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.settingsAction)
        self.toolBar.addAction(self.lockAction)
        self.toolBar.addAction(self.exitAction)
        #====================== END ToolBar =============================================


    def get_item_info(self):
        try:
            self.hide_password()
            item = self.listKeys.currentItem()
            item = item.data(QtCore.Qt.UserRole).toPyObject()
            self.txtNameKey.setText(item.name)
            self.txtUsername.setText(item.username)
            self.txtNotes.setText(item.notes)
            self.txtPassword.setText(decode_password(item.password))
            self.txtEmail.setText(item.email)
            self.txtWebPage.setText(item.webpage)
        except:
            pass

    def run(self):
        self.show()

    def show_add_key_form(self):
        self.createAddForm()

    def get_exit_icon(self):
        img = "quit.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/img/%s'%img))
        return path

    def get_add_user_icon(self):
        img = "addUser.png"
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

    def get_view_pass_icon(self):
        img = "view_pass.png"
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
        for key in keys:
            item = QtGui.QListWidgetItem()
            item.setText(key.name)
            item.setData(QtCore.Qt.UserRole,key)
            self.listKeys.addItem(item)

    def clear_list_elements(self):
        self.listKeys.clear()

    def createAddForm(self):
        self.addKey = AddKeyForm(self.user,self)
        self.addKey.show()

    def set_statusBar(self,message):
        self.statusBar().showMessage(message)

    def hide_this_and_show_login(self):
        self.close()
        self.loginForm.show()

    def update_key_list(self):
        self.clear_list_elements()
        self.set_list_elements()

    def show_add_user_form(self):
        self.addUser = AddUserForm()
        self.addUser.run()

    def setConnectors(self):
        self.listKeys.currentItemChanged.connect(self.get_item_info)
        self.btnViewPassword.pressed.connect(self.show_hide_password)
        self.btnDelete.pressed.connect(self.delete_element)
        self.btnSave.pressed.connect(self.update_element)
        # Add  Signals to the toolBar elements
        self.connect(self.addKeyAction, QtCore.SIGNAL("triggered()"),self.show_add_key_form)
        self.connect(self.lockAction, QtCore.SIGNAL("triggered()"),self.hide_this_and_show_login)
        self.connect(self.addUserAction, QtCore.SIGNAL("triggered()"),self.show_add_user_form)

    def clean_textbox_info(self):
        try:
            self.txtNameKey.setText("")
            self.txtPassword.setText("")
            self.txtEmail.setText("")
            self.txtNotes.setText("")
            self.txtUsername.setText("")
            self.txtWebPage.setText("")
        except:
            pass

    def hide_password(self):
        self.btnViewPassword.setText("View Pass")
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Password)

    def show_password(self):
        self.btnViewPassword.setText("Hide Pass")
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Normal)

    def show_hide_password(self):
        """
        Show and Hide the password depending of the
        text of the Button
        """
        text_button = self.btnViewPassword.text()
        if text_button == "View Pass":
            self.show_password()
        else:
            self.hide_password()

    def update_element(self):
        item_list = self.listKeys.currentItem()
        key_object = item_list.data(QtCore.Qt.UserRole).toPyObject()
        new_data = {
            'name':self.txtNameKey.text(),
            'username': self.txtUsername.text(),
            'email':self.txtEmail.text(),
            'password':self.txtPassword.text(),
            'notes':self.txtNotes.toPlainText(),
            'webpage':self.txtWebPage.text(),
        }
        item_updated = update_key(key_object, new_data)
        if item_updated:
            item_list.setText(item_updated.name)
            self.show_hide_password()
        else:
            QtGui.QMessageBox.about(self, "Error",
                                    "There was an error during updating")


    def delete_element(self):
        reply = QtGui.QMessageBox.question(self,
                                           'Deleting key',
                "Are you sure to delete %s?" % self.txtNameKey.text(),
                QtGui.QMessageBox.Yes,
                QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            item = self.listKeys.currentItem()
            item = item.data(QtCore.Qt.UserRole).toPyObject()
            response = delete_key(item)
            self.clean_textbox_info()
            if response:
                self.update_key_list()
            else:
                QtGui.QMessageBox.about(self, "Error",
                                        "There was an error during deleting")
