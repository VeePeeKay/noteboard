# -*- coding: utf-8 -*-
import json
import random
import sqlite3
import os
from datetime import datetime

DB_PATH = "static/board.db"


class DB:
    def __init__(self):
        global DB_PATH
        self.path = DB_PATH
        if not os.path.exists(DB_PATH):
            open(DB_PATH)
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.executescript("""CREATE TABLE "boards" (
            "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "note"	INTEGER);""")
            c.executescript("""CREATE TABLE "notes" (
            "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "user"	TEXT,
            "text"	TEXT NOT NULL,
            "subnote"	INTEGER,
            "tick"	INTEGER NOT NULL,
            "date"	INTEGER);""")
            c.executescript("""CREATE TABLE "users" (
            "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "name"	TEXT NOT NULL,
            "password" TEXT NOT NULL);""")
            conn.commit()
            conn.close()

    def select(self, tableName: str, filterName: str, value):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute(f"SELECT * FROM {tableName} WHERE {filterName}=(?)", (value, ))
        data = c.fetchall()
        conn.commit()
        conn.close()
        return data

    def userExist(self, name: str, passw: str):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute(f"SELECT * FROM users WHERE name=(?) AND password=(?)", (name, passw))
        data = c.fetchall()
        conn.commit()
        conn.close()
        return data

    def userGetNotes(self, number):
        if type(number) is int:
            number = str(number)
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute(f"SELECT (notes.id) FROM notes, json_each(user) WHERE value=(?)", (number, ))
        data = c.fetchall()
        conn.commit()
        conn.close()
        return [int(i[0]) for i in data]

    def insertUser(self, name: str, passw: str):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, passw))
        number = c.execute("SELECT * FROM users WHERE name=?", (name, )).fetchall()[0][0]
        conn.commit()
        conn.close()
        return number

    def insertNote(self, text: str):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute("INSERT INTO notes (user, text, subnote, tick) VALUES (?, ?, ?, ?)", (None, text, None, 0))
        number = c.execute("SELECT * FROM notes WHERE text=?", (text, )).fetchall()[0][0]
        conn.commit()
        conn.close()
        return number

    def delete(self, tableName: str, filterName: str, value):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute(f"DELETE FROM {tableName} WHERE ?=?", (filterName, value))
        conn.commit()
        conn.close()

    def replace(self, tableName: str, filterName: str, number, new_value):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        #c.execute(f"REPLACE INTO {tableName} (id, {filterName}) VALUES (?, ?)", (number, new_value))
        c.execute(f"UPDATE {tableName} SET {filterName} = ? WHERE id=?", (new_value, number))
        conn.commit()
        conn.close()


class User:
    def __init__(self, user, passw=""):
        db = DB()
        if type(user) is str:
            name = user
            data = db.select("users", "name", name)
            print("data =", data)
            if data:
                self.number = data[0][0]
                self.name = data[0][1]
                self.password = data[0][2]
            else:
                self.number = db.insertUser(name, passw)
                self.name = name
                self.password = passw

        elif type(user) is int:
            data = db.select("users", "id", user)
            if data:
                self.number = data[0][0]
                self.name = data[0][1]
                self.password = data[0][2]
            else:
                self.number = None
                self.name = None
                self.password = None

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return str(self.number)

    def delete(self):
        db = DB()
        db.delete("names", "id", self.number)

    def getNotes(self):
        db = DB()
        ids = db.userGetNotes(self.number)
        return ids


class Note:
    def __init__(self, note, date=int(datetime.timestamp(datetime.now()))):
        self.user = []
        self.subnote = []
        db = DB()
        if type(note) is str:
            text = note
            data = db.select("notes", "text", text)
            if data:
                self.number = data[0][0]
                if data[0][1]:
                    users = json.loads(data[0][1])
                    for i in users:
                        user = User(int(i))
                        '''
                        if user.number not in selfusers:
                            print("user is not in selfusers")
                            self.user.append(user)
                        '''

                self.text = data[0][2]

                if data[0][3]:
                    subnotes = json.loads(data[0][3])
                    for i in subnotes:
                        note = Note(int(i))

                self.tick = bool(data[0][4])
                self.date = data[0][5]
            else:
                self.number = db.insertNote(text)
                self.user = []
                self.text = text
                self.subnote = []
                self.tick = False
                self.setDate(date)

        if type(note) is int:
            data = db.select("notes", "id", note)
            if data:
                self.number = data[0][0]
                if data[0][1]:
                    self.user = [User(int(i)) for i in json.loads(data[0][1])]
                else:
                    self.user = None
                self.text = data[0][2]
                if data[0][3]:
                    self.subnote = Note(data[0][3])
                else:
                    self.subnote = None
                self.tick = bool(data[0][4])
                self.date = data[0][5]

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return str(self.number)

    def setDate(self, date):
        self.date = date
        db = DB()
        db.replace("notes", "date", self.number, date)

    def addUser(self, user):
        db = DB()
        user = User(user)
        if user not in self.user:
            self.user.append(user)
        data = []
        for i in self.user:
            data.append(str(i))
        data = json.dumps(data)
        db.replace("notes", "user", self.number, data)

    def addSubnote(self, note):
        db = DB()
        note = Note(note)
        if note not in self.subnote:
            self.subnote.append(note)
        data = []
        for i in self.subnote:
            data.append(str(i))
        data = json.dumps(data)
        db.replace("notes", "subnote", self.number, data)

    def check(self, uncheck=False):
        db = DB()
        self.tick = not uncheck
        db.replace("notes", "tick", self.number, self.tick)

    def delete(self):
        db = DB()
        db.delete("notes", "id", self.number)


class Board:
    def __init__(self, board=None):
        self.note = []
        db = DB()
        if type(board) is not None:
            data = db.select("board", "id", board)
            if data:
                self.number = board
                if data[0][1]:
                    self.note.append(Note(json.dumps(data[0][1])))

    def addNote(self, note):
        db = DB()
        note = Note(note)
        if note not in self.note:
            self.note.append(note)
        data = []
        for i in self.note:
            data.append(str(i))
        data = json.dumps(data)
        db.replace("notes", "subnote", self.number, data)


if __name__ == "__main__":
    note = Note(8)
    #note.addUser(9)
    #note.setDate(datetime.datetime.timestamp(datetime.datetime.now()))
    #user = User("victorhom19")
    #print(user)
    #user = User("icen")
    #print()
    print(f"{note.number}, {note.user}, {note.subnote}, {note.tick}, {note.text}, {note.date}")
