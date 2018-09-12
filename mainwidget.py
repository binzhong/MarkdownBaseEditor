#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QHBoxLayout, QVBoxLayout, QSplitter
from PyQt5.QtCore import Qt

from globalvalue import *
from textedit import TextEdit
from textbrowser import TextBrowser
from toolbar import initToolBar, ToolBar

# main window need to customize user interface, use the QWidget but the QMainWindow
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #init Text edit
        self.textEdit = TextEdit()
        #init Tool bar
        self.toolBar = ToolBar()
        initToolBar(self)
        #init textSplitter
        self.textSplitter = None

        #init layout
        self.centerVBox = QVBoxLayout()
        self.centerVBox.addWidget(self.toolBar)
        self.centerVBox.addWidget(self.textEdit)
        self.centerVBox.setSpacing(0)
        self.centerVBox.setContentsMargins(3, 0, 3, 3)
        self.setLayout(self.centerVBox)

        #init tile
        self.updateWindowTitle()
        #init position
        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(screen.width() / 4,
                         screen.height() / 6,
                         screen.width() / 2,
                         screen.height() * 2 / 3)
        self.show()
    
    def updateWindowTitle(self):
        curFileName = getCurrentFileName()
        if curFileName != STR_NULL:
            self.setWindowTitle(curFileName)
        else:
            self.setWindowTitle(SoftWareName)
    
    def togglePreviewWindow(self):
        if self.textSplitter != None and self.textBrowser.isShow():
            self.hideTextBrowser()
        else:
            self.showTextBrowser()
    
    def showTextBrowser(self):
        self.createTextSplitter()

        self.centerVBox.removeWidget(self.textEdit)
        self.centerVBox.addWidget(self.textSplitter)
        
    def hideTextBrowser(self):
        self.centerVBox.removeWidget(self.textSplitter)
        self.centerVBox.addWidget(self.textEdit)
        
    def createTextSplitter(self):
        if self.textSplitter == None:
            #create the textbrowser and splitter
            self.textBrowser = TextBrowser()
            self.textSplitter = QSplitter(Qt.Horizontal, self)

            self.textSplitter.addWidget(self.textEdit)
            self.textSplitter.addWidget(self.textBrowser)