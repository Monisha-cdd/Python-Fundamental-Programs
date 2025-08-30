# Program 8: Encapsulation Example (Admin vs Customer View)
class Order:
    def __init__(self, name, items, amount, discount):
        self.name = name
        self.items = items
        self.__amount = amount
        self.__discount = discount

    def __calculate_final(self):
        return self.__amount - self.__discount

    def admin_view(self):
        return {
            "Customer Name": self.name,
            "Order": self.items,
            "Total Amount": self.__amount,
            "Discount": self.__discount,
            "Total Payable": self.__calculate_final()
        }

    def customer_view(self):
        return {
            "Customer Name": self.name,
            "Order": self.items,
            "Total Payable": self.__calculate_final()
        }

class Admin:
    def show_order(self, obj):
        return obj.admin_view()

class Customer:
    def show_order(self, obj):
        return obj.customer_view()

o = Order("Monisha", ["Chicken Burger", "French Fries"], 500, 150)
a = Admin()
print("Admin view:", a.show_order(o))
c = Customer()
print("Customer view:", c.show_order(o))
