from restaurant import Restaurant
import copy
class Customer:
    customer_obj_llist = []
    
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.cart = []
        self.past_order = []
        self.balance = 0
        
    def view_menu (self,restaurant_obj):
        restaurant_obj.show_menu()
    
    def add_to_cart(self, name, qnt):
        for i in Restaurant.item_list_obj:
            if i.name.lower() == name:
                obj = copy.copy(i)
                i.qnt -= qnt
                obj.qnt = qnt
                self.cart.append(obj)
                print()
                print("Add to cart successful")
                return 
        print()
        print("Invalid Item Name.")
    
    def order_now(self):
        print()
        print("\t---- Seleted Item For The Order ----")
        print("Name\t\t Quentity \t Price")
        total = 0
        for i in self.cart:
            print(f'{i.name}\t\t   {i.qnt} \t\t  {i.price}')
            total+= i.qnt * i.price 
        print("--------------------------------------")
        print(f"\t\t\t Total:  {total}")
        print()
        
        if self.balance > total:
            self.balance -= total
            for i in self.cart:
                self.past_order.append(i)
                print()
            print(f"Payment {total} tk successfully done.")
        else:
            print()
            print(f'Sorry!. Your balance less than {total} tk.')
        
    # Can check available balance before placing an order.
    def check_balance (self):
        print()
        print(f"Your Balance is: {self.balance}")
        print()
    
    # Can view a list of past orders.
    def view_past_order (self):
        print()
        print("   ---- Seleted Item For The Order ----")
        print("Name\t\t Quentity \t Price")
        total = 0
        for i in self.past_order:
            print(f'{i.name}\t\t   {i.qnt} \t\t  {i.price}')
            total+= i.qnt * i.price 
        print("--------------------------------------")
        print(f"\t\t\t Total:  {total}")
        print()
    
    # Can add funds to their balance.
    def add_funds (self, ammount):
        self.balance = ammount
        print()
        print(f'Found Successfull, Now your account balance is {self.balance}')
        print()
