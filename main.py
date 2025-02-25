from utils import login, register
from classAdmin import Admin
from classCustomer import Customer
import datetime

dates = []

for x in range(10):
    date = datetime.datetime.now()
    new_time = date - datetime.timedelta(days=x)
    dates.append(new_time)

print("full list of dates")
print(dates)
print()

dates_within = []

for x in dates:
    comparison_date = datetime.datetime.now() - datetime.timedelta(days=2)
    if x > comparison_date:
        dates_within.append(x)

print("within 4 days")
print(dates_within)
print()

# def testDate(time):
#     date = datetime.datetime.now()
#     previous_time = date - datetime.timedelta(days=time)
#     print(date)
#     print(previous_time)
#     test = date - previous_time
#     print(test)

#     if test.days > time:
#         print("greater")
#     else:
#         print("less")

# testDate(8)

# current_user = None
# def insert_break():
#     print("\n------------------------------------------\n")

# def logout():
#     global current_user
#     current_user = None
#     insert_break()
    
# def display_header():
#     if current_user:
#         print(f'Welcome, {current_user["username"]} (ID: {current_user["userId"]}, Admin: {current_user["isAdmin"]})')
#         print()

# def format_products(products):
#     insert_break()
#     print(f"Products: ")
#     for product in products:
#         print(f'ID: {product["productId"]} ({product["stock"]} in stock) - ${product["price"]} - {product["name"]}')
#     insert_break()

# def format_cart_items(cart_items):
#     insert_break()
#     print(f"Cart items: ")
#     if len(cart_items) == 0:
#         print("No items in cart")
#     for item in cart_items:
#         print(f'ID: {item["productId"]} ({item["quantity"]} x ${item["price"]} = ${int(item["quantity"]) * int(item["price"])})  {item["name"]}')
#     insert_break()

# def format_orders(orders):
#     insert_break()
#     print(f"Orders: ")
#     for order in orders:
#         print(f'Order ID: {order["orderId"]},  User ID: {order["userId"]},  Total Price: ${order["totalPrice"]}, Date placed: {order["datePlaced"]}')
#     insert_break()

# def format_individual_orders(order_details, order):
#     insert_break()
#     print(f'Order ID: {order["orderId"]},  User ID: {order["userId"]},  Total Price: ${order["totalPrice"]}, Date placed: {order["datePlaced"]}')
#     for item in order_details:
#         print(f'ID: {item["productId"]} ({item["quantity"]} x ${item["price"]} = ${int(item["quantity"]) * int(item["price"])})  {item["name"]}')
#     insert_break()

# def display_auth_menu():
#     print("Welcome to the online store!")
#     print("Log in or sign up\n")
#     print("1 - Log in")
#     print("2 - Sign up\n")

# def display_customer_menu():
#     print("Choose action as customer")
#     print("1 - List all products")
#     print("2 - Show my cart")
#     print("3 - Add item to cart")
#     print("4 - Remove item from cart")
#     print("5 - Place order")
#     print("6 - View previous orders")
#     print("7 - View previous orders within X days")
#     print("8 - View order details")
#     print("9 - LOGOUT")

# def display_admin_menu():
#     print("Choose action as admin")
#     print("1 - List all products")
#     print("2 - Add new product")
#     print("3 - Edit individual product")
#     print("4 - Delete individual product")
#     print("5 - View all orders")
#     print("6 - View orders within X days")
#     print("7 - View order details")
#     print("8 - LOGOUT")

# while True:
#     ##LOGIN/REGISTER
#     while (current_user == None):
#         display_auth_menu()
#         command = input("Command: ")
#         if(command == "1"):
#             current_user = login()
#             insert_break()
#         elif(command == "2"):
#             current_user = register()
#             insert_break()
#         else:
#             print("not a valid reply, choose 1 to login or 2 to sign up")

#     ##CUSTOMER
#     while (current_user and current_user["isAdmin"] == False):
#         display_header()
#         display_customer_menu()
#         command = input("Select number from menu: ")
#         if command.lower() == "1":
#             format_products(current_user.list_all_products())
#         elif command.lower() == "2":
#             format_cart_items(current_user.list_user_cart())
#         elif command.lower() == "3":
#             format_products(current_user.list_all_products())
#             current_user.add_item_to_cart()
#             format_cart_items(current_user.list_user_cart())
#         elif command.lower() == "4":
#             format_cart_items(current_user.list_user_cart())
#             current_user.remove_item_from_cart()
#             format_cart_items(current_user.list_user_cart())
#         elif command.lower() == "5":
#             current_user.place_order()
#         elif command.lower() == "6":
#             format_orders(current_user.list_user_orders())
#         elif command.lower() == "7":
#             print("x")
#         elif command.lower() == "8":
#             ##get individual order
#             format_orders(current_user.list_user_orders())
#             individual_order = current_user.get_individual_order()
#             format_individual_orders(current_user.list_order_items(individual_order), individual_order)
#         elif command.lower() == "9":
#             logout()
            
#         else:
#             print("Not a valid command. Please try again.\n")

#     ## ADMIN
#     while (current_user and current_user["isAdmin"] == True):
#         display_header()
#         display_admin_menu()
#         command = input("Select number from menu: ")
#         if command.lower() == "1":
#             format_products(current_user.list_all_products())
#         elif command.lower() == "2":
#             current_user.add_new_product()
#             format_products(current_user.list_all_products())      
#         elif command.lower() == "3":
#             #edit product
#             format_products(current_user.list_all_products())
#             current_user.edit_product()
#             format_products(current_user.list_all_products()) 
#         elif command.lower() == "4":
#             format_products(current_user.list_all_products())
#             current_user.delete_product()
#             format_products(current_user.list_all_products()) 
#         elif command.lower() == "5":
#             #view orders
#             format_orders(current_user.list_all_orders())
#         # elif command.lower() == "6":
#         #     #view orders within range
#         elif command.lower() == "8":
#             logout()
#         else:
#             print("Not a valid command. Please try again.\n")
