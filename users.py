from order import order
from abc import ABC
#class
class User(ABC):
    #constructor:
    def __init__(self,name,email,phone,address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        
#Admin:
class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
    def add_employee(self,restaurent,employee):
        restaurent.add_employee(employee)
    def view_employee(self,restaurent):
        restaurent.view_employee()
    def add_new_food(self,restaurent,item):
        restaurent.menu.add_to_menu(item)
    def delete_item(self,restaurent,item):
        restaurent.menu.remove_item(item)
   
#employee class:
class Employee(User):
    def __init__(self, name, email, phone, address,age,position,salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.position = position
        self.salary = salary
              
#Customer:
class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = order()
        
    def view_menu(self,restaurent,customer):
        print(f"\tWelcome to our hotel, {customer.name}")
        restaurent.menu.view_menu()
        
    def add_to_cart(self,restaurent,item_name,quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if item.quantity < quantity:
                # extra = quantity - item.quantity
                print(f"You can order max {item.quantity}")
            else:
                item.quantity = quantity
                self.cart.add_order(item)
                print(f"{item.name} added to cart")
        else:
            print(f"{item} not found")
            
    def view_cart(self):
        print("___ View Cart ____")
        print("Food Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total price: {self.cart.total_price()}")
