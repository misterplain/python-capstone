import csv
import os
from config import endpoint_dict, generate_short_uuid
# from models import User
# from classAdmin import Admin
# from classCustomer import Customer


def get_admin_class():

    from classAdmin import Admin
    return Admin

def get_customer_class():
    from classCustomer import Customer
    return Customer

##read write functions
def read_from_csv(endpoint):
    """Read user data from CSV and return a list of dictionaries."""
    items = []
    try:
        with open(endpoint_dict[endpoint][0], "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                items.append(row)
    except FileNotFoundError as e:
        print(e)
        print(f"Warning: {endpoint_dict[endpoint][0]} not found. Creating a new one.")
    return items

def write_to_csv(endpoint, items, method):
    """Write user data to CSV."""
    # fieldnames = endpoint_dict[endpoint]
    file_exists = os.path.exists(endpoint_dict[endpoint][0])
    try:
        with open(endpoint_dict[endpoint][0], method, newline="") as file:
            writer = csv.DictWriter(file, fieldnames=endpoint_dict[endpoint][1])
            if not file_exists:
                writer.writeheader()
            if(method=="w"):
                writer.writeheader()
                writer.writerows(items)
            elif(method=="a"):
                writer.writerow(items) 


    except IOError:
        print(f"Error: Unable to write to {endpoint_dict[endpoint][0]}.")



def register():
    file_exists = os.path.exists("data-users.csv")
    try:
        with open("data-users.csv", "a", newline="") as file: 
            writer = csv.DictWriter(file, fieldnames=endpoint_dict["users"][1])

            if not file_exists:
                writer.writeheader()
    except IOError as e:
        print(e)
        print(f"Error: Unable to write to products.csv")

    #UNIQUE USERNAME
    while (True):
        users = read_from_csv("users")
        username = input("Username: ").strip()
        for item in users:
            if item["username"] == username:
                print("Username exists, please choose another")
                username = input("Username: ")
                continue
        break
    #PASSWORD
    password = input("Password: ").strip()
    #ISADMIN - BOOLEAN
    registerAdmin = input("isAdmin? True or False: ").strip()
    userId = generate_short_uuid()
    while(not registerAdmin == "True" and not registerAdmin == "False"):
        registerAdmin = input("isAdmin? True or False: ")
    if(registerAdmin == "True"):
        registerAdmin = True
        print("admin created")
        Class = get_admin_class()
        new_user = Class(userId, username, password, registerAdmin)
    else:
        registerAdmin = False
        print("customer created")
        Class = get_customer_class()
        new_user = Class(userId, username, password, registerAdmin)

    new_user_dict = new_user.to_dict()
    write_to_csv("users", new_user_dict, "a")
    return new_user_dict

def login():
    #READ FROM CSV FILE
    users = read_from_csv("users")
    #GET INPUT AND 
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    attempts = 0
    #WHILE ATTEMPTS < 3, CHECK FOR USERNAME AND PASSWORD
    while attempts < 3:
        for user in users:
            if user["username"] == username:
                if user["password"] == password:
                    print("Login successful!")
                    print("utils current user")
                    print(user)
                    #RETURN AS DICTIONARY
                    if(user["isAdmin"] == "True"):
                        Class = get_admin_class()
                        new_user = Class(user["userId"], user["username"], user["password"], True)
                        new_user_dict = new_user.to_dict()
                        return new_user_dict
                        
                    else:
                        Class = get_customer_class()
                        new_user = Class(user["userId"], user["username"], user["password"], False)
                        new_user_dict = new_user.to_dict()
                        return new_user_dict
                else:
                    attempts += 1
                    print(f"Password incorrect ({attempts}/3 attempts). Try again:")
                    password = input("Password: ").strip()
                    break  # Break the for-loop and retry the while-loop

        else:
            print("Username not found. Try again.")
            return None  # Username doesn't exist → return None

    print("Too many failed attempts. Returning to welcome screen.")
    return None

