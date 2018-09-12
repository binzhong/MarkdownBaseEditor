#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QTextBrowser

from globalvalue import *

class TextBrowser(QTextBrowser):
    def __init__(self):
        super().__init__()
        self.showFlag = False
        self.initUI()

    def initUI(self):
        pass
        