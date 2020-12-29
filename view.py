# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, uic
from model import *
from time import sleep

SignupForm, _ = uic.loadUiType("registration.ui")
WelcomeForm, _ = uic.loadUiType("welcum.ui")

def alert(msg):
    error_dialog = QtWidgets.QMessageBox()
    error_dialog.setText(msg)
    error_dialog.exec_()


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
        exist = db.select("users", "name", login)

        if exist or not login.replace("_", "").isalnum():
            alert('U TEBYA SHO SHIZA? ILI PEREDOZ?')
        else:
            user = User(login, passw)
            alert('WELCUM TO THE CLUB, BUDDY (EST PROBITIE)')




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = SignupUi()
    w.show()
    sys.exit(app.exec_())
