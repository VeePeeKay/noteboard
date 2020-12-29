# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, uic
from model import *
from time import sleep

SignupForm, _ = uic.loadUiType("registration.ui")
WelcomeForm, _ = uic.loadUiType("welcum.ui")


class WelcomeUi(QtWidgets.QDialog, WelcomeForm):
    def __init__(self):
        super(WelcomeUi, self).__init__()
        self.setupUi(self)
        self.loginButt.clicked.connect(self.login)

    def login(self):
        db = DB()
        login = self.signEdit.text()
        passw = self.passEdit.text()
        exist = db.userExist(login, passw)
        if exist:
            user = User(login)
            print(user)
        else:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('GOVNO LOGIN, PEREDELAY!')
            error_dialog.exec_()


class SignupUi(QtWidgets.QDialog, SignupForm):
    def __init__(self):
        super(SignupUi, self).__init__()
        self.setupUi(self)
        self.finishRegButt.clicked.connect(self.signup)

    def signup(self):
        db = DB()
        login = self.createLogEdit.text()
        passw = self.createPassEdit.text()
        exist = db.userExist(login, passw)
        if exist:
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('U TEBYA SHO SHIZA? ILI PEREDOZ?')
            error_dialog.exec_()
        else:
            user = User(login, passw)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = SignupUi()
    w.show()
    sys.exit(app.exec_())
