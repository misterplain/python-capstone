
import uuid
import csv
import json
import os
from utils import Order
from auth import register, login
from admin import list_all_products, add_new_product, edit_product, delete_product, view_orders, view_orders_range

current_user = None

def logout():
    global current_user
    current_user = None

def display_auth_menu():
    print("Log in or sign up")
    print("1 - Log in")
    print("2 - Sign up")

def display_customer_menu():
    print("Choose action as customer")
    print("1 - List all products")

def display_admin_menu():
    print("Choose action as admin")
    print("1 - List all products")
    print("2 - Add new product")
    print("3 - Edit individual product")
    print("4 - Delete individual product")
    print("5 - View all orders")
    print("6 - View orders within X days")
    print("7 - LOGOUT")

while True:
    ##nobody is logged in
    while (current_user == None):
        display_auth_menu()
        command = input("Command: ")
        if(command == "1"):
            current_user = login()
        elif(command == "2"):
            current_user = register()
        else:
            print("not a valid reply, choose 1 to login or 2 to sign up")


    ##somebody is logged in but isAdmin is false
    while (current_user and current_user.isAdmin == False):
        print(f"Customer LOGGED IN - Username: {current_user.username} ({current_user.userId}, Admin: {current_user.isAdmin})")
        display_customer_menu()

    ## somebody is logged in but isAdmin is true
    while (current_user and current_user.isAdmin == True):
        print(f"Admin LOGGED IN - Username: {current_user.username} ({current_user.userId}, Admin: {current_user.isAdmin})")
        display_admin_menu()

        command = input("Select number from menu: ")
        if command.lower() == "1":
            list_all_products()
        elif command.lower() == "2":
            add_new_product()
        elif command.lower() == "3":
            edit_product()
        elif command.lower() == "4":
            delete_product()
        elif command.lower() == "5":
            view_orders()
        elif command.lower() == "6":
            view_orders_range()
        elif command.lower() == "7":
            logout()
        else:
            print("Not a valid command. Please try again.\n")






# test_order = Order("100", "200", "March 1", [[3, "test", 65], [4, "test2", 66]])
# # print(test_order)
# dict = test_order.to_dict()
# # print(dict)

# fieldnames = ["orderId", "userId", "datePlaced", "items"]
# file_exists = os.path.exists("orders.csv")
# try:
#     with open("orders.csv", "a", newline="") as file: 
#         writer = csv.DictWriter(file, fieldnames=fieldnames)

#     if not file_exists:
#         writer.writeheader()
#     print(dict)
#     writer.writerow(dict) 
# except IOError as e:
#         print(e)
#         print(f"Error: Unable to write to products.csv")


# class Order:
#     def __init__(self, orderId, userId, datePlaced, items):
#         self.orderId = orderId
#         self.userId = userId
#         self.datePlaced = datePlaced
#         self.items = items

#     def to_dict(self):
#         """Convert Order object to dictionary for main order CSV writing."""
#         return {
#             "orderId": self.orderId,
#             "userId": self.userId,
#             "datePlaced": self.datePlaced
#         }

#     def items_to_dicts(self):
#         """Convert Order items to list of dictionaries for items CSV writing."""
#         return [{"orderId": self.orderId, "itemId": item[0], "description": item[1], "quantity": item[2]} for item in self.items]

# # Example usage
# order = Order('100', '200', 'March 1', [[3, 'test', 65], [4, 'test2', 66]])

# # Convert to dictionary for main orders CSV
# main_order_dict = order.to_dict()

# # Convert items to dictionaries for order items CSV
# items_dicts = order.items_to_dicts()

# # Writing to CSV
# import csv

# # Main orders CSV
# with open('main_orders.csv', 'w', newline='') as csvfile:
#     fieldnames = main_order_dict.keys()
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     writer.writeheader()
#     writer.writerow(main_order_dict)

# # Order items CSV
# with open('order_items.csv', 'w', newline='') as csvfile:
#     fieldnames = ["orderId", "itemId", "description", "quantity"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     writer.writeheader()
#     writer.writerows(items_dicts)
