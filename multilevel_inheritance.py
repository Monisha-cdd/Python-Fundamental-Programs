# Program 5: Multilevel + Hierarchical Inheritance
class Grandfather:
    def asset(self):
        print("My asset is for my son (Dad)")

class Dad(Grandfather):
    def money(self):
        print("My money is for my son (Son)")

class Son(Dad):
    def card(self):
        print("My card comes from both Dad and Grandfather")

s = Son()
s.asset()
s.money()
s.card()
