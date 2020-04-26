# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GRE_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Frame)
        self.centralwidget.setObjectName("centralwidget")
        self.word = QtWidgets.QLabel(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(200, 80, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.word.setFont(font)
        self.word.setAlignment(QtCore.Qt.AlignCenter)
        self.word.setObjectName("word")
        self.explain = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.explain.setGeometry(QtCore.QRect(100, 150, 600, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.explain.setFont(font)
        self.explain.setReadOnly(True)
        self.explain.setObjectName("explain")
        self.showButton = QtWidgets.QPushButton(self.centralwidget)
        self.showButton.setGeometry(QtCore.QRect(100, 480, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.showButton.setFont(font)
        self.showButton.setObjectName("showButton")
        self.coverButton = QtWidgets.QPushButton(self.centralwidget)
        self.coverButton.setGeometry(QtCore.QRect(350, 480, 100, 30))
        self.coverButton.setObjectName("coverButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(600, 480, 100, 30))
        self.nextButton.setObjectName("nextButton")
        self.count = QtWidgets.QLabel(self.centralwidget)
        self.count.setGeometry(QtCore.QRect(350, 530, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.count.setFont(font)
        self.count.setObjectName("count")
        self.shiftButton = QtWidgets.QPushButton(self.centralwidget)
        self.shiftButton.setGeometry(QtCore.QRect(100, 30, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.shiftButton.setFont(font)
        self.shiftButton.setObjectName("shiftButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 30, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        Frame.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Frame)
        self.statusbar.setObjectName("statusbar")
        Frame.setStatusBar(self.statusbar)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "GRE_Helper"))
        self.word.setText(_translate("Frame", "TextLabel"))
        self.showButton.setText(_translate("Frame", "Show"))
        self.coverButton.setText(_translate("Frame", "Cover"))
        self.nextButton.setText(_translate("Frame", "Next"))
        self.count.setText(_translate("Frame", "Count:"))
        self.shiftButton.setText(_translate("Frame", "ShiftMode"))
        self.label.setText(_translate("Frame", "Random Evil Mode"))
