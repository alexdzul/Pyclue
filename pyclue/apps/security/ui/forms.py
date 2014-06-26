'''
Created on 26/06/2014

@author: edzul
'''
from PyQt4 import QtGui
from PyQt4 import QtCore
from pyclue.apps.main.ui.forms import MainForm
from pyclue.ui.generics.functions import Center, SetIcon
from pyclue.apps.security.functions import decode_password
from pyclue.apps.settings.functions import get_settings
from pyclue.apps.security.ui.ui_sizes import get_login_size
from pyclue.apps.security.ui.resources_mapper import get_login_icon, get_quit_icon


class LoginForm(QtGui.QWidget):

    def __init__(self):
        super(LoginForm,self).__init__()
        self.constructorUI()

    def constructorUI(self):
        self.drawUI() # Draw de UI elements
        self.setTextElements() # Set titles and text to the elements
        Center(self) # Center the form
        SetIcon(self) # Set a Main Icon
        self.setConnectors() # Set Connectors to the Buttons
        self.setFocusOrder() # Set elements order

    def run(self):
        self.show()

    def exit(self):
        QtCore.QCoreApplication.instance().quit()


    def validateCredential(self):
        my_password = self.txtMasterPassword.text()
        settings = get_settings()
        if settings:
            if decode_password(settings.user_password) == my_password:
                self.createMain(settings)
            else:
                self.alert("Error","Incorrect password")
                self.txtMasterPassword.setFocus()
        else:
            self.alert("Error","Error reading the main settings")
            self.txtMasterPassword.setFocus()


    def createMain(self,settings):
        loginForm = self
        self.main = MainForm(settings, loginForm)
        self.txtMasterPassword.setText("")
        self.hide()
        self.main.run()

    def alert(self, title,  mensaje):
        QtGui.QMessageBox.about(self, title, mensaje)

    def setConnectors(self):
        self.btnExit.clicked.connect(self.exit)
        self.btnLogin.clicked.connect(self.validateCredential)
        self.txtMasterPassword.returnPressed.connect(self.btnLogin.click)

    def setFocusOrder(self):
        self.setTabOrder(self.txtMasterPassword, self.btnLogin)
        self.setTabOrder(self.btnLogin, self.btnExit)

    def drawUI(self):
        self.setObjectName("loginForm")
        self.setWindowTitle("Login PyClue")
        self.setWindowModality(QtCore.Qt.NonModal)
        get_login_size(self)
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayoutPassword = QtGui.QHBoxLayout()
        self.horizontalLayoutPassword.setObjectName("horizontalLayoutPassword")
        self.lblMasterPassword = QtGui.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblMasterPassword.setFont(font)
        self.lblMasterPassword.setObjectName("lblMasterPassword")
        self.horizontalLayoutPassword.addWidget(self.lblMasterPassword)
        self.txtMasterPassword = QtGui.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.txtMasterPassword.setFont(font)
        self.txtMasterPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.txtMasterPassword.setObjectName("txtMasterPassword")
        self.horizontalLayoutPassword.addWidget(self.txtMasterPassword)
        self.gridLayout.addLayout(self.horizontalLayoutPassword, 0, 0, 1, 1)
        self.horizontalLayoutButtons = QtGui.QHBoxLayout()
        self.horizontalLayoutButtons.setObjectName("horizontalLayoutButtons")
        self.btnLogin = QtGui.QPushButton(self)
        self.btnLogin.setMinimumSize(QtCore.QSize(0, 0))
        self.btnLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        iconLogin = QtGui.QIcon()
        iconLogin.addPixmap(QtGui.QPixmap(get_login_icon()), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogin.setIcon(iconLogin)
        self.btnLogin.setIconSize(QtCore.QSize(40, 40))
        self.btnLogin.setObjectName("btnLogin")
        self.horizontalLayoutButtons.addWidget(self.btnLogin)
        self.btnExit = QtGui.QPushButton(self)
        self.btnExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        iconExit = QtGui.QIcon()
        iconExit.addPixmap(QtGui.QPixmap(get_quit_icon()), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(iconExit)
        self.btnExit.setIconSize(QtCore.QSize(40, 40))
        self.btnExit.setObjectName("btnExit")
        self.horizontalLayoutButtons.addWidget(self.btnExit)
        self.gridLayout.addLayout(self.horizontalLayoutButtons, 1, 0, 1, 1)

    def setTextElements(self):
        self.lblMasterPassword.setText("Password")
        self.setWindowTitle("Login")
        self.btnExit.setText("Exit")
        self.btnLogin.setText("Login")
