from Data import Person

class Book:
    def __init__(self) -> None:
        self.people = []
        
    def add(self, name, phone, address):
        self.people.append(Person(name, phone, address))
        print("Person added.")

    def remove(self, name, phone, address):
        found = False
        for person in self.people:
            if(person.name == name and person.phone == phone and person.address == address):
                self.people.pop(self.people.index(person))
                print("Person removed.")
                found = True
                break
        if(found == False):
            print("Person not found.")

    def find(self, name, phone, address):
        found = False
        for person in self.people:
            if(person.name == name and person.phone == phone and person.address == address):
                print("Person found.")
                found = True
                break
        if(found == False):
            print("Person not found.")
    def printall(self):
        for person in self.people:
            print(person.name+" "+person.phone+" "+person.address)