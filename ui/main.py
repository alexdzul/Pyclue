# -*- coding: utf-8 -*-
__author__ = 'alex'
import sys
import os
from PyQt4 import QtGui
from PyQt4.QtCore import Qt
from generics.functions import Center, SetIcon
from settings import RESOURCES_DIR

class MainForm(QtGui.QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.constructorUI()


    def constructorUI(self):
        self.drawUI()
        Center(self)


    def drawUI(self):
        # Nombre de la ventana
        self.setWindowTitle('Keys Python')
        # Status Bar
        self.statusBar().showMessage('By: Alex Dzul')
        # Windows Size
        self.setMinimumSize(700,700)
        self.setGeometry(300,300,450,400)
        SetIcon(self)
        # Add the Exit Button
        exitAction = QtGui.QAction(QtGui.QIcon(self.get_exit_icon()),'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)
        # Add the Add Button
        addAction = QtGui.QAction(QtGui.QIcon(self.get_add_icon()),'Add Key',self)
        addAction.setShortcut('Ctrl+A')
        # Add the Settings Button
        settingsAction = QtGui.QAction(QtGui.QIcon(self.get_settings_icon()),'Settings',self)
        settingsAction.setShortcut('Ctrl+S')
        # Create toolBar Element
        self.toolBar = self.addToolBar('Main')
        # Add the elements to the toolBar
        self.toolBar.addAction(addAction)
        self.toolBar.addAction(settingsAction)
        self.toolBar.addAction(exitAction)
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


    def get_exit_icon(self):
        img = "quit.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/img/%s'%img))
        return path

    def get_add_icon(self):
        img = "key_add.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/img/%s'%img))
        print path
        return path

    def get_settings_icon(self):
        img = "settings.png"
        path =  os.path.abspath(os.path.join(RESOURCES_DIR,'main/img/%s'%img))
        print path
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
