import json
from Book import Book

class Files:

    @staticmethod
    def loadBook():
        book = Book()
        f = open("data.txt", "r")
        data = json.load(f)
        for entry in data:
                book.add(entry["name"], entry["phone"], entry["address"])
        f.close()
        return book
    
    @staticmethod
    def saveBook(book):
        f = open("data.txt", "w")
        data = []
        for entry in book.people:
            converted = {}
            converted["name"] = entry.name
            converted["phone"] = entry.phone
            converted["address"] = entry.address
            data.append(converted)
        json.dump(data, f)
        f.close()