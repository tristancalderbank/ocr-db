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
        MainWindow.resize(515, 487)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Fixedsys"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Fixedsys"))
        font.setPointSize(6)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.searchBar = QtGui.QLineEdit(self.groupBox)
        self.searchBar.setObjectName(_fromUtf8("searchBar"))
        self.verticalLayout_2.addWidget(self.searchBar)
        self.matchList = QtGui.QListWidget(self.groupBox)
        self.matchList.setObjectName(_fromUtf8("matchList"))
        self.verticalLayout_2.addWidget(self.matchList)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.directoryBar = QtGui.QLineEdit(self.groupBox_2)
        self.directoryBar.setObjectName(_fromUtf8("directoryBar"))
        self.horizontalLayout_2.addWidget(self.directoryBar)
        self.folderSelect = QtGui.QPushButton(self.groupBox_2)
        self.folderSelect.setObjectName(_fromUtf8("folderSelect"))
        self.horizontalLayout_2.addWidget(self.folderSelect)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.runOCR = QtGui.QPushButton(self.groupBox_2)
        self.runOCR.setObjectName(_fromUtf8("runOCR"))
        self.verticalLayout_3.addWidget(self.runOCR)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.radioHigh = QtGui.QRadioButton(self.groupBox_3)
        self.radioHigh.setChecked(True)
        self.radioHigh.setObjectName(_fromUtf8("radioHigh"))
        self.verticalLayout_4.addWidget(self.radioHigh)
        self.radioLow = QtGui.QRadioButton(self.groupBox_3)
        self.radioLow.setObjectName(_fromUtf8("radioLow"))
        self.verticalLayout_4.addWidget(self.radioLow)
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.checkMovingCrop = QtGui.QCheckBox(self.groupBox_3)
        self.checkMovingCrop.setObjectName(_fromUtf8("checkMovingCrop"))
        self.verticalLayout_4.addWidget(self.checkMovingCrop)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ocr-db", None))
        self.label.setText(_translate("MainWindow", "ocr-db", None))
        self.label_2.setText(_translate("MainWindow", "Created by Tristan Calderbank", None))
        self.groupBox.setTitle(_translate("MainWindow", "Search", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Scan", None))
        self.folderSelect.setText(_translate("MainWindow", "Folder", None))
        self.runOCR.setText(_translate("MainWindow", "Run OCR", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Settings", None))
        self.label_3.setText(_translate("MainWindow", "Quality", None))
        self.radioHigh.setText(_translate("MainWindow", "High (slower)", None))
        self.radioLow.setText(_translate("MainWindow", "Low (faster)", None))
        self.label_4.setText(_translate("MainWindow", "Experimental", None))
        self.checkMovingCrop.setText(_translate("MainWindow", "Enable moving crop", None))

