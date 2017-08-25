#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from ui_login import Ui_MainWindow
import sys

# if __name__ == '__main__':
app = QtWidgets.QApplication(sys.argv)
widget =  QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(widget)
widget.show()

sys.exit(app.exec_())

