from Book import Book
from Files import Files
from DB import DB

#set to False for file handling
useDB = True

if(useDB):
    db = DB()
    book = db.loadBook()
else:
    book = Files.loadBook()

while True:
    print("(1) Add Person\n(2) Remove Person\n(3) Find Person\n(4) Print All\n(5) Quit \n\n")
    
    choice = input("Enter your choice:")

    if(choice == '1'):
        name = input("Enter name:")
        
        phone = input("Enter phone:")
        
        address = input("Enter address:")
        
        book.add(name, phone, address)

        if(useDB):
            db.saveEntry(name, phone, address)
    elif(choice == '2'):
        name = input("Enter name:")
        
        phone = input("Enter phone:")
        
        address = input("Enter address:")
        
        book.remove(name, phone, address)
    elif(choice == '3'):
        name = input("Enter name:")
        
        phone = input("Enter phone:")
        
        address = input("Enter address:")
        
        book.find(name, phone, address)
    elif(choice == '4'):
        book.printall()
    elif(choice == '5'):
        print("Quitting...\n")
        if(useDB):
            pass
        else:
            book = Files.loadBook()
        break
    else:
        print("Invalid Choice.\n")