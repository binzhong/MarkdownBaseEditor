#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

from PyQt5.QtWidgets import QToolBar, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon

from localelanguage import tr
from globalvalue import *
from multiencodefile import mcOpen, McFile, openWithEncoding

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
    saveFile.triggered.connect(saveCurrentFileWithoutAsk)

    togglePW = mainWidget.toolBar.addAction(tr(Str_TogglePreviewWindow))
    togglePW.setShortcut(Shortcut_TogglePW)
    togglePW.setIcon(QIcon(PathForToggleIcon))
    togglePW.triggered.connect(mainWidget.togglePreviewWindow)

    height = mainWidget.toolBar.iconSize().height()
    mainWidget.toolBar.setMaximumHeight(height)


def saveCurrentFile():
    mainWidget = getMainWidget()
    #Check the flag of text changed
    if mainWidget.isTextSaved():
        return
    mainWidget.resetTextSavedFlag()

    #If current file is valid, save it
    curFileInfo = getCurrentFileInfo()
    if curFileInfo != None:
        reply = QMessageBox.question(mainWidget, tr(Str_MessageBoxTitle), 
                tr(Str_QuestionForIfSaveFile), QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.No:
            return

        with openWithEncoding(curFileInfo.fileName,'w', curFileInfo.encoding) as file:
            data = mainWidget.getPlainText()
            file.write(data)

        return

    #Otherwise check the contents in textedit
    contents = mainWidget.getPlainText()
    if len(contents) < 1:
        return

    reply = QMessageBox.question(mainWidget, tr(Str_MessageBoxTitle), 
                tr(Str_QuestionForIfSaveFile), QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    if reply == QMessageBox.No:
        return

    #Save file dialog
    fileName = QFileDialog.getSaveFileName(mainWidget, tr(Str_SaveFileDialogTitle))
    if fileName[0]:
        with openWithEncoding(fileName[0], 'w', DefaultFileEncoding) as file:
            data = mainWidget.getPlainText()
            file.write(data)

def saveCurrentFileWithoutAsk():
    mainWidget = getMainWidget()
    #Check the flag of text changed
    if mainWidget.isTextSaved():
        return

    #If current file is valid, save it
    curFileInfo = getCurrentFileInfo()
    if curFileInfo != None:
        with openWithEncoding(curFileInfo.fileName,'w', curFileInfo.encoding) as file:
            data = mainWidget.getPlainText()
            file.write(data)
        #Reset the flag of text changed
        mainWidget.resetTextSavedFlag()
        return

    #Save file dialog
    fileName = QFileDialog.getSaveFileName(mainWidget, tr(Str_SaveFileDialogTitle))
    if fileName[0]:
        with openWithEncoding(fileName[0], 'w', DefaultFileEncoding) as file:
            data = mainWidget.getPlainText()
            file.write(data)
        mainWidget.resetTextSavedFlag()


def openFileDialog():
    # save the current file
    saveCurrentFile()

    #homePath = 'C:/Users/UserName/'
    mainWidget = getMainWidget()
    fileName = QFileDialog.getOpenFileName(mainWidget, tr(Str_OpenDialogTitle))

    if fileName[0]:
        with mcOpen(fileName[0], 'r') as mcFile:
            # backup the file infomation
            setCurrentFileInfoWithDetail(fileName[0], mcFile.encoding)

            #update the text and the title of the main window
            data = mcFile.file.read()
            mainWidget.setPlainText(data)
            mainWidget.updateWindowTitle()
            mainWidget.resetTextSavedFlag()