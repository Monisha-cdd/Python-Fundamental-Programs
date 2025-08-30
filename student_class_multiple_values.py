# Program 2: Class with multiple attributes and methods
class Student:
    def details(self, fname, age, department):
        self.name = fname
        self.age = age
        self.department = department

    def display(self):
        print("Name:", self.name, "Age:", self.age, "Department:", self.department)

s = Student()
s.details("Monisha", 19, "IT")
s.display()
