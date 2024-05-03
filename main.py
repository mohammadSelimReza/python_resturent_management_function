#common class for Customer , Admin, Employee
#for reusable code use:
#abstract base class
from abc import ABC

#class
class User(ABC):
    #constructor:
    def __init__(self,name,email,phone,address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        
#employee class:
class Employee(User):
    def __init__(self, name, email, phone, address,age,position,salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.position = position
        self.salary = salary
        
#Admin:
class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        
        
#Customer:
class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)



#test:
emp = Employee("Sohan Sheikh","ssheikha2024@gmail.com","+8801523541698","Badda",16,"Sub worker",9000)
print(emp.name,emp.position,emp.salary)