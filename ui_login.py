# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\broadcast\broadcast\login.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(450, 700)
        MainWindow.setMinimumSize(QtCore.QSize(450, 700))
        MainWindow.setMaximumSize(QtCore.QSize(450, 700))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.bg_title = QtWidgets.QLabel(self.centralWidget)
        self.bg_title.setGeometry(QtCore.QRect(0, 0, 450, 700))
        self.bg_title.setMinimumSize(QtCore.QSize(450, 700))
        self.bg_title.setMaximumSize(QtCore.QSize(450, 700))
        self.bg_title.setText("")
        self.bg_title.setTextFormat(QtCore.Qt.AutoText)
        self.bg_title.setPixmap(QtGui.QPixmap("loginbg.jpg"))
        self.bg_title.setObjectName("bg_title")
        self.username = QtWidgets.QLineEdit(self.centralWidget)
        self.username.setGeometry(QtCore.QRect(70, 350, 310, 70))
        self.username.setMinimumSize(QtCore.QSize(310, 70))
        self.username.setMaximumSize(QtCore.QSize(310, 70))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(95, 95, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 95, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.username.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralWidget)
        self.password.setGeometry(QtCore.QRect(70, 420, 310, 70))
        self.password.setMinimumSize(QtCore.QSize(310, 70))
        self.password.setMaximumSize(QtCore.QSize(310, 70))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 95, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 95, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.password.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.submit = QtWidgets.QPushButton(self.centralWidget)
        self.submit.setGeometry(QtCore.QRect(70, 490, 310, 70))
        self.submit.setMinimumSize(QtCore.QSize(310, 70))
        self.submit.setMaximumSize(QtCore.QSize(310, 70))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.submit.setFont(font)
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit.setStyleSheet("background-color: rgb(35, 93, 169);\n"
"border: none;\n"
"selection-background-color: rgb(6, 161, 224);\n"
"color: rgb(255, 255, 255);")
        self.submit.setObjectName("submit")
        self.reminder = QtWidgets.QLabel(self.centralWidget)
        self.reminder.setEnabled(True)
        self.reminder.setGeometry(QtCore.QRect(70, 570, 300, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(95, 95, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 95, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.reminder.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.reminder.setFont(font)
        self.reminder.setObjectName("reminder")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.username.setText(_translate("MainWindow", "请输入用户名"))
        self.password.setText(_translate("MainWindow", "请输入密码"))
        self.submit.setText(_translate("MainWindow", "登  录"))
        self.reminder.setText(_translate("MainWindow", "用户名或密码错误"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    myshow = Ui_MainWindow()
    myshow.setupUi(window)
    window.show()
    sys.exit(app.exec_())
