# -*- coding: utf-8 -*-
__author__ = 'alex'
from PyQt4 import QtGui
from PyQt4 import QtCore
from settings import RESOURCES_DIR, ABOUT_MESSAGE
from ui.generics.functions import SetIcon
import os


class AppSettingsForm(QtGui.QWidget):

    def __init__(self, user, MainWindows):
        """
        user = Object User that is logged in
        MainWindows = Main Windows that display all the keys
        """
        super(AppSettingsForm,self).__init__()
        self.user = user
        self.Main = MainWindows
        self.constructorUI()

    def constructorUI(self):
        self.drawUI()
        SetIcon(self)
        #self.setConnector()

    def drawUI(self):
        self.setObjectName("SettingsForm")
        self.setWindowTitle("Main Settings")
        self.resize(483, 383)
        self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.setWindowOpacity(1.0)
        self.setAutoFillBackground(False)
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabMainContainer = QtGui.QTabWidget(self)
        self.tabMainContainer.setObjectName("tabMainContainer")
        self.tabAccount = QtGui.QWidget()
        self.tabAccount.setObjectName("tabAccount")
        self.gridLayout_2 = QtGui.QGridLayout(self.tabAccount)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gbChangePassword = QtGui.QGroupBox(self.tabAccount)
        self.gbChangePassword.setObjectName("gbChangePassword")
        self.gbChangePassword.setTitle("Change Password for login:")
        self.gridLayout_4 = QtGui.QGridLayout(self.gbChangePassword)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lblTypeAgainPass = QtGui.QLabel(self.gbChangePassword)
        self.lblTypeAgainPass.setObjectName("lblTypeAgainPass")
        self.lblTypeAgainPass.setText("Type Again:")
        self.gridLayout_4.addWidget(self.lblTypeAgainPass, 2, 0, 1, 1)
        self.txtTypeAgainPass = QtGui.QLineEdit(self.gbChangePassword)
        self.txtTypeAgainPass.setObjectName("txtTypeAgainPass")
        self.gridLayout_4.addWidget(self.txtTypeAgainPass, 2, 2, 1, 1)
        self.txtCurrentPass = QtGui.QLineEdit(self.gbChangePassword)
        self.txtCurrentPass.setObjectName("txtCurrentPass")
        self.gridLayout_4.addWidget(self.txtCurrentPass, 0, 2, 1, 1)
        self.lblCurrentPass = QtGui.QLabel(self.gbChangePassword)
        self.lblCurrentPass.setObjectName("lblCurrentPass")
        self.lblCurrentPass.setText("Current Password:")
        self.gridLayout_4.addWidget(self.lblCurrentPass, 0, 0, 1, 1)
        self.txtNewPass = QtGui.QLineEdit(self.gbChangePassword)
        self.txtNewPass.setObjectName("txtNewPass")
        self.gridLayout_4.addWidget(self.txtNewPass, 1, 2, 1, 1)
        self.lblNewPass = QtGui.QLabel(self.gbChangePassword)
        self.lblNewPass.setObjectName("lblNewPass")
        self.lblNewPass.setText("New Password:")
        self.gridLayout_4.addWidget(self.lblNewPass, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.gbChangePassword, 2, 0, 1, 1)
        self.gbAccountInfo = QtGui.QGroupBox(self.tabAccount)
        self.gbAccountInfo.setObjectName("gbAccountInfo")
        self.gbAccountInfo.setTitle("Account Info")
        self.gridLayout_3 = QtGui.QGridLayout(self.gbAccountInfo)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.txtLastName = QtGui.QLineEdit(self.gbAccountInfo)
        self.txtLastName.setObjectName("txtLastName")
        self.gridLayout_3.addWidget(self.txtLastName, 2, 1, 1, 1)
        self.lblFirstName = QtGui.QLabel(self.gbAccountInfo)
        self.lblFirstName.setObjectName("lblFirstName")
        self.lblFirstName.setText("First Name:")
        self.gridLayout_3.addWidget(self.lblFirstName, 1, 0, 1, 1)
        self.txtFirstName = QtGui.QLineEdit(self.gbAccountInfo)
        self.txtFirstName.setObjectName("txtFirstName")
        self.gridLayout_3.addWidget(self.txtFirstName, 1, 1, 1, 1)
        self.lblLastName = QtGui.QLabel(self.gbAccountInfo)
        self.lblLastName.setObjectName("lblLastName")
        self.lblLastName.setText("Las Name:")
        self.gridLayout_3.addWidget(self.lblLastName, 2, 0, 1, 1)
        self.lblUsername = QtGui.QLabel(self.gbAccountInfo)
        self.lblUsername.setObjectName("lblUsername")
        self.lblUsername.setText("Username:")
        self.gridLayout_3.addWidget(self.lblUsername, 0, 0, 1, 1)
        self.txtUsername = QtGui.QLineEdit(self.gbAccountInfo)
        self.txtUsername.setObjectName("txtUsername")
        self.gridLayout_3.addWidget(self.txtUsername, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.gbAccountInfo, 0, 0, 1, 1)
        self.btnSaveMyAccount = QtGui.QPushButton(self.tabAccount)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap((self.get_save_info_icon())), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSaveMyAccount.setIcon(icon)
        self.btnSaveMyAccount.setIconSize(QtCore.QSize(24, 24))
        self.btnSaveMyAccount.setObjectName("btnSaveMyAccount")
        self.btnSaveMyAccount.setText("Save")
        self.gridLayout_2.addWidget(self.btnSaveMyAccount, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.tabMainContainer.addTab(self.tabAccount,"")
        self.tabBackup = QtGui.QWidget()
        self.tabBackup.setObjectName("tabBackup")
        self.gridLayout = QtGui.QGridLayout(self.tabBackup)
        self.gridLayout.setObjectName("gridLayout")
        self.gbPeriod = QtGui.QGroupBox(self.tabBackup)
        self.gbPeriod.setObjectName("gbPeriod")
        self.gbPeriod.setTitle("Period")
        self.gridLayout_7 = QtGui.QGridLayout(self.gbPeriod)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.cmbPeriodicity = QtGui.QComboBox(self.gbPeriod)
        self.cmbPeriodicity.setObjectName("cmbPeriodicity")
        self.cmbPeriodicity.addItem("Weekly")
        self.cmbPeriodicity.addItem("Monthly")
        self.gridLayout_7.addWidget(self.cmbPeriodicity, 0, 0, 1, 1)
        self.checkNoBackup = QtGui.QCheckBox(self.gbPeriod)
        self.checkNoBackup.setObjectName("checkNoBackup")
        self.checkNoBackup.setText("No Backup.")
        self.gridLayout_7.addWidget(self.checkNoBackup, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.gbPeriod, 0, 0, 1, 1)
        self.gbStoreSettings = QtGui.QGroupBox(self.tabBackup)
        self.gbStoreSettings.setObjectName("gbStoreSettings")
        self.gbStoreSettings.setTitle("Store Settings")
        self.gridLayout_5 = QtGui.QGridLayout(self.gbStoreSettings)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lblFiles = QtGui.QLabel(self.gbStoreSettings)
        self.lblFiles.setObjectName("lblFiles")
        self.lblFiles.setText("files.")
        self.gridLayout_5.addWidget(self.lblFiles, 1, 2, 1, 1)
        self.btnFileBrowser = QtGui.QPushButton(self.gbStoreSettings)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap((self.get_folder_icon())), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFileBrowser.setIcon(icon1)
        self.btnFileBrowser.setIconSize(QtCore.QSize(20, 20))
        self.btnFileBrowser.setObjectName("btnFileBrowser")
        self.btnFileBrowser.setText("...")
        self.gridLayout_5.addWidget(self.btnFileBrowser, 1, 4, 1, 1)
        self.lblStoreOnly = QtGui.QLabel(self.gbStoreSettings)
        self.lblStoreOnly.setObjectName("lblStoreOnly")
        self.lblStoreOnly.setText("Store only:")
        self.gridLayout_5.addWidget(self.lblStoreOnly, 1, 0, 1, 1)
        self.txtStorePath = QtGui.QLineEdit(self.gbStoreSettings)
        self.txtStorePath.setObjectName("txtStorePath")
        self.gridLayout_5.addWidget(self.txtStorePath, 0, 0, 1, 5)
        self.sbNumDays = QtGui.QSpinBox(self.gbStoreSettings)
        self.sbNumDays.setObjectName("sbNumDays")
        self.gridLayout_5.addWidget(self.sbNumDays, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.gbStoreSettings, 1, 0, 1, 1)
        self.gbFile = QtGui.QGroupBox(self.tabBackup)
        self.gbFile.setObjectName("gbFile")
        self.gbFile.setTitle("File")
        self.gridLayout_6 = QtGui.QGridLayout(self.gbFile)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lblFileName = QtGui.QLabel(self.gbFile)
        self.lblFileName.setObjectName("lblFileName")
        self.lblFileName.setText("Name:")
        self.gridLayout_6.addWidget(self.lblFileName, 0, 0, 1, 1)
        self.txtFileName = QtGui.QLineEdit(self.gbFile)
        self.txtFileName.setObjectName("txtFileName")
        self.gridLayout_6.addWidget(self.txtFileName, 0, 1, 1, 1)
        self.lblFormatDate = QtGui.QLabel(self.gbFile)
        self.lblFormatDate.setObjectName("lblFormatDate")
        self.lblFormatDate.setText("_DD-MM-YY")
        self.gridLayout_6.addWidget(self.lblFormatDate, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.gbFile, 2, 0, 1, 1)
        self.btnSaveBackup = QtGui.QPushButton(self.tabBackup)
        self.btnSaveBackup.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnSaveBackup.setInputMethodHints(QtCore.Qt.ImhNone)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap((self.get_save_info_icon())), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSaveBackup.setIcon(icon2)
        self.btnSaveBackup.setIconSize(QtCore.QSize(24, 24))
        self.btnSaveBackup.setAutoDefault(False)
        self.btnSaveBackup.setDefault(False)
        self.btnSaveBackup.setFlat(False)
        self.btnSaveBackup.setObjectName("btnSaveBackup")
        self.btnSaveBackup.setText("Save")
        self.gridLayout.addWidget(self.btnSaveBackup, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.tabMainContainer.addTab(self.tabBackup,"")
        self.tabAbout = QtGui.QWidget()
        self.tabAbout.setObjectName("tabAbout")
        self.gridLayout_8 = QtGui.QGridLayout(self.tabAbout)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lblAbout = QtGui.QLabel(self.tabAbout)
        self.lblAbout.setObjectName("lblAbout")
        self.lblAbout.setText(ABOUT_MESSAGE)
        self.gridLayout_8.addWidget(self.lblAbout, 0, 0, 1, 1)
        self.tabMainContainer.addTab(self.tabAbout, "")
        self.verticalLayout.addWidget(self.tabMainContainer)
        # Add title to the Tabs.
        self.tabMainContainer.setTabText(self.tabMainContainer.indexOf(self.tabAbout),"About")
        self.tabMainContainer.setTabText(self.tabMainContainer.indexOf(self.tabAccount),"Account")
        self.tabMainContainer.setTabText(self.tabMainContainer.indexOf(self.tabBackup),"Backup")
        # Add the Account tab like the first tab.
        self.tabMainContainer.setCurrentIndex(0)

    def run(self):
        self.show()

    def get_save_info_icon(self):
        img = "Save.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'settings/%s'%img))
        return path

    def get_folder_icon(self):
        img = "folder.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'settings/%s'%img))
        return path