#!/usr/bin/python3
# -*- coding: utf-8 -*-

# About SoftWare
SoftWareName = 'GitNote'
DefaultFontList = [ 
    'Microsoft YaHei UI',
    '微软雅黑',
    '宋体'
]
DefaultFontSize = 12
DefaultFontSizeForToolTip = 8
DefaultFileEncoding = 'utf-8'

# Tool Bar
Str_Save = 'Save'
Str_Open = 'Open'
Str_OpenDialogTitle = 'Open file'
Str_TogglePreviewWindow = 'Open/Close Preview window'

# Some Dialog
Str_MessageBoxTitle = 'Message'
Str_QuestionForIfSaveFile = "The current file's constents is changed, do you want to save it?"
Str_SaveFileDialogTitle = 'Save file'


# Icon source path
PathForOpenIcon = './resource/icon/open.bmp'
PathForSaveIcon = './resource/icon/save.bmp'
PathForToggleIcon = './resource/icon/toggle.bmp'

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

# The current file infomation
class FileInfo():
    def __init__(self, fileName, encoding = DefaultFileEncoding):
        # It is important class, don't allow invalid value
        assert(fileName != '' and fileName != None)

        self.fileName = fileName
        self.encoding = encoding

curFileInfo = None

def getCurrentFileName():
    global curFileInfo
    if curFileInfo == None:
        return STR_NULL
    else:
        return curFileInfo.fileName

def getCurrentFileInfo():
    global curFileInfo
    return curFileInfo

def setCurrentFileInfo(fileInfo):
    # It is an important value, don't allow invalid value
    assert(fileInfo != None)

    global curFileInfo
    curFileInfo = fileInfo

def setCurrentFileInfoWithDetail(fileName, encoding):
    # It is an important value, don't allow invalid value
    assert(fileName != STR_NULL and fileName != None)
    assert(encoding != STR_NULL and encoding != None)

    global curFileInfo
    
    if curFileInfo == None:
        curFileInfo = FileInfo(fileName, encoding)
    else:
        curFileInfo.fileName = fileName
        curFileInfo.encoding = encoding