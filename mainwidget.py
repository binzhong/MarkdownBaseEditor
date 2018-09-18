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
        self.bTextSaved = True
        self.bCursorPosChanged = False
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
        if self.bTextSaved == True:
            self.bTextSaved = False
    
    def resetTextChangedFlag(self):
        self.bTextChanged = False
    
    def isTextChanged(self):
        return self.bTextChanged
    
    def resetTextSavedFlag(self):
        self.bTextSaved = True
    
    def isTextSaved(self):
        return self.bTextSaved
    
    def cursorPosChanged(self):
        if self.bCursorPosChanged == False :
            self.bCursorPosChanged = True
    
    def resetCursorPosChangedFlag(self):
        self.bCursorPosChanged = False
    
    def isCursorPosChanged(self):
        return self.bCursorPosChanged
    
    def getPlainText(self):
        return self.textEdit.toPlainText()
    
    def setPlainText(self, data):
        self.textEdit.setPlainText(data)
    
    # Text Browser
    def togglePreviewWindow(self):
        self.setUpdatesEnabled(False)

        if self.bShowPW:
            self.hideTextBrowser()
        else:
            self.showTextBrowser()
            
        self.setUpdatesEnabled(True)
        self.update()
    
    def showTextBrowser(self):
        self.bShowPW = True
        if self.textBrowser == None:
            self.textBrowser = TextBrowser(self)
            #create the timer for flush textBrowser
            self.createTimerForRefreshTextBrowser()
            #text splitter add textbrowser
            self.textSplitter.addWidget(self.textBrowser)
            #sync the position of textedit to textbrowser
            self.textEdit.cursorPositionChanged.connect(self.cursorPosChanged)
        self.textBrowser.show()
        
    def hideTextBrowser(self):
        self.bShowPW = False
        self.timer.stop()
        self.textBrowser.hide()
        
    def createTimerForRefreshTextBrowser(self):
        if self.timer == None:
            self.timer = QTimer(self)
            self.timer.setSingleShot(False)
            self.timer.timeout.connect(self.fleshTextBrowser)
            self.timer.start(TimerInterval)
        else:
            self.timer.start()

    def fleshTextBrowser(self):
        if self.isTextChanged():
            self.setUpdatesEnabled(False)
            data = self.textEdit.toPlainText()
            self.textBrowser.setText(data)
            self.resetTextChangedFlag()
            #Avoid resync the textbrowser when user is inputting
            if self.isCursorPosChanged():
                self.syncTextBrowserPosition()
                self.resetCursorPosChangedFlag()
            self.setUpdatesEnabled(True)
        elif self.isCursorPosChanged():
            self.syncTextBrowserPosition()
            self.resetCursorPosChangedFlag()
    
    def syncTextBrowserPosition(self):
        browserSB = self.textBrowser.verticalScrollBar()
        maximum2 = browserSB.maximum()
        if maximum2 == 0: #without scrollbar
            return

        minimum2 = browserSB.minimum()
        pageStep2 = browserSB.pageStep()

        #scrollbar area
        textSB = self.textEdit.verticalScrollBar()
        maximum = textSB.maximum()
        destPos = 0
        if maximum == 0:
            pos = self.textEdit.textCursor().position()
            length = len(self.textEdit.toPlainText())
            if length == 0:
                return
            destPos = int((maximum2 - minimum2 + pageStep2)*float(pos/length) + minimum2 - float(pageStep2/2))
        else:
            curSBPos = textSB.value()
            minimum = textSB.minimum()
            pageStep = textSB.pageStep()
            #cursor position
            cursorRect = self.textEdit.cursorRect()
            yPos = cursorRect.center().y()
            #viewport's height
            vpHeight = self.textEdit.viewport().height()
            destPos = int((maximum2 - minimum2 + pageStep2)*((curSBPos + pageStep*float(yPos/vpHeight) 
            - minimum2)/(maximum - minimum + pageStep)) + minimum2 - float(pageStep2/2))
        
        #Ajust the result
        if destPos < minimum2:
            destPos = minimum2
        elif destPos > maximum2:
            destPos = maximum2
        browserSB.setValue(destPos)
        
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