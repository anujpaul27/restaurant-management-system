from restaurant import Restaurant
from customer import Customer
class Admin:
    
    def add_item (self,restaurant_obj, name, qnt, price):
        restaurant_obj.add_item(name,qnt,price)
        
    def view_menu (self,restaurant_obj):
        restaurant_obj.show_menu()
    
    def add_customer(self, name, email, address):
        Customer.customer_obj_llist.append(Customer(name,email,address))

    def view_customer_details (self):
        print()
        print("\t\t----- Registrared Customer Details -----")
        print("Name\t\t\tEmail\t\t\t\tAddress")
        for i in Customer.customer_obj_llist:
            print(f'{i.name}\t\t\t{i.email}\t\t\t{i.address}')
        print()
    
    def remove_customer_account(self, name):
        for i,j in enumerate(Customer.customer_obj_llist):
            if j.name.lower() == name.lower():
                del Customer.customer_obj_llist[i]
                print()
                print(f"Remove Customer account is name of {name}")
                return
        print()
        print("Not Found Customer!.")
    
    def remove_item(self,restaurant_obj,name):
        restaurant_obj.remove_item(name)
    
    # Update Price 
    def update_price(self,restaurant_obj, name, ammount ):
        for i in restaurant_obj.item_list_obj:
            if i.name.lower() == name.lower():
                i.price = ammount
                print()
                print(f"Price Update, Name of the item is {name}")
                return
        print()
        print("Not found, Item!.")
     
