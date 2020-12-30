# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDateTime

from model import *

SignupForm, _ = uic.loadUiType("view/registration.ui")
WelcomeForm, _ = uic.loadUiType("view/login.ui")
MainForm, _ = uic.loadUiType("view/main.ui")
AddForm, _ = uic.loadUiType("view/add.ui")


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
            alert('Неправильный логин или пароль')


class SignupUi(QtWidgets.QDialog, SignupForm):
    def __init__(self):
        super(SignupUi, self).__init__()
        self.setupUi(self)
        #self.login = WelcomeUi()
        self.finishRegButt.clicked.connect(self.signup)

    def signup(self):
        db = DB()
        login = self.createLogEdit.text()
        passw = self.createPassEdit.text()
        exist = db.select("users", "name", login)

        if exist:
            alert("Пользователь с таким именем уже существует")
        elif not login.replace("_", "").isalnum():
            alert("Имя пользователя должно состоять только из цифр, букв латинского алфавита и нижнего подчёркивания")
        else:
            user = User(login, passw)
            alert("Вы успешно зарегистрировались")
            self.close()


class AddUi(QtWidgets.QDialog, AddForm):
    def __init__(self):
        super(AddUi, self).__init__()
        self.setupUi(self)
        self.cancelButt.clicked.connect(self.close)
        self.addFriendButt.clicked.connect(self.addFriend)

    def addFriend(self):
        db = DB()
        note = int(self.idSearch.text())
        user = self.loginSearch.text()
        user_exist = db.select("users", "name", user)
        note_exist = db.select("notes", "id", note)
        if not user_exist:
            alert("Пользователь не найден")
        elif not note_exist:
            alert("Заметка с таким id не найдена")
        else:
            note = Note(note)
            note.addUser(user)
            alert(f"Пользователь {user} успешно добавлен к заметке \"{note.text}\"")
            self.close()


class MainUi(QtWidgets.QDialog, MainForm):
    def __init__(self, user):
        super(MainUi, self).__init__()
        self.setupUi(self)
        self.addUi = AddUi()
        self.user = user
        self.ExitButt.clicked.connect(self.toLogin)
        self.all_dates = {}
        self.updateData()
        self.addEventButt.clicked.connect(self.find_date)
        self.clearButt.clicked.connect(self.clearNotes)
        self.addRememberButt.clicked.connect(self.addUser)

    def addUser(self):
        self.addUi.exec()

    def updateData(self):
        notes = [Note(i) for i in self.user.getNotes()]
        self.textBrowser.clear()
        self.all_dates = {}
        for note in notes:
            dt = datetime.fromtimestamp(note.date)
            string_date = QDateTime(dt.date(), dt.time()).date().getDate()
            if int(string_date[1]) <= 9:
                string_date = (string_date[0], '0' + str(string_date[1]), string_date[-1])
            if int(string_date[2]) <= 9:
                string_date = (string_date[0], str(string_date[1]), '0' + str(string_date[-1]))
            line_edit = note.text
            self.all_dates[
                f'id:{note.number}\n{string_date[2]}-{string_date[1]}-{string_date[0]}-{dt.time()}'] = line_edit+"\n"
            self.textBrowser.clear()
            for key in sorted(self.all_dates.keys()):
                self.textBrowser.append(f'{key} - {self.all_dates[key]}')

    def find_date(self):
        dt = QDateTime(self.calendarWidget.selectedDate(), self.timeEdit.time())
        note = Note(self.WriteEdit.text(), dt.toTime_t())
        note.addUser(self.user.number)
        self.updateData()

    def clearNotes(self):
        notes = [Note(i) for i in self.user.getNotes()]
        for note in notes:
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
