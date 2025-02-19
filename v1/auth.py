import uuid
import csv
from utils import generate_short_uuid, User
from readWrite import read_users_from_csv, write_users_to_csv


def register():
    #UNIQUE USERNAME
    while (True):
        users = read_users_from_csv("users.csv")
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
    while(not registerAdmin == "True" and not registerAdmin == "False"):
        registerAdmin = input("isAdmin? True or False: ")
    if(registerAdmin == "True"):
        registerAdmin = True
    else:
        registerAdmin = False
    #CREATE USER AND ADD TO ALL USERS
    userId = generate_short_uuid()
    new_user = User(userId, username, password, registerAdmin)
    users.append(new_user.to_dict())
    #WRITE NEW USERS FILE CSV
    write_users_to_csv("users.csv", users)
    return new_user

def login():
    #READ FROM CSV FILE
    users = read_users_from_csv("users.csv")
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
                    #RETURN AS DICTIONARY
                    return User(
                        user["userId"],
                        user["username"],
                        user["password"],
                        user["isAdmin"]
                    )
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




