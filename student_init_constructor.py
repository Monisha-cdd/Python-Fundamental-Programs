# Program 3: Using __init__ constructor
class Student:
    def __init__(self, fname, age, department):
        self.name = fname
        self.age = age
        self.department = department

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Department: {self.department}")

s = Student("Monisha", 19, "IT")
s.display()
