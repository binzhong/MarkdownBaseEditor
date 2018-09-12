#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, \
                            QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon

from globalvalue import *
from textedit import TextEdit
from toolbar import initToolBar, ToolBar

import sys

# main window need to customize user interface, use the QWidget but the QMainWindow
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #init Text edit
        setTextEdit(TextEdit())
        #init Tool bar
        setToolBar(ToolBar())
        initToolBar()

        #init layout
        vBox = QVBoxLayout()
        vBox.addWidget(getToolBar())
        vBox.addWidget(getTextEdit())
        self.setLayout(vBox)

        #init tile
        self.updateWindowTitle()
        #init position
        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(screen.width() / 4,
                         screen.height() / 6,
                         screen.width() / 2,
                         screen.height() * 2 / 3)
        self.show()
    
    def updateWindowTitle(self):
        curFileName = getCurrentFileName()
        if curFileName != STR_NULL:
            self.setWindowTitle(curFileName)
        else:
            self.setWindowTitle(SoftWareName)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    mainWidget = MainWidget()
    setMainWidget(mainWidget)

    # catch the : SystemExit
    try:
        sys.exit(app.exec_())
    except SystemExit:
        pass