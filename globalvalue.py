#!/usr/bin/python3
# -*- coding: utf-8 -*-

# About SoftWare
SoftWareName = 'GitNote'

# Tool Bar
Str_Open = 'Open'
Str_OpenDialogTitle = 'Open file'

Str_Save = 'Save'

# Icon source path
PathForOpenIcon = './resource/icon/open.ico'
PathForSaveIcon = './resource/icon/save.ico'

# Shortcut key
Shortcut_OpenFile = 'Ctrl+o'
Shortcut_SaveFile = 'Ctrl+s'

# Const String
STR_NULL = ''

# Global variable
# Main Widget
mainWidget = None

def getMainWidget():
    global mainWidget
    return mainWidget

def setMainWidget(widget):
    global mainWidget
    mainWidget = widget

# ToolBar
toolBar = None

def getToolBar():
    global toolBar
    return toolBar

def setToolBar(toolbar):
    global toolBar
    toolBar = toolbar

# TextEdit
textEdit = None

def getTextEdit():
    global textEdit
    return textEdit

def setTextEdit(textedit):
    global textEdit
    textEdit = textedit

# The current file name
curFileName = ''

def getCurrentFileName():
    global curFileName
    return curFileName

def setCurrentFileName(fileName):
    global curFileName
    curFileName = fileName
