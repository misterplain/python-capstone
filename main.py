
import uuid
loggedIn = False
isAdmin = False
userId = ""
users = [["uuid", "patrick", "password", False], ["uuid2", "patrick2", "password2", False]]

class User:
    def __init__(self, name, password, isAdmin):
        self.name = name
        self.password = password
        self.isAdmin = isAdmin

class Admin(User):
    def __init__ (self, name, password, isAdmin):
        super().__init__(name, password, isAdmin)

class Customer(User):
    def __init__ (self, name, password, isAdmin):
        super().__init__(name, password, isAdmin)

    def testItem(self):
        print(self.name)
        print(self.password)
        print(self.isAdmin)


def display_login_menu():
    print("Welcome!")
    print()
    print("Choose 1 to login or 2 to sign up")
    print()

display_login_menu()

def generate_short_uuid():
    return str(uuid.uuid4())[:8]

def register():
    username = input("Username: ")
    password = input("Password: ")
    registerAdmin = input("isAdmin? True or False: ")
    global isAdmin
    while(not registerAdmin == "True" and not registerAdmin == "False"):
        registerAdmin = input("isAdmin? True or False: ")
    if(registerAdmin == "True"):
        registerAdmin = True
        isAdmin = True
    else:
        registerAdmin = False
        isAdmin = False
    userIdSlug = generate_short_uuid()
    global loggedIn
    global userId
    userId = userIdSlug
    loggedIn = True
    users.append([userIdSlug, username, password, isAdmin])

def login():
    username = input("Username: ")
    password = input("Password: ")
    global users 
    global loggedIn
    global isAdmin
    global userId
    attempts = 0


    while(not loggedIn):
        ## both correct
        for user in users:
            ##both correct
            if(username == user[1] and password == user[2]):
                print("login successful")
                loggedIn = True
                userId = user[0]
                isAdmin = user[3]
                break
            ##username found, password incorrect
            elif (username==user[1] and not password == user[2]):
                attempts = attempts + 1
                if(attempts >=3):
                    return 0
                print("Password incorrect, please try again. At 3 attempts, you'll be sent to welcome screen")
                password = input("Password: ")
                continue



##nobody is logged in
while (loggedIn == False):
    authType = input("Command: ")
    if((authType) == "1"):
        print("trigger login function")
        login()
    elif((authType) == "2"):
        print("trigger register function")
        register()
    else:
        print("not a valid reply, choose 1 to login or 2 to sign up")

print(users)
print(loggedIn)
print(isAdmin)
print(userId)

##somebody is logged in but isAdmin is false
while (loggedIn == True and isAdmin == False):
    print("logged in as customer")
    exit()

## somebody is logged in but isAdmin is true
while (loggedIn == True and isAdmin == True):
    print("logged in as admin")
    exit()




       