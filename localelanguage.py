#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import locale

def tr(s):
    global language
    global langDict

    #default language or ont in langDict, return the original string
    if language < 0 or not (s in langDict):
        return s
    else:
        return langDict[s][language]

def initLocale():
    global language
    global langList

    localeLang , encoding = locale.getdefaultlocale()

    language = -1
    for lang in langList:
        language = language + 1
        if localeLang == lang:
            break
    else:
        language = -1

language = -1
#default is en_US
langList = ['zh_CN']
# language dict
langDict = {
    # english chinese
    'Open':['打开'],
    'Save':['保存'],
    'Open/Close Preview window':[
        '打开/关闭 预览'
    ]
}