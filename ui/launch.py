__author__ = 'edzul'
from PyQt4 import QtGui
from PyQt4 import QtCore
from settings import WELCOME_MESSAGE
from ui.generics.functions import Center,SetIcon


class LaunchForm(QtGui.QWidget):

    def __init__(self):
        super(LaunchForm,self).__init__()
        self.constructorUI()

    def constructorUI(self):
        self.drawUI()
        self.setConnector()
        Center(self)

    def run(self):
        self.show()

    def exit(self):
        QtCore.QCoreApplication.instance().quit()

    def drawUI(self):
        # Set some basic settings to the form
        self.setWindowTitle('Welcome!')
        self.resize(300, 316)
        self.setMinimumSize(QtCore.QSize(300, 316))
        self.setMaximumSize(QtCore.QSize(500, 500))
        SetIcon(self)
        # Create the main Grid
        self.gridMain = QtGui.QGridLayout(self)
        self.gridMain.setObjectName("gridName")
        #1. Add the Welcome label and insert it to the Main Grid
        self.lblWelcome = QtGui.QLabel(self)
        self.lblWelcome.setObjectName("lblWelcome")
        self.lblWelcome.setText("Welcome to PyClue!!")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lblWelcome.setFont(font)
        self.gridMain.addWidget(self.lblWelcome, 0, 0, 1, 1)
        #2. Add the Message Label an insert it to the Main Grid
        self.lblMessage = QtGui.QLabel(self)
        self.lblMessage.setTextFormat(QtCore.Qt.AutoText)
        self.lblMessage.setText(WELCOME_MESSAGE)
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setObjectName("lblMessage")
        self.gridMain.addWidget(self.lblMessage, 1, 0, 1, 1)
        #3. Add the Initial Info group and insert it to the grid Initial Info
        self.gbInitialinfo = QtGui.QGroupBox(self)
        self.gbInitialinfo.setObjectName("gbInitialinfo")
        self.gbInitialinfo.setTitle("Initial Info")
        self.gridInitialInfo = QtGui.QGridLayout(self.gbInitialinfo)
        self.gridInitialInfo.setObjectName("gridInitialInfo")
        self.lblFirstName = QtGui.QLabel(self.gbInitialinfo)
        self.lblFirstName.setObjectName("lblFirstName")
        self.lblFirstName.setText("First Name:")
        self.gridInitialInfo.addWidget(self.lblFirstName, 0, 0, 1, 1)
        self.txtFirstName = QtGui.QLineEdit(self.gbInitialinfo)
        self.txtFirstName.setObjectName("txtFirstName")
        self.gridInitialInfo.addWidget(self.txtFirstName, 0, 1, 1, 1)
        self.lblLastName = QtGui.QLabel(self.gbInitialinfo)
        self.lblLastName.setObjectName("lblLastName")
        self.lblLastName.setText("Last Name:")
        self.gridInitialInfo.addWidget(self.lblLastName, 1, 0, 1, 1)
        self.txtLastName = QtGui.QLineEdit(self.gbInitialinfo)
        self.txtLastName.setObjectName("txtLastName")
        self.gridInitialInfo.addWidget(self.txtLastName, 1, 1, 1, 1)
        self.gridMain.addWidget(self.gbInitialinfo, 2, 0, 1, 1)
        # 4. Add the Login Data group and insert it to the grid Login Data
        self.gbLoginData = QtGui.QGroupBox(self)
        self.gbLoginData.setObjectName("gbLoginData")
        self.gridLoginData = QtGui.QGridLayout(self.gbLoginData)
        self.gridLoginData.setObjectName("gridLoginData")
        self.lblUsername = QtGui.QLabel(self.gbLoginData)
        self.lblUsername.setObjectName("lblUsername")
        self.lblUsername.setText("Username:")
        self.gridLoginData.addWidget(self.lblUsername, 0, 0, 1, 1)
        self.txtUsername = QtGui.QLineEdit(self.gbLoginData)
        self.txtUsername.setObjectName("txtUsername")
        self.gridLoginData.addWidget(self.txtUsername, 0, 1, 1, 1)
        self.lblPassword = QtGui.QLabel(self.gbLoginData)
        self.lblPassword.setObjectName("lblPassword")
        self.lblPassword.setText("Password:")
        self.gridLoginData.addWidget(self.lblPassword, 1, 0, 1, 1)
        self.txtPassword = QtGui.QLineEdit(self.gbLoginData)
        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.gridLoginData.addWidget(self.txtPassword, 1, 1, 1, 1)
        self.lblPassword_2 = QtGui.QLabel(self.gbLoginData)
        self.lblPassword_2.setObjectName("lblPassword2")
        self.lblPassword_2.setText("Retype Pass:")
        self.gridLoginData.addWidget(self.lblPassword_2, 2, 0, 1, 1)
        self.txtPassword_2 = QtGui.QLineEdit(self.gbLoginData)
        self.txtPassword_2.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPassword_2.setObjectName("txtPassword_2")
        self.gridLoginData.addWidget(self.txtPassword_2, 2, 1, 1, 1)
        self.gridMain.addWidget(self.gbLoginData, 3, 0, 1, 1)
        #5. Add the Buttons Group and insert it to the Main grid
        self.gridButtons = QtGui.QGridLayout()
        self.gridButtons.setObjectName("gridButtons")
        self.btnSave = QtGui.QPushButton(self)
        self.btnSave.setObjectName("btnSave")
        self.btnSave.setText("Save")
        self.gridButtons.addWidget(self.btnSave, 0, 0, 1, 1)
        self.btnExit = QtGui.QPushButton(self)
        self.btnExit.setObjectName("btnExit")
        self.btnExit.setText("Exit")
        self.gridButtons.addWidget(self.btnExit, 0, 1, 1, 1)
        self.gridMain.addLayout(self.gridButtons, 4, 0, 1, 1)

    def setConnector(self):
        self.btnExit.clicked.connect(self.exit)
