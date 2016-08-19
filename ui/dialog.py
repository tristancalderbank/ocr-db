# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogue.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(500, 185)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(500, 185))
        Dialog.setMaximumSize(QtCore.QSize(500, 185))
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.currentTask = QtGui.QLabel(Dialog)
        self.currentTask.setAlignment(QtCore.Qt.AlignCenter)
        self.currentTask.setObjectName(_fromUtf8("currentTask"))
        self.verticalLayout.addWidget(self.currentTask)
        self.currentFile = QtGui.QLabel(Dialog)
        self.currentFile.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.currentFile.setObjectName(_fromUtf8("currentFile"))
        self.verticalLayout.addWidget(self.currentFile)
        self.filesProcessed = QtGui.QLabel(Dialog)
        self.filesProcessed.setObjectName(_fromUtf8("filesProcessed"))
        self.verticalLayout.addWidget(self.filesProcessed)
        self.elapsedTime = QtGui.QLabel(Dialog)
        self.elapsedTime.setObjectName(_fromUtf8("elapsedTime"))
        self.verticalLayout.addWidget(self.elapsedTime)
        self.timeRemaining = QtGui.QLabel(Dialog)
        self.timeRemaining.setObjectName(_fromUtf8("timeRemaining"))
        self.verticalLayout.addWidget(self.timeRemaining)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.stopButton = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        self.stopButton.setMinimumSize(QtCore.QSize(0, 30))
        self.stopButton.setMaximumSize(QtCore.QSize(200, 200))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout.addWidget(self.stopButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Running OCR", None))
        self.currentTask.setText(_translate("Dialog", "converting to tiff...", None))
        self.currentFile.setText(_translate("Dialog", "Current File:", None))
        self.filesProcessed.setText(_translate("Dialog", "Files Processed: ", None))
        self.elapsedTime.setText(_translate("Dialog", "Elapsed Time:", None))
        self.timeRemaining.setText(_translate("Dialog", "Estimated Remaining:", None))
        self.stopButton.setText(_translate("Dialog", "Stop OCR", None))

