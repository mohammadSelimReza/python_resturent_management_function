class order:
    def __init__(self) -> None:
        self.items = {}
        
    def add_order(self,item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity
            
    def remove_oder(self,item):
        if item in self.items:
            del self.items[item]
    def total_price(self):
        return sum(item.price *quantity for item,quantity in self.items.items())
    def clear_cart(self):
        self.items = {}