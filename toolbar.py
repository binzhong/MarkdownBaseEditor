#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

from PyQt5.QtWidgets import QToolBar, QAction, QFileDialog
from PyQt5.QtGui import QIcon

from localelanguage import tr
from globalvalue import *

class ToolBar(QToolBar):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setMovable(False)
        self.setFloatable(False)


def initToolBar(mainWidget):
    openFile = mainWidget.toolBar.addAction(tr(Str_Open))
    openFile.setShortcut(Shortcut_OpenFile)
    openFile.setIcon(QIcon(PathForOpenIcon))
    openFile.triggered.connect(openFileDialog)

    saveFile = mainWidget.toolBar.addAction(tr(Str_Save))
    saveFile.setShortcut(Shortcut_SaveFile)
    saveFile.setIcon(QIcon(PathForSaveIcon))
    saveFile.triggered.connect(saveCurrentFile)

    togglePW = mainWidget.toolBar.addAction(tr(Str_TogglePreviewWindow))
    togglePW.setShortcut(Shortcut_TogglePW)
    togglePW.setIcon(QIcon(PathForToggleIcon))
    togglePW.triggered.connect(mainWidget.togglePreviewWindow)

    height = mainWidget.toolBar.iconSize().height()
    mainWidget.toolBar.setMaximumHeight(height)


def saveCurrentFile():
    curFileName = getCurrentFileName()

    if curFileName != STR_NULL:
        file = open(curFileName,'w')

        with file:
            data = getMainWidget().textEdit.toPlainText()
            file.write(data)

def openFileDialog():
    #homePath = 'C:/Users/UserName/'
    fileName = QFileDialog.getOpenFileName(getMainWidget(), tr(Str_OpenDialogTitle))

    if fileName[0]:
        file = open(fileName[0], 'r')
        with file:
            # save the current file
            saveCurrentFile()

            # backup the current file name
            setCurrentFileName(fileName[0])

            #update the text and the title of the main window
            data = file.read()
            getMainWidget().textEdit.setText(data)
            getMainWidget().updateWindowTitle()