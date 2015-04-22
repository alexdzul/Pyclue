# -*- coding: utf-8 -*-
__author__ = 'alex'
import sys
import traceback
from PyQt5 import QtGui, QtWidgets
from PyQt5 import QtCore
from pyclue.apps.main.ui.resources_mapper import *
from pyclue.appSettings import WELCOME_MESSAGE
from pyclue.ui.generics.functions import Center, SetIcon
from pyclue.apps.settings.functions import create_settings, get_settings
from pyclue.apps.keys.functions import get_keys, delete_key, update_key
from pyclue.apps.keys.ui.forms import AddKeyForm
from pyclue.apps.security.functions import decode_password
from pyclue.apps.settings.ui.forms import AppSettingsForm
from pyclue.apps.main.ui.ui_sizes import get_launch_size, get_main_size


class LaunchForm(QtWidgets.QDialog):

    def __init__(self):
        super(LaunchForm, self).__init__()
        self.constructorUI()

    def constructorUI(self):
        self.drawUI()
        self.setConnector()
        self.setTextElements()
        Center(self)
        SetIcon(self)

    def run(self):
        self.show()

    def exit(self):
        QtCore.QCoreApplication.instance().quit()

    def drawUI(self):
        self.setObjectName("LaunchForm")
        get_launch_size(self)
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.gridMain = QtWidgets.QGridLayout(self)
        self.gridMain.setObjectName("gridMain")
        self.lblWelcome = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lblWelcome.setFont(font)
        self.lblWelcome.setObjectName("lblWelcome")
        self.gridMain.addWidget(self.lblWelcome, 0, 0, 1, 1)
        self.lblMessage = QtWidgets.QLabel(self)
        self.lblMessage.setTextFormat(QtCore.Qt.AutoText)
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setObjectName("lblMessage")
        self.gridMain.addWidget(self.lblMessage, 1, 0, 1, 1)
        self.gbInitialinfo = QtWidgets.QGroupBox(self)
        self.gbInitialinfo.setObjectName("gbInitialinfo")
        self.gridInitialInfo = QtWidgets.QGridLayout(self.gbInitialinfo)
        self.gridInitialInfo.setObjectName("gridInitialInfo")
        self.txtFullName = QtWidgets.QLineEdit(self.gbInitialinfo)
        self.txtFullName.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.txtFullName.setObjectName("txtFullName")
        self.gridInitialInfo.addWidget(self.txtFullName, 0, 1, 1, 1)
        self.lblFullName = QtWidgets.QLabel(self.gbInitialinfo)
        self.lblFullName.setObjectName("lblFullName")
        self.gridInitialInfo.addWidget(self.lblFullName, 0, 0, 1, 1)
        self.gridMain.addWidget(self.gbInitialinfo, 2, 0, 1, 1)
        self.gbLoginData = QtWidgets.QGroupBox(self)
        self.gbLoginData.setObjectName("gbLoginData")
        self.gridLayout = QtWidgets.QGridLayout(self.gbLoginData)
        self.gridLayout.setObjectName("gridLayout")
        self.lblPassword_2 = QtWidgets.QLabel(self.gbLoginData)
        self.lblPassword_2.setObjectName("lblPassword_2")
        self.gridLayout.addWidget(self.lblPassword_2, 1, 0, 1, 1)
        self.txtPassword = QtWidgets.QLineEdit(self.gbLoginData)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.gridLayout.addWidget(self.txtPassword, 0, 1, 1, 1)
        self.lblPassword = QtWidgets.QLabel(self.gbLoginData)
        self.lblPassword.setObjectName("lblPassword")
        self.gridLayout.addWidget(self.lblPassword, 0, 0, 1, 1)
        self.txtPassword_2 = QtWidgets.QLineEdit(self.gbLoginData)
        self.txtPassword_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword_2.setObjectName("txtPassword_2")
        self.gridLayout.addWidget(self.txtPassword_2, 1, 1, 1, 1)
        self.gridMain.addWidget(self.gbLoginData, 3, 0, 1, 1)
        self.gridButtons = QtWidgets.QGridLayout()
        self.gridButtons.setObjectName("gridButtons")
        self.btnSave = QtWidgets.QPushButton(self)
        self.btnSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(get_save_icon()), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSave.setIcon(icon)
        self.btnSave.setIconSize(QtCore.QSize(30, 30))
        self.btnSave.setObjectName("btnSave")
        self.gridButtons.addWidget(self.btnSave, 0, 0, 1, 1)
        self.btnExit = QtWidgets.QPushButton(self)
        self.btnExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(get_exit_icon()), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon1)
        self.btnExit.setIconSize(QtCore.QSize(30, 30))
        self.btnExit.setObjectName("btnExit")
        self.gridButtons.addWidget(self.btnExit, 0, 1, 1, 1)
        self.gridMain.addLayout(self.gridButtons, 4, 0, 1, 1)

    def setTextElements(self):
        self.lblWelcome.setText("Welcome to PyClue!")
        self.lblMessage.setText(WELCOME_MESSAGE)
        self.lblFullName.setText("Full Name:")
        self.lblPassword.setText("Password:")
        self.lblPassword_2.setText("Retype Password:")
        self.setWindowTitle("Welcome!")
        self.btnExit.setText("Exit")
        self.btnSave.setText("Save")

    def setConnector(self):
        self.btnSave.clicked.connect(self.save_settings)
        self.btnExit.clicked.connect(self.exit)


    def save_settings(self):
        """
        Save the initial configuration
        """
        self.construct_get_data()
        data = self.validate_data()
        if data['status']:
            if self.validate_password():
                success = create_settings(self.fullName,self.password_one)
                if success:
                    QtWidgets.QMessageBox.about(self, "Great!", "Settings created successfully!"
                                                        "<br>Please Open the Software Again")
                    self.close()
                else:
                    QtWidgets.QMessageBox.about(self, "Error", "Sorry! Unnespected error \n")
                    self.exit()
            else:
                QtWidgets.QMessageBox.about(self, "Error", "Password not match")
                self.txtPassword.setText("")
                self.txtPassword_2.setText("")
                self.txtPassword.setFocus()
        else:
            QtWidgets.QMessageBox.about(self, "Error", data['message'])

    def construct_get_data(self):
        """
        Takes the field values and insert it to self variables
        """
        self.fullName = self.txtFullName.text()
        self.password_one = self.txtPassword.text()
        self.password_two = self.txtPassword_2.text()


    def validate_data(self):
        """
        Validate empty fields.
        """
        self.construct_get_data()
        flag = True
        message = ""
        if self.fullName == "":
            flag = False
            message += "Field: Full Name required \n"
        if self.password_one == "":
            flag = False
            message += "Field: Password required \n"
        if self.password_two == "":
            flag = False
            message += "Field: Retype Pass required \n"
        return {'status': flag, 'message': message}

    def validate_password(self):
        """
        Validate correct password
        """
        pw_1 = self.password_one
        pw_2 = self.password_two
        if pw_1 == "" or pw_2 == "":
            response = False
        elif pw_1 == pw_2:
            response = True
        else:
            response = False
        return response


