# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, uic
from model import *

Form, _ = uic.loadUiType("welcum.ui")


class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.loginButt.clicked.connect(self.login)

    def login(self):
        db = DB()
        login = self.signLog.toPlainText()
        print(login)
        exist = bool(db.select("users", "name", login))
        print(exist)
        if exist:
            user = User(login)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec_())
