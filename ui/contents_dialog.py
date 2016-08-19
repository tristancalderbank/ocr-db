# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contents_dialogue.ui'
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

class Ui_contentsDialog(object):
    def setupUi(self, contentsDialog):
        contentsDialog.setObjectName(_fromUtf8("contentsDialog"))
        contentsDialog.resize(300, 268)
        self.verticalLayout = QtGui.QVBoxLayout(contentsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.contentsBox = QtGui.QPlainTextEdit(contentsDialog)
        self.contentsBox.setPlainText(_fromUtf8(""))
        self.contentsBox.setObjectName(_fromUtf8("contentsBox"))
        self.verticalLayout.addWidget(self.contentsBox)

        self.retranslateUi(contentsDialog)
        QtCore.QMetaObject.connectSlotsByName(contentsDialog)

    def retranslateUi(self, contentsDialog):
        contentsDialog.setWindowTitle(_translate("contentsDialog", "Contents", None))

