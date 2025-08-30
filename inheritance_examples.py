# Program 4: Inheritance Example
class Dad:
    def house(self):
        print("Dad class")

class Son(Dad):
    def room(self):
        print("Son class inside Dad class")

s = Son()
s.house()
s.room()
