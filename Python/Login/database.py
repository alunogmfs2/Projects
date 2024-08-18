import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self) -> None:
        pass
    
    def connectToDatabase(self) -> sqlite3.Connection:
        try:
            conn = sqlite3.connect('dados.db')
            return conn
        except Error as e:
            print(e)

    def query(self, conn: sqlite3.Connection, sql: str, data=None) -> None:
        try:
            cursor = conn.cursor()
            print("Pronto")
            cursor.execute(sql, data)
            conn.commit()
        except Error as e:
            print(e)

    def get(self, conn: sqlite3.Connection) -> list:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dados")
            return cursor.fetchall()
        except Error as e:
            print(e)
