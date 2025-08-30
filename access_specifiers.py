# Program 7: Access Specifiers (Public, Protected, Private)

class Parent:
    def __init__(self):
        self.public = "Public member"
        self._protected = "Protected member"
        self.__private = "Private member"

    def access_from_same_class(self):
        print("Parent class:")
        print("Public:", self.public)
        print("Protected:", self._protected)
        print("Private:", self.__private)

class Child(Parent):
    def access_from_sub_class(self):
        print("Child class:")
        print("Public:", self.public)
        print("Protected:", self._protected)
        try:
            print("Private:", self.__private)   # Private not accessible directly
        except:
            print("Cannot access private member in child class")

class Stranger:
    def access_from_other_class(self, obj):
        print("Stranger class:")
        print("Public:", obj.public)
        print("Protected:", obj._protected)
        try:
            print("Private:", obj.__private)
        except:
            print("Cannot access private member in stranger class")

p = Parent()
p.access_from_same_class()
c = Child()
c.access_from_sub_class()
s = Stranger()
s.access_from_other_class(p)
