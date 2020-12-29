# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, uic
from model import *
import logging
from time import sleep

SignupForm, _ = uic.loadUiType("registration.ui")
WelcomeForm, _ = uic.loadUiType("welcum.ui")
MainForm, _ = uic.loadUiType("main.ui")


def alert(msg):
    error_dialog = QtWidgets.QMessageBox()
    error_dialog.setText(msg)
    error_dialog.exec_()


class WelcomeUi(QtWidgets.QDialog, WelcomeForm):
    def __init__(self):
        super(WelcomeUi, self).__init__()
        self.signup = SignupUi()
        self.setupUi(self)
        self.loginButt.clicked.connect(self.login)
        self.registrButt.clicked.connect(self.openWindowSignup)

    def openWindowSignup(self):
        #self.close()
        self.signup.exec()

    def login(self):
        db = DB()
        login = self.signEdit.text()
        passw = self.passEdit.text()
        exist = db.userExist(login, passw)
        if exist:
            self.user = User(login)
            self.mainwindow = MainUi(self.user)
            self.close()
            self.mainwindow.exec()
        else:
            alert('GOVNO LOGIN, PEREDELAY!')


class SignupUi(QtWidgets.QDialog, SignupForm):
    def __init__(self):
        super(SignupUi, self).__init__()
        self.setupUi(self)
        #self.login = WelcomeUi()
        self.finishRegButt.clicked.connect(self.signup)

    def signup(self):
        print("signup")
        db = DB()
        login = self.createLogEdit.text()
        passw = self.createPassEdit.text()
        exist = db.select("users", "name", login)

        if exist or not login.replace("_", "").isalnum():
            alert('U TEBYA SHO SHIZA? ILI PEREDOZ?')
        else:
            user = User(login, passw)
            alert('WELCUM TO THE CLUB, BUDDY (EST PROBITIE)')
            self.close()


class MainUi(QtWidgets.QDialog, MainForm):
    def __init__(self, user):
        super(MainUi, self).__init__()
        self.setupUi(self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = WelcomeUi()
    w.show()
    sys.exit(app.exec_())
