# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(490, 368)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.searchBar = QtGui.QLineEdit(self.centralwidget)
        self.searchBar.setObjectName(_fromUtf8("searchBar"))
        self.verticalLayout.addWidget(self.searchBar)
        self.matchList = QtGui.QListWidget(self.centralwidget)
        self.matchList.setObjectName(_fromUtf8("matchList"))
        self.verticalLayout.addWidget(self.matchList)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.directoryBar = QtGui.QLineEdit(self.centralwidget)
        self.directoryBar.setObjectName(_fromUtf8("directoryBar"))
        self.horizontalLayout.addWidget(self.directoryBar)
        self.folderSelect = QtGui.QPushButton(self.centralwidget)
        self.folderSelect.setObjectName(_fromUtf8("folderSelect"))
        self.horizontalLayout.addWidget(self.folderSelect)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.runOCR = QtGui.QPushButton(self.centralwidget)
        self.runOCR.setObjectName(_fromUtf8("runOCR"))
        self.verticalLayout.addWidget(self.runOCR)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ocr-db", None))
        self.label.setText(_translate("MainWindow", "Search", None))
        self.label_2.setText(_translate("MainWindow", "Folder", None))
        self.folderSelect.setText(_translate("MainWindow", "Browse", None))
        self.runOCR.setText(_translate("MainWindow", "Run OCR", None))

