#!/usr/bin/python3
# -*- coding: utf-8 -*-

# About SoftWare
SoftWareName = 'GitNote'

# Tool Bar
Str_Open = 'Open'
Str_OpenDialogTitle = 'Open file'
Str_TogglePreviewWindow = 'Open/Close Preview window'

Str_Save = 'Save'

# Icon source path
PathForOpenIcon = './resource/icon/open.ico'
PathForSaveIcon = './resource/icon/save.ico'
PathForToggleIcon = './resource/icon/toggle.ico'

# Shortcut key
Shortcut_OpenFile = 'Ctrl+o'
Shortcut_SaveFile = 'Ctrl+s'
Shortcut_TogglePW = 'Ctrl+p'

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

# timer interval, msec milliseconds
TimerInterval = 1000

# The current file name
curFileName = ''

def getCurrentFileName():
    global curFileName
    return curFileName

def setCurrentFileName(fileName):
    global curFileName
    curFileName = fileName
