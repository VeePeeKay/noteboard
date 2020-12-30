# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDateTime

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
        self.user = user
        self.ExitButt.clicked.connect(self.toLogin)
        self.all_dates = {}
        self.updateData()
        self.addEventButt.clicked.connect(self.find_date)
        self.clearButt.clicked.connect(self.clearNotes)

    def updateData(self):
        notes = [Note(i) for i in self.user.getNotes()]
        print(notes)
        self.textBrowser.clear()
        self.all_dates = {}
        for note in notes:
            dt = datetime.fromtimestamp(note.date)
            string_date = QDateTime(dt.date(), dt.time()).date().getDate()
            print(string_date)
            if int(string_date[1]) <= 9:
                string_date = (string_date[0], '0' + str(string_date[1]), string_date[-1])
            if int(string_date[2]) <= 9:
                string_date = (string_date[0], str(string_date[1]), '0' + str(string_date[-1]))
            line_edit = note.text
            self.all_dates[
                f'{string_date[0]}-{string_date[1]}-{string_date[2]}-{dt.time()}'] = line_edit
            self.textBrowser.clear()
            for key in sorted(self.all_dates.keys()):
                self.textBrowser.append(f'{key} - {self.all_dates[key]}')

    def find_date(self):
        string_date = self.calendarWidget.selectedDate().getDate()
        if int(string_date[1]) <= 9:
            string_date = (string_date[0], '0' + str(string_date[1]), string_date[-1])
        if int(string_date[2]) <= 9:
            string_date = (string_date[0], str(string_date[1]), '0' + str(string_date[-1]))
        line_edit = self.WriteEdit.text()
        self.all_dates[
            f'{string_date[0]}-{string_date[1]}-{string_date[2]}-{self.timeEdit.time().toString()}'] = line_edit
        self.textBrowser.clear()
        for key in sorted(self.all_dates.keys()):
            self.textBrowser.append(f'{key} - {self.all_dates[key]}')

        dt = QDateTime(self.calendarWidget.selectedDate(), self.timeEdit.time())
        note = Note(self.WriteEdit.text(), dt.toTime_t())
        note.addUser(self.user.number)

    def clearNotes(self):
        notes = [Note(i) for i in self.user.getNotes()]
        for note in notes:
            print(note)
            note.delUser(self.user.number)
        self.updateData()

    def toLogin(self):
        self.welcome = WelcomeUi()
        self.close()
        self.welcome.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = WelcomeUi()
    w.show()
    sys.exit(app.exec_())
