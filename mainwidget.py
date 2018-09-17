#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QHBoxLayout, QVBoxLayout, QSplitter, QSizePolicy
from PyQt5.QtCore import Qt, QTimer

from globalvalue import *
from textedit import TextEdit
from textbrowser import TextBrowser
from toolbar import initToolBar, ToolBar, saveCurrentFile


# main window need to customize user interface, use the QWidget but the QMainWindow
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #init Text edit
        self.textEdit = TextEdit(self)
        self.textEdit.textChanged.connect(self.textChanged)
        self.bTextChanged = False
        #init Tool bar
        self.toolBar = ToolBar(self)
        initToolBar(self)
        #init textSplitter
        self.textSplitter = QSplitter(Qt.Horizontal, self)
        self.textSplitter.addWidget(self.textEdit)
        #init textBrowser
        self.bShowPW = False
        self.textBrowser = None
        #init timer
        self.timer = None

        #init layout
        self.centerVBox = QVBoxLayout()
        self.centerVBox.addWidget(self.textSplitter)
        self.centerVBox.addWidget(self.toolBar)
        self.centerVBox.setSpacing(0)
        self.centerVBox.setContentsMargins(0, 0, 0, 0)
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
    
    # Text Edit   
    def textChanged(self):
        if self.bTextChanged == False:
            self.bTextChanged = True
    
    def resetTextChangedFlag(self):
        self.bTextChanged = False
    
    def isTextChanged(self):
        return self.bTextChanged
    
    def getPlainText(self):
        return self.textEdit.toPlainText()
    
    def setPlainText(self, data):
        self.textEdit.setPlainText(data)
        self.resetTextChangedFlag()
    
    # Text Browser
    def togglePreviewWindow(self):
        self.setUpdatesEnabled(False)

        if self.textBrowser != None and self.bShowPW:
            self.hideTextBrowser()
        else:
            self.showTextBrowser()
            
        self.setUpdatesEnabled(True)
        self.update()
    
    def showTextBrowser(self):
        self.bShowPW = True
        self.createTextBrowser()
        self.textBrowser.show()
        
    def hideTextBrowser(self):
        self.bShowPW = False
        self.timer.stop()
        self.textBrowser.hide()
        
    def createTextBrowser(self):
        if self.textBrowser == None:
            #create the textbrowser and splitter
            self.textBrowser = TextBrowser(self)
            #create the timer for flush textBrowser
            self.createTimerForRefreshTextBrowser()

        #text splitter add textbrowser
        self.textSplitter.addWidget(self.textBrowser)
    
    def createTimerForRefreshTextBrowser(self):
        if self.timer == None:
            self.timer = QTimer(self)
            self.timer.setSingleShot(False)
            self.timer.timeout.connect(self.fleshTextBrowser)
            self.timer.start(TimerInterval)
        else:
            self.timer.start()

    def fleshTextBrowser(self):
        data = self.textEdit.toPlainText()
        self.textBrowser.setText(data)
        
    # main widget 
    def updateWindowTitle(self):
        curFileName = getCurrentFileName()
        if curFileName != STR_NULL:
            self.setWindowTitle(curFileName)
        else:
            self.setWindowTitle(SoftWareName)
    
    def closeEvent(self, event):
        saveCurrentFile()
        event.accept()