#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

from PyQt5.QtWidgets import QToolBar, QAction, QFileDialog
from PyQt5.QtGui import QIcon

from globalvalue import *

class ToolBar(QToolBar):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setMovable(False)
        self.setFloatable(False)


def initToolBar():
    openFile = getToolBar().addAction(Str_Open)
    openFile.setShortcut(Shortcut_OpenFile)
    openFile.setIcon(QIcon(PathForOpenIcon))
    openFile.triggered.connect(openFileDialog)

    saveFile = getToolBar().addAction(Str_Save)
    saveFile.setShortcut(Shortcut_SaveFile)
    saveFile.setIcon(QIcon(PathForSaveIcon))
    saveFile.triggered.connect(saveCurrentFile)
    

def saveCurrentFile():
    curFileName = getCurrentFileName()

    if curFileName != STR_NULL:
        file = open(curFileName,'w')

        with file:
            data = getTextEdit().toPlainText()
            file.write(data)

def openFileDialog():
    import Main

    #homePath = 'C:/Users/UserName/'
    fileName = QFileDialog.getOpenFileName(getMainWidget(), Str_OpenDialogTitle)

    if fileName[0]:
        file = open(fileName[0], 'r')
        with file:
            # save the current file
            saveCurrentFile()

            # backup the current file name
            setCurrentFileName(fileName[0])

            #update the text and the title of the main window
            data = file.read()
            getTextEdit().setText(data)
            getMainWidget().updateWindowTitle()
    


