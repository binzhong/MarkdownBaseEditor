#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication

from globalvalue import setMainWidget
from mainwidget import MainWidget

import sys


if __name__ == '__main__':

    app = QApplication(sys.argv)

    mainWidget = MainWidget()
    setMainWidget(mainWidget)

    # catch the : SystemExit
    try:
        sys.exit(app.exec_())
    except SystemExit:
        pass