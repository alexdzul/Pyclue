# -*- coding: utf-8 -*-
__author__ = 'alex'
from PyQt4 import QtGui
from PyQt4 import QtCore

from pyclue.appSettings import ABOUT_MESSAGE
from pyclue.ui.generics.functions import SetIcon, alert, Center
from pyclue.apps.settings.functions import save_settings, decode_password
from pyclue.apps.settings.ui.resources_mapper import get_exit_icon, get_save_info_icon
from pyclue.apps.settings.ui.ui_sizes import get_size

class AppSettingsForm(QtGui.QWidget):

    def __init__(self,settings, MainWindows):
        """
        MainWindows = Main Windows that display all the keys
        """
        super(AppSettingsForm,self).__init__()
        self.settings = settings
        self.Main = MainWindows
        self.constructorUI()

    def constructorUI(self):
        self.drawUI()
        SetIcon(self)
        Center(self)
        self.fill_data()
        self.disable_enable_backup_elements()
        self.setConnectors()
        self.setTextElements()
        self.setFocusOrder()

    def drawUI(self):
        self.setObjectName("SettingsForm")
        get_size(self) # Dibujamos con el mejor tamaño
        self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.setWindowOpacity(1.0)
        self.setWhatsThis("")
        self.setAutoFillBackground(False)
        self.gridLayout_9 = QtGui.QGridLayout(self)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tabMainContainer = QtGui.QTabWidget(self)
        self.tabMainContainer.setToolTip("")
        self.tabMainContainer.setObjectName("tabMainContainer")
        self.tabAccount = QtGui.QWidget()
        self.tabAccount.setObjectName("tabAccount")
        self.gridLayout_2 = QtGui.QGridLayout(self.tabAccount)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gbAccountInfo = QtGui.QGroupBox(self.tabAccount)
        self.gbAccountInfo.setObjectName("gbAccountInfo")
        self.gridLayout_3 = QtGui.QGridLayout(self.gbAccountInfo)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.txtFullName = QtGui.QLineEdit(self.gbAccountInfo)
        self.txtFullName.setObjectName("txtFullName")
        self.gridLayout_3.addWidget(self.txtFullName, 0, 1, 1, 1)
        self.lblFullName = QtGui.QLabel(self.gbAccountInfo)
        self.lblFullName.setObjectName("lblFullName")
        self.gridLayout_3.addWidget(self.lblFullName, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.gbAccountInfo, 0, 0, 1, 1)
        self.gbChangePassword = QtGui.QGroupBox(self.tabAccount)
        self.gbChangePassword.setObjectName("gbChangePassword")
        self.gridLayout_4 = QtGui.QGridLayout(self.gbChangePassword)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lblTypeAgainPass = QtGui.QLabel(self.gbChangePassword)
        self.lblTypeAgainPass.setObjectName("lblTypeAgainPass")
        self.gridLayout_4.addWidget(self.lblTypeAgainPass, 2, 0, 1, 1)
        self.txtTypeAgainPass = QtGui.QLineEdit(self.gbChangePassword)
        self.txtTypeAgainPass.setEchoMode(QtGui.QLineEdit.Password)
        self.txtTypeAgainPass.setObjectName("txtTypeAgainPass")
        self.gridLayout_4.addWidget(self.txtTypeAgainPass, 2, 2, 1, 1)
        self.txtCurrentPass = QtGui.QLineEdit(self.gbChangePassword)
        self.txtCurrentPass.setObjectName("txtCurrentPass")
        self.txtCurrentPass.setEchoMode(QtGui.QLineEdit.Password)
        self.gridLayout_4.addWidget(self.txtCurrentPass, 0, 2, 1, 1)
        self.lblCurrentPass = QtGui.QLabel(self.gbChangePassword)
        self.lblCurrentPass.setObjectName("lblCurrentPass")
        self.gridLayout_4.addWidget(self.lblCurrentPass, 0, 0, 1, 1)
        self.txtNewPass = QtGui.QLineEdit(self.gbChangePassword)
        self.txtNewPass.setObjectName("txtNewPass")
        self.txtNewPass.setEchoMode(QtGui.QLineEdit.Password)
        self.gridLayout_4.addWidget(self.txtNewPass, 1, 2, 1, 1)
        self.lblNewPass = QtGui.QLabel(self.gbChangePassword)
        self.lblNewPass.setObjectName("lblNewPass")
        self.gridLayout_4.addWidget(self.lblNewPass, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.gbChangePassword, 2, 0, 1, 1)
        self.tabMainContainer.addTab(self.tabAccount,"My Account")
        self.tabBackup = QtGui.QWidget()
        self.tabBackup.setObjectName("tabBackup")
        self.gridLayout = QtGui.QGridLayout(self.tabBackup)
        self.gridLayout.setObjectName("gridLayout")
        self.gbPeriod = QtGui.QGroupBox(self.tabBackup)
        self.gbPeriod.setObjectName("gbPeriod")
        self.gridLayout_7 = QtGui.QGridLayout(self.gbPeriod)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.cmbPeriodicity = QtGui.QComboBox(self.gbPeriod)
        self.cmbPeriodicity.setObjectName("cmbPeriodicity")
        self.cmbPeriodicity.addItem("Weekly")
        self.cmbPeriodicity.addItem("Monthly")
        self.gridLayout_7.addWidget(self.cmbPeriodicity, 0, 0, 1, 1)
        self.checkNoBackup = QtGui.QCheckBox(self.gbPeriod)
        self.checkNoBackup.setObjectName("checkNoBackup")
        self.gridLayout_7.addWidget(self.checkNoBackup, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.gbPeriod, 0, 0, 1, 1)
        self.gbStoreSettings = QtGui.QGroupBox(self.tabBackup)
        self.gbStoreSettings.setObjectName("gbStoreSettings")
        self.gridLayout_5 = QtGui.QGridLayout(self.gbStoreSettings)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lblFiles = QtGui.QLabel(self.gbStoreSettings)
        self.lblFiles.setObjectName("lblFiles")
        self.gridLayout_5.addWidget(self.lblFiles, 1, 2, 1, 1)
        self.lblStoreOnly = QtGui.QLabel(self.gbStoreSettings)
        self.lblStoreOnly.setObjectName("lblStoreOnly")
        self.gridLayout_5.addWidget(self.lblStoreOnly, 1, 0, 1, 1)
        self.sbNumFiles = QtGui.QSpinBox(self.gbStoreSettings)
        self.sbNumFiles.setObjectName("sbNumFiles")
        self.gridLayout_5.addWidget(self.sbNumFiles, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.gbStoreSettings, 1, 0, 1, 1)
        self.gbFile = QtGui.QGroupBox(self.tabBackup)
        self.gbFile.setObjectName("gbFile")
        self.gridLayout_6 = QtGui.QGridLayout(self.gbFile)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lblFileName = QtGui.QLabel(self.gbFile)
        self.lblFileName.setObjectName("lblFileName")
        self.gridLayout_6.addWidget(self.lblFileName, 0, 0, 1, 1)
        self.txtFileName = QtGui.QLineEdit(self.gbFile)
        self.txtFileName.setObjectName("txtFileName")
        self.gridLayout_6.addWidget(self.txtFileName, 0, 1, 1, 1)
        self.lblFormatDate = QtGui.QLabel(self.gbFile)
        self.lblFormatDate.setObjectName("lblFormatDate")
        self.gridLayout_6.addWidget(self.lblFormatDate, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.gbFile, 2, 0, 1, 1)
        self.tabMainContainer.addTab(self.tabBackup,"Backup")
        self.tabAbout = QtGui.QWidget()
        self.tabAbout.setObjectName("tabAbout")
        self.gridLayout_8 = QtGui.QGridLayout(self.tabAbout)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lblAbout = QtGui.QLabel(self.tabAbout)
        self.lblAbout.setObjectName("lblAbout")
        self.gridLayout_8.addWidget(self.lblAbout, 0, 0, 1, 1)
        self.tabMainContainer.addTab(self.tabAbout,"About PyClue")
        self.gridLayout_9.addWidget(self.tabMainContainer, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSaveMyAccount = QtGui.QPushButton(self)
        self.btnSaveMyAccount.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(get_save_info_icon()), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSaveMyAccount.setIcon(icon1)
        self.btnSaveMyAccount.setIconSize(QtCore.QSize(40, 40))
        self.btnSaveMyAccount.setObjectName("btnSaveMyAccount")
        self.btnSaveMyAccount.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.btnSaveMyAccount)
        self.btnCancel = QtGui.QPushButton(self)
        self.btnCancel.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(get_exit_icon()), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon2)
        self.btnCancel.setIconSize(QtCore.QSize(40, 40))
        self.btnCancel.setObjectName("btnCancel")
        self.btnCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.btnCancel)
        self.gridLayout_9.addLayout(self.horizontalLayout, 1, 0, 1, 1)

    def run(self):
        self.show()



    def setTextElements(self):
        self.lblFileName.setText("File Name:")
        self.setWindowTitle("Settings")
        self.lblAbout.setText(ABOUT_MESSAGE)
        self.lblCurrentPass.setText("Current Password:")
        self.lblFormatDate.setText(self.settings.file_name_sufix_backup)
        self.lblFullName.setText("Full Name:")
        self.lblNewPass.setText("New Password:")
        self.lblTypeAgainPass.setText("Type Again:")
        self.lblStoreOnly.setText("Store only:")
        self.gbPeriod.setTitle("Period.")
        self.gbFile.setTitle("File.")
        self.gbStoreSettings.setTitle("Store Settings.")
        self.gbAccountInfo.setTitle("Account Info.")
        self.gbChangePassword.setTitle("Change password for login.")
        self.checkNoBackup.setText("No Backups.")
        self.lblFiles.setText("Backups.")

    def fill_data(self):
        self.txtFullName.setText(self.settings.user_fullName)
        self.checkNoBackup.setChecked(self.settings.deactivate_backup)
        self.sbNumFiles.setValue(int(self.settings.num_files_store))
        self.sbNumFiles.setMinimum(1)
        self.txtFileName.setText(self.settings.file_name_backup)
        # Find Selected periodicity and set current index
        index = self.cmbPeriodicity.findText(self.settings.period_backup)
        self.cmbPeriodicity.setCurrentIndex(index)



    def get_form_data(self):
        self.FullName = self.txtFullName.text()
        self.CurrentPass = self.txtCurrentPass.text()
        self.password_1 = self.txtNewPass.text()
        self.password_2 = self.txtTypeAgainPass.text()
        self.FileName = self.txtFileName.text()
        self.NoBackup = self.checkNoBackup.isChecked()
        self.NumFiles = self.sbNumFiles.text()
        self.Periodicity = self.cmbPeriodicity.currentText()


    def save_settings_(self):
        self.get_form_data()
        if self.CurrentPass == decode_password(self.settings.user_password):
            if self.password_1 == self.password_2:
                if self.password_1 == "":
                    success = save_settings(self.Periodicity,self.NoBackup,
                              self.NumFiles, self.FileName,self.FullName)
                else:
                    success = save_settings(self.Periodicity,self.NoBackup,
                              self.NumFiles, self.FileName,self.FullName,self.password_1)
                if success:
                    self.close()
                    self.Main.load_settings()
                else:
                    alert(self,"Error","There was an error saving data...")
            else:
                alert(self,"Info","Passwords don't match.")
        else:
            alert(self,"Info","Incorrect current password")
            self.txtCurrentPass.setFocus()

    def save_settings(self):
        success = False
        self.get_form_data()
        if self.CurrentPass == "":
            success = save_settings(self.Periodicity,self.NoBackup,
                              self.NumFiles, self.FileName,self.FullName)
        else:
            if self.CurrentPass == decode_password(self.settings.user_password):
                if self.password_1 == self.password_2:
                    if self.password_1 == "":
                        success = save_settings(self.Periodicity,self.NoBackup,
                                  self.NumFiles, self.FileName,self.FullName)
                    else:
                        success = save_settings(self.Periodicity,self.NoBackup,
                                  self.NumFiles, self.FileName,self.FullName,self.password_1)
                else:
                    alert(self,"Info","Passwords don't match.")
            else:
                alert(self,"info","Incorrect current password")
        if success:
            self.close()
            self.Main.load_settings()







    def setConnectors(self):
        self.btnCancel.pressed.connect(self.close)
        self.btnSaveMyAccount.pressed.connect(self.save_settings)
        self.checkNoBackup.stateChanged.connect(self.disable_enable_backup_elements)

    def setFocusOrder(self):
        self.setTabOrder(self.txtFullName, self.txtCurrentPass)
        self.setTabOrder(self.txtNewPass,self.txtTypeAgainPass)
        
    def disable_enable_backup_elements(self):
        if self.checkNoBackup.isChecked():
            self.txtFileName.setEnabled(False)
            self.cmbPeriodicity.setEnabled(False)
            self.sbNumFiles.setEnabled(False)
        else:
            self.txtFileName.setEnabled(True)
            self.cmbPeriodicity.setEnabled(True)
            self.sbNumFiles.setEnabled(True)