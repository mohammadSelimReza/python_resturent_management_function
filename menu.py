#menu_list:
class Menu:
    def __init__ (self):
        self.items_list = []
        
    def add_to_menu(self,item):
        self.items_list.append(item)    
    
    def view_menu(self):
        print("-------- This is our today's menu list --------")
        print("Food Name\tPrice\tQuantity")
        for i in self.items_list:
            print(f"{i.name}\t{i.price}\t{i.quantity}")
    
    def find_item(self,item):
        for i in self.items_list:
            if i.name.lower() == item.lower():
                return i
        return None
    def remove_item(self,item):
        item = self.find_item(item)
        if item:
            self.items_list.remove(item)
        else:
            print("No item found!!!")