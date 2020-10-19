# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui',
# licensing of 'about.ui' applies.
#
# Created: Mon Jan  6 11:21:21 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(474, 233)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/cool-icon-32218-Windows.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 20, 291, 21))
        self.label.setStyleSheet("font: 57 12pt \"Yu Gothic Medium\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 60, 321, 111))
        self.label_2.setStyleSheet("font: 8pt \"Segoe UI\";")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 196, 291, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 111, 131))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/cool-icon-32218.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "About", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "File Mover based on File type", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "This is a small desktop GUI application/a standalone executable which manages(moves) all the files of different file types and puts them in a folder for each file type. So it makes a new folder named based on file extension if it doesn\'t exist and moves all the files of that extension into that folder. ", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "This app is created By Siris Bajracharya (c) 2020", None, -1))

import icons_rc
