from admin import Admin
from customer import Customer
from restaurant import Restaurant

admin = Admin()
res = Restaurant()

option = None
while (option != 0):
    print("1. Admin Pannel")
    print("2. Restaurant pannel")
    print("3. Customer log in")
    print("0. Exit") 
    option = int (input ('Enter Your Choice: '))

    if option == 1:
        opt1 = None
        while (opt1 != 0):
            print()
            print("1. Add Item")
            print("2. View Menu")
            print("3. Remove Item")
            print("4. Update Item Price")
            print("5. Add Customer")
            print("6. View All Customer Account")
            print("7. Remove Customer Account")
            print("0. Exit")
            opt1 = int(input ("Enter Your Choice: "))

            if opt1 == 1:
                name = input("Enter Item Name: ")
                qnt = int (input ('Enter Item Quentity: '))
                price = int (input("Enter Item Price: "))
                admin.add_item(res,name,qnt,price)
            
            elif opt1 == 2:
                admin.view_menu(res)

            elif opt1 == 3:
                name = input ("Enter Item Name: ")
                admin.remove_item(res,name)
                
            elif opt1 == 4:
                name = input ('Enter item name for the update price: ')
                price = int (input ("Enter Update price: "))
                admin.update_price(res,name,price)
                
            elif opt1 == 5:
                name = input ('Enter Customer Name: ')
                email = input ("Enter Customer Email: ")
                address = input ("Enter Customer Address: ")
                admin.add_customer(name,email,address)
            
            elif opt1 == 6:
                admin.view_customer_details()
            
            elif opt1 == 7:
                name = input ('Enter Removed Customer Name: ')
                admin.remove_customer_account(name)

    elif option == 2:
        opt2 = None
        while (opt2 != 0):
            print("1. Add Item")
            print("2. View Menu")
            print("3. Remove Item")
            print("4. View Customer")
            print("0. Exit")
            opt2 = int(input ('Enter Choice: '))
            
            if opt2 == 1:
                name = input("Enter Item Name: ")
                qnt = int (input ('Enter Item Quentity: '))
                price = int (input("Enter Item Price: "))
                admin.add_item(res,name,qnt,price)
            
            elif opt2 == 2:
                admin.view_menu(res)

            elif opt2 == 3:
                name = input ("Enter Item Name: ")
                admin.remove_item(res,name)
            
            elif opt2 == 4:
                admin.view_customer_details()
        
    elif option == 3:
        log_in = False
        print()
        print("----- Welcome to customer Pannel -----")
        print()
        name = input('Please Enter Your name: ')
        email = input("Please Enter Your Email: ")
        
        val = None
        for j,i in enumerate(Customer.customer_obj_llist):
            if i.name.lower() == name.lower() and i.email == email:
                log_in = True
                val = j        
            
        if log_in == True:
            opt3 = None
            while (opt3 != 0):
                print("1. View Menu")
                print("2. Add cart")
                print("3. Order Now")
                print("4. Check Past Order")
                print("5. Check balance")
                print("6. Add Funds to balance")
                print("0. Exit")
                opt3 = int(input ('Enter Choice: '))

                if opt3 == 1:
                    admin.view_menu(res)
                
                elif opt3 == 2:
                    name = input("Enter Item name: ")
                    qnt = int (input("Enter Qnt: "))
                    Customer.customer_obj_llist[val].add_to_cart(name,qnt)
                
                elif opt3 == 3:
                    Customer.customer_obj_llist[val].order_now()
                
                elif opt3 == 4:
                    Customer.customer_obj_llist[val].view_past_order()
                    
                elif opt3 == 5:
                    Customer.customer_obj_llist[val].check_balance()
                    
                elif opt3 == 6:
                    ammount = int (input ("Enter Ammount: "))
                    Customer.customer_obj_llist[val].add_funds(ammount)
                                 
        else :
            print("Log in faild!.")
                            
            
        