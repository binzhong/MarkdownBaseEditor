#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QTextBrowser

from globalvalue import *

class TextBrowser(QTextBrowser):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.showFlag = False
        self.initUI()

    def initUI(self):
        pass
        