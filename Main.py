#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QToolTip
from PyQt5.QtGui import QFont

from globalvalue import setMainWidget, DefaultFontList, DefaultFontSize, DefaultFontSizeForToolTip
from mainwidget import MainWidget

import sys
from localelanguage import initLocale


if __name__ == '__main__':

    #init locale
    initLocale()

    app = QApplication(sys.argv)
    #Try to init font with default font list
    for fontName in DefaultFontList:
        font = QFont(fontName, DefaultFontSize)
        if font.exactMatch():
            app.setFont(font)
            tipFont = QFont(fontName, DefaultFontSizeForToolTip)
            QToolTip.setFont(tipFont)
            break

    mainWidget = MainWidget()
    setMainWidget(mainWidget)

    sys.exit(app.exec_())