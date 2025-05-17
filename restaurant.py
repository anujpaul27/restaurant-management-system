
class Item:
    def __init__(self, name, qnt, price):
        self.name = name
        self.qnt = qnt
        self.price = price

class Restaurant:
    item_list_obj = []
    
    def add_item (self, name, qnt, price):
        self.item_list_obj.append(Item(name,qnt, price))
        print()
        print("Add Item Successfull")
    
    def show_menu (self):
        print()
        print("\t**** Item list in the restaurant ****")
        print("Name \t\t Quentity \t Price")
        for i in self.item_list_obj:
            print(f'{i.name} \t\t {i.qnt} \t\t {i.price}')
        print()
        
    def remove_item (self,name):
        for i,j in enumerate(self.item_list_obj):
            if j.name.lower() == name.lower():
                del self.item_list_obj[i]
                print()
                print(f"Remove item is name of {name}")
                return
        print()
        print("Item Not Found!.")
    



 