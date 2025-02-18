
import uuid
import csv
import json
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






       