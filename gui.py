# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        dictEng = {'0':'hello', '1':'weather', '2':'tree', '3':'car', '4':'man'}
        dictRus = {'0':'здравствуйте', '1':'погода', '2':'дерево', '3':'машина', '4':'мужчина'}
        self.Eng = dictEng
        randVar = randint(0, 4)
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 189)
        Dialog.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(160, 160, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 60, 141, 31))
        self.label.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(210, 60, 171, 31))
        self.textEdit.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.textEdit.setObjectName("textEdit")
        self.retranslateUi(Dialog)
        self.rand = randVar
        self.label.setText(dictRus[f'{randVar}'])
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
