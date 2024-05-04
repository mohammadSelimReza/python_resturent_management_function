from users import Admin,Customer,Employee
from restaurent import Restaurent
from menu import Menu
from food_items import Food
from order import order

res = Restaurent("Sirajgong Awesome Hotel")
# customer interface
def customer_menu():
    name = input("Enter your name:")
    email = input("Enter your email:")
    phone = input("Enter your contact no.:")
    address = input("Enter your address:")
    customer = Customer(name=name,email=email,phone=phone,address=address)
    while True:
        print(f"Welcome {customer.name} To Our {res.name}")
        print("1. View Menu")
        print("2. Add To Cart")
        print("3. View Cart")
        print("4. Paybill")
        print("5. Exit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            customer.view_menu(res,customer)
        elif choice == 2:
            item_name = input("Enter your order:")
            item_quantity = int(input("Enter the quantity:"))
            customer.add_to_cart(restaurent=res,item_name=item_name,quantity=item_quantity)
        elif choice == 3:
            
            customer.view_cart()
        elif choice == 4:
            pass
        elif choice == 5:
            customer.cart.clear_cart()
            break
        else:
            print("Invalid option")
            print("Try to enter valid option")
            choice = int(input("Enter valid choice"))
            
# Admin interface:
def admin_menu():
    admin_name = "Selim Reza"
    admin_email = "selimreza@gmail.com"
    admin_phone = "+12345"
    admin_address = "Badda"
    
    input_admin_name = input("Enter admin name:")
    input_admin_email= input("Enter admin email:")
    input_admin_phone= input("Enter admin phone")
    input_admin_address = input("Enter admin addreess:")
    if admin_name.lower() == input_admin_name.lower() and admin_email.lower() == input_admin_email.lower() and admin_phone == input_admin_phone.lower() and admin_address.lower() == input_admin_address.lower():
        admin = Admin(name=admin_name,email=admin_email,phone=admin_phone,address=admin_address)
        print(f"{admin},Admin login successfully")
    else:
        print("Wrong Adming information")
        return
    while True:
        print("1. Add new food")
        print("2. Add new employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete item")
        print("6. Exit")
        choice = int(input("Enter Your Choice:"))
        
        if choice == 1:
            item_name = input("Enter food name:")
            item_price = int(input("Enter item's price:"))
            item_quantity = int(input("Enter item's quantity:"))
            food = Food(name=item_name,price=item_price,quantity=item_quantity)
            admin.add_new_food(restaurent=res,item=food)
        elif choice == 2:
            emp_name = input("Enter new employee's name:")
            emp_email = input("Enter new employee's email")
            emp_phone = input("Enter new employee's phone:")
            emp_address = input("Enter new employee's address:")
            emp_age = input("Enter new employee's age:")
            emp_position = input("Enter new employee's position:")
            emp_salary = input("Enter new employee's salary:")
            emp = Employee(name=emp_name,email=emp_email,phone=emp_phone,address=emp_address,age=emp_age,position=emp_position,salary=emp_salary)
            admin.add_employee(res,emp)
        elif choice == 3:
            admin.view_employee(restaurent=res)
        elif choice == 4:
            res.menu.view_menu()
        elif choice == 5:
            del_item = ("Enter item's name to remove:")
            admin.delete_item(res,del_item)
        elif choice == 6:
            break
        else:
            print("Invalid option")
            print("Try to enter valid option")
            choice = int(input("Enter valid choice"))
            
while True:
    print(f"Welcome to {res.name}")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter you choice:"))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid option")
        break