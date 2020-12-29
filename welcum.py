# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\админ\Desktop\welcum.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(491, 422)
        Dialog.setAcceptDrops(False)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: #FF7F50")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 120, 131, 21))
        self.label.setObjectName("label")
        self.signLog = QtWidgets.QTextEdit(Dialog)
        self.signLog.setGeometry(QtCore.QRect(110, 150, 261, 31))
        self.signLog.setToolTipDuration(0)
        self.signLog.setStyleSheet("background-color:#ffa852")
        self.signLog.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.signLog.setLineWidth(0)
        self.signLog.setTabChangesFocus(False)
        self.signLog.setObjectName("signLog")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 190, 131, 21))
        self.label_2.setObjectName("label_2")
        self.signPass = QtWidgets.QTextEdit(Dialog)
        self.signPass.setGeometry(QtCore.QRect(110, 220, 261, 31))
        self.signPass.setToolTipDuration(0)
        self.signPass.setStyleSheet("background-color:#ffa852")
        self.signPass.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.signPass.setLineWidth(0)
        self.signPass.setTabChangesFocus(False)
        self.signPass.setObjectName("signPass")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 270, 261, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginButt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.loginButt.setStyleSheet(" display: inline-block;\n"
"    text-decoration: none;\n"
"    background-color: #ffa852;\n"
"    color: #006089;\n"
"    border: 3px solid #d9812f;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"    padding: 7px 10px; \n"
"    transition: all 0.8s ease;")
        self.loginButt.setDefault(False)
        self.loginButt.setObjectName("loginButt")
        self.verticalLayout.addWidget(self.loginButt)
        self.registrButt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.registrButt.setEnabled(True)
        self.registrButt.setStyleSheet("    display: inline-block;\n"
"    text-decoration: none;\n"
"    background-color: #ffa852;\n"
"    color: #006089;\n"
"    border: 3px solid #d9812f;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"    padding: 7px 8px; ;")
        self.registrButt.setIconSize(QtCore.QSize(16, 13))
        self.registrButt.setObjectName("registrButt")
        self.verticalLayout.addWidget(self.registrButt)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(110, 30, 266, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.welcome = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(24)
        self.welcome.setFont(font)
        self.welcome.setStyleSheet("text-align:center")
        self.welcome.setObjectName("welcome")
        self.verticalLayout_2.addWidget(self.welcome)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Введите логин"))
        self.signLog.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Введите пароль"))
        self.signPass.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.loginButt.setText(_translate("Dialog", "Войти"))
        self.registrButt.setText(_translate("Dialog", "Регистрация"))
        self.welcome.setText(_translate("Dialog", "Welcome to club"))