class MainForm(QtWidgets.QMainWindow):
    def __init__(self, settings, loginForm):
        """
        Build the Form with the User information
        """
        self.loginForm = loginForm
        self.settings = settings
        super(MainForm, self).__init__()
        self.constructorUI()


    def constructorUI(self):
        self.drawUI()
        message = "Welcome: %s"%(self.settings.user_fullName)
        self.set_statusBar(message)
        self.set_list_elements()
        self.setConnectors()
        self.disable_fields()
        Center(self)


    def drawUI(self):
        # Nombre de la ventana
        self.setWindowTitle('PyClue')
        # Windows Size
        get_main_size(self)
        self.centralwidget = QtWidgets.QWidget(self)
        SetIcon(self)
        # Set the grid to show de keys list
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listKeys = QtWidgets.QListWidget(self.centralwidget)
        self.listKeys.setObjectName("listKeys")
        self.gridLayout_2.addWidget(self.listKeys, 0, 0, 1, 1)
        # Set the group box info and added into a grid element
        self.gbInformation = QtWidgets.QGroupBox(self.centralwidget)
        self.gbInformation.setObjectName("gbInformation")
        self.gbInformation.setTitle("Information")
        self.gridLayout = QtWidgets.QGridLayout(self.gbInformation)
        self.gridLayout.setObjectName("gridLayout")

        # Set the txtNameKey and its Label into a grid element
        self.lblNameKey = QtWidgets.QLabel(self.gbInformation)
        self.lblNameKey.setObjectName("lblNameKey")
        self.lblNameKey.setText("Name of the Key:")
        self.gridLayout.addWidget(self.lblNameKey, 0, 0, 1, 1)
        self.txtNameKey = QtWidgets.QLineEdit(self.gbInformation)
        self.txtNameKey.setObjectName("txtNameKey")
        self.gridLayout.addWidget(self.txtNameKey, 1, 0, 1, 1)
        # Set the txtUsername and its Label into a grid element
        self.lblUsername = QtWidgets.QLabel(self.gbInformation)
        self.lblUsername.setObjectName("lblUsername")
        self.lblUsername.setText("Username:")
        self.gridLayout.addWidget(self.lblUsername, 2, 0, 1, 1)
        self.txtUsername = QtWidgets.QLineEdit(self.gbInformation)
        self.txtUsername.setMinimumSize(QtCore.QSize(0, 0))
        self.txtUsername.setObjectName("txtUsername")
        self.gridLayout.addWidget(self.txtUsername, 3, 0, 1, 1)
        # Set the txtEmail and its Label into a grid Element
        self.lblEmail = QtWidgets.QLabel(self.gbInformation)
        self.lblEmail.setObjectName("lblEmail")
        self.lblEmail.setText("Email:")
        self.gridLayout.addWidget(self.lblEmail, 4, 0, 1, 1)
        self.txtEmail = QtWidgets.QLineEdit(self.gbInformation)
        self.txtEmail.setObjectName("txtEmail")
        self.gridLayout.addWidget(self.txtEmail, 5, 0, 1, 1)
        # Set the txtWebPage and its Label into a grid Element
        self.lblWebPage = QtWidgets.QLabel(self.gbInformation)
        self.lblWebPage.setObjectName("lblWebPage")
        self.lblWebPage.setText("WebPage:")
        self.gridLayout.addWidget(self.lblWebPage, 6, 0, 1, 1)
        self.txtWebPage = QtWidgets.QLineEdit(self.gbInformation)
        self.txtWebPage.setObjectName("txtWebPage")
        self.gridLayout.addWidget(self.txtWebPage, 7, 0, 1, 1)
        # Set a Horizontal Layout in order to set txt and View password together
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # Set the txtPassword and its Label into a grid Element
        self.lblPassword = QtWidgets.QLabel(self.gbInformation)
        self.lblPassword.setObjectName("lblPassword")
        self.lblPassword.setText("Password:")
        self.gridLayout.addWidget(self.lblPassword, 8, 0, 1, 1)
        self.txtPassword = QtWidgets.QLineEdit(self.gbInformation)
        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_2.addWidget(self.txtPassword)
        # Set the Button View Password and added into a grid element
        self.btnViewPassword = QtWidgets.QPushButton(self.gbInformation)
        self.btnViewPassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnViewPassword.setObjectName("btnViewPassword")
        self.btnViewPassword.setText("View Pass")
        icon = QtGui.QIcon(get_view_pass_icon())
        self.btnViewPassword.setIcon(icon)
        self.horizontalLayout_2.addWidget(self.btnViewPassword)
        self.gridLayout.addLayout(self.horizontalLayout_2, 9, 0, 1, 1)
        # Set the txtNotes and its Label into a grid element
        self.lblNotes = QtWidgets.QLabel(self.gbInformation)
        self.lblNotes.setObjectName("lblNotes")
        self.lblNotes.setText("Notes:")
        self.gridLayout.addWidget(self.lblNotes, 10, 0, 1, 1)
        self.txtNotes = QtWidgets.QTextEdit(self.gbInformation)
        self.txtNotes.setObjectName("txtNotes")
        self.gridLayout.addWidget(self.txtNotes, 11, 0, 1, 1)
        # Set another Group Box to show btn Delete and Save
        self.groupBox = QtWidgets.QGroupBox(self.gbInformation)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle("Actions")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # Add the Delete Button ===========================
        self.btnDelete = QtWidgets.QPushButton(self.groupBox)
        self.btnDelete.setObjectName("btnDelete")
        icon = QtGui.QIcon(get_delete_icon())
        self.btnDelete.setIcon(icon)
        self.btnDelete.setText("Delete")
        self.btnDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.btnDelete)
        # Add the Save Button ============================
        self.btnSave = QtWidgets.QPushButton(self.groupBox)
        self.btnSave.setObjectName("btnSave")
        icon = QtGui.QIcon(get_update_icon())
        self.btnSave.setIcon(icon)
        self.btnSave.setText("Save")
        self.btnSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.btnSave)
        self.gridLayout.addWidget(self.groupBox, 12, 0, 1, 1)
        self.gridLayout_2.addWidget(self.gbInformation, 0, 1, 1, 1)
        self.setCentralWidget(self.centralwidget)
        # ===================== START ToolBar =========================================
        # Add the Lock Button
        self.lockAction = QtWidgets.QAction(QtGui.QIcon(get_locked_icon()),'Lock the Windows',self)
        self.lockAction.setShortcut('Ctrl+L')
        # Add the Exit Button
        self.exitAction = QtWidgets.QAction(QtGui.QIcon(get_exit_icon()),'Exit',self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.triggered.connect(QtWidgets.qApp.quit)
        # Add the Add Button
        self.addKeyAction = QtWidgets.QAction(QtGui.QIcon(get_add_icon()),'Add Key',self)
        self.addKeyAction.setShortcut('Ctrl+A')
        # Add the Settings Button
        self.settingsAction = QtWidgets.QAction(QtGui.QIcon(get_settings_icon()),'Settings',self)
        self.settingsAction.setShortcut('Ctrl+S')
        # Create toolBar Element
        self.toolBar = self.addToolBar('Main')
        # Add the elements to the toolBar
        self.toolBar.addAction(self.addKeyAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.settingsAction)
        self.toolBar.addAction(self.lockAction)
        self.toolBar.addAction(self.exitAction)
        # ====================== END ToolBar =============================================

    def get_item_info(self):
        try:
            self.disable_fields()
            self.hide_password()
            item = self.listKeys.currentItem()
            item = item.data(QtCore.Qt.UserRole)
            self.txtNameKey.setText(item.name)
            self.txtUsername.setText(item.username)
            self.txtNotes.setText(item.notes)
            self.txtPassword.setText(decode_password(item.password))
            self.txtEmail.setText(item.email)
            self.txtWebPage.setText(item.webpage)
        except AttributeError:
            pass
        except:
            message = "Error" + str(sys.exc_info()[0]) + " " +\
                      str(sys.exc_info()[1]) + " " + \
                      str(sys.exc_info()[2]) + " " + traceback.format_exc()
            print(message)
            pass

    def run(self):
        self.show()


    def show_add_key_form(self):
        self.createAddForm()

    def set_list_elements(self):
        keys = get_keys()
        if keys:
            for key in keys:
                item = QtWidgets.QListWidgetItem()
                item.setText(key.name)
                item.setData(QtCore.Qt.UserRole, key)
                self.listKeys.addItem(item)

    def clear_list_elements(self):
        self.listKeys.clear()

    def createAddForm(self):
        main_form = self
        self.addKey = AddKeyForm(main_form)
        self.addKey.show()

    def set_statusBar(self, message):
        self.statusBar().showMessage(message)

    def hide_this_and_show_login(self):
        self.close()
        self.loginForm.show()

    def update_key_list(self):
        self.clear_list_elements()
        self.set_list_elements()

    def show_appSettings_form(self):
        self.appSett = AppSettingsForm(self.settings,self)
        self.appSett.run()

    def setConnectors(self):
        self.listKeys.currentItemChanged.connect(self.get_item_info)
        self.listKeys.doubleClicked.connect(self.enable_fields)
        self.btnViewPassword.pressed.connect(self.show_hide_password)
        self.btnDelete.pressed.connect(self.delete_element)
        self.btnSave.pressed.connect(self.update_element)
        # Add  Signals to the toolBar elements
        self.addKeyAction.triggered.connect(self.show_add_key_form)
        self.lockAction.triggered.connect(self.hide_this_and_show_login)
        self.settingsAction.triggered.connect(self.show_appSettings_form)

    def enable_fields(self):
        self.btnDelete.setEnabled(True)
        self.btnSave.setEnabled(True)
        self.txtEmail.setEnabled(True)
        self.txtNameKey.setEnabled(True)
        self.txtNotes.setEnabled(True)
        self.txtPassword.setEnabled(True)
        self.txtUsername.setEnabled(True)
        self.txtWebPage.setEnabled(True)

    def disable_fields(self):
        self.btnSave.setEnabled(False)
        self.btnDelete.setEnabled(False)
        self.txtEmail.setEnabled(False)
        self.txtNameKey.setEnabled(False)
        self.txtNotes.setEnabled(False)
        self.txtPassword.setEnabled(False)
        self.txtUsername.setEnabled(False)
        self.txtWebPage.setEnabled(False)

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
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def show_password(self):
        self.btnViewPassword.setText("Hide Pass")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Normal)

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
        key_object = item_list.data(QtCore.Qt.UserRole)
        new_data = {
            'name': self.txtNameKey.text(),
            'username': self.txtUsername.text(),
            'email': self.txtEmail.text(),
            'password': self.txtPassword.text(),
            'notes': self.txtNotes.toPlainText(),
            'webpage': self.txtWebPage.text(),
        }
        item_updated = update_key(key_object, new_data)
        if item_updated:
            item_list.setText(item_updated.name)
            self.disable_fields()  # Deshabilitamos de nuevo los campos
            self.hide_password()
        else:
            QtWidgets.QMessageBox.about(self, "Error", "There was an error during updating")

    def load_settings(self):
        self.settings = get_settings()
        self.set_statusBar("Welcome "+self.settings.user_fullName)


    def delete_element(self):
        reply = QtWidgets.QMessageBox.question(self,
                                               'Deleting key',
                                               "Are you sure to delete {0}?".format(self.txtNameKey.text()),
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            item = self.listKeys.currentItem()
            item = item.data(QtCore.Qt.UserRole)
            response = delete_key(item)
            self.clean_textbox_info()
            if response:
                self.update_key_list()
            else:
                QtWidgets.QMessageBox.about(self, "Error", "There was an error during deleting")