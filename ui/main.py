# -*- coding: utf-8 -*-
__author__ = 'alex'
import os
from PyQt4 import QtGui
from PyQt4 import QtCore
from generics.functions import Center, SetIcon
from settings import RESOURCES_DIR
from ui.keys import AddKeyForm

class MainForm(QtGui.QMainWindow):
    def __init__(self,user):
        """
        I Build the Form with the User information
        """
        self.user = user
        super(MainForm, self).__init__()
        self.constructorUI()


    def constructorUI(self):
        self.drawUI()
        Center(self)


    def drawUI(self):
        # Nombre de la ventana
        self.setWindowTitle('Keys Python')
        # Status Bar
        message = "Welcome: %s %s" % (self.user.first_name,self.user.last_name)
        self.statusBar().showMessage(message)
        # Windows Size
        self.setMinimumSize(700,700)
        self.setGeometry(300,300,450,400)
        SetIcon(self)
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
        self.connect(addKeyAction,QtCore.SIGNAL("triggered()"),self.aTest)
        # Create a QWidget
        self.central = QtGui.QWidget(self)
        self.central.setObjectName("central")
        # Setting up to the CentralWidget
        self.setCentralWidget(self.central)
        # Start a Vertical Layout
        self.horizontal_layout = QtGui.QHBoxLayout(self.central)
        # Add List
        self.listWidget = QtGui.QListWidget()
        self.get_list_elements()
        # Add a GroupBox Element
        self.groupBox = QtGui.QGroupBox()
        self.groupBox.setTitle("Information")
        # Add the 2 elements in te horizontal Layout
        self.horizontal_layout.addWidget(self.listWidget)
        self.horizontal_layout.addWidget(self.groupBox)


    def run(self):
        self.show()

    def aTest(self):
        self.createAddForm()

    def get_exit_icon(self):
        img = "quit.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/img/%s'%img))
        return path

    def get_locked_icon(self):
        img = "lock.png"
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

    def get_list_elements(self):
        item = QtGui.QListWidgetItem()
        item.setText("Alex")
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setText("Dzul")
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setText("Cetina")
        self.listWidget.addItem(item)

    def createAddForm(self):
        self.addKey = AddKeyForm(self.user)
        self.addKey.show()

    def set_statusBar(self,message):
        self.statusBar().showMessage(message)
