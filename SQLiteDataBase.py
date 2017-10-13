import sqlite3


class DB:
    def __init__(self):
        self.__connector = sqlite3.connect('test.db')
        self.__cursor = self.__connector.cursor()
        self.__createTables()


    def __createTables(self):
        self.__cursor.execute("CREATE TABLE StreamItem"  +
                                "ID INTEGER PRIMARY KEY,"+
                                "title TEXT,"            +
                                "description TEXT,"      +
                                "topic TEXT,"            +
                                "category TEXT,"         +
                                "content_path TEXT)")

    def insertData(self, dataTuple):
        self.__cursor.execute("INSERT INTO StreamItem VALUES (?,?,?,?,?)", dataTuple)

    def getData(self):
        self.__cursor.execute("SELECT * FROM StreamItem")
        return self.__cursor.fetchall()

