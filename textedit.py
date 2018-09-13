#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QTextEdit

class TextEdit(QTextEdit):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUI()
    
    def initUI(self):
        #set font
        #set boder
        pass

    def setText(self, text):
        super().setPlainText(text)