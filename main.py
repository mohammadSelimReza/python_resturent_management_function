# common class:
from abc import ABC

class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

# Employee class 
class Employee(User):
        def __init__(self, name, phone, email, address, age, designation, salary):
             super().__init__(name, phone, email, address)
             self.age = age
             self.designation = designation
             self.salary = salary


