import mysql.connector
from Book import Book

class DB:
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="addressbook"
        )
        self.mycursor = self.mydb.cursor()

    def loadBook(self):
        book = Book()
        sql = "SELECT * FROM people"
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        for row in myresult:
            book.add(row[0], str(row[1]), row[2])
        return book
    
    def saveEntry(self, name, phone, address):
        sql = "INSERT INTO people (name, phone, address) VALUES (%s, %s, %s)"
        val = (name, phone, address)
        self.mycursor.execute(sql, val)
        self.mydb.commit()