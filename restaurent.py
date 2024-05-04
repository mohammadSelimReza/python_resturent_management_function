from menu import Menu
#resuarent:
class Restaurent:
    def __init__(self,name) -> None:
        self.name = name
        self.employee = [] #our local instance database
        self.menu = Menu()
        
    def add_employee(self,employee):
        self.employee.append(employee)
        # print(f"{name} is recruited")
    def view_employee(self):
        print("------ Employee List --------")
        for emp in self.employee:
            print(emp.name,emp.address)