import mysql.connector
import sys
## attempts to connect to the database
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="methods"
    )
    print("Successful connection.")
except:
    print("Failed connection.")
    ## exits the program if unsuccessful
    sys.exit()
class User:
    
    #Constructor
    def __init__(self, firstname, lastname, address, phone, username, password, userID):
        try:
            self.firstname = str(firstname)
        except:
            print("User.firstname: An unknown error occurred.")
        try:
            self.lastname = str(lastname)
        except TypeError:
            print("User.lastname: TypeError")
        except:
            print("User.lastname: An unknown error occurred.")
        try:
            self.address = str(address)
        except TypeError:
            print("User.address: TypeError")
        except:
            print("User.address: An unknown error occurred.")
        try:
            self.phone = str(phone)
        except TypeError:
            print("User.phone: TypeError")
        except:
            print("User.phone: An unknown error occurred.")
        try:
            self.username = str(username)
        except TypeError:
            print("User.username: TypeError")
        except:
            print("User.username: An unknown error occurred.")
        try:
            self.password = str(password)
        except TypeError:
            print("User.password: TypeError")
        except:
            print("User.password: An unknown error occurred.")
        try:
            self.userID = int(userID)
        except TypeError:
            print("User.userID: TypeError")
        except:
            print("User.userID: An unknown error occurred.")

    #Destructor
    def __del__(self):

    #Setter Block
        def setUsername(self, username):
            try:
                self.username = str(username)
            except:
                print("User.setUsername: An unknown error occurred.")

    def setPassword(self, password):
        try:
            self.password = str(password)
        except TypeError:
            print("User.setPassword: TypeError")
        except:
            print("User.setPassword: An unknown error occurred.")

    def setFirstname(self, firstname):
        try:
            self.firstname = str(firstname)
        except:
            print("User.setFirstname: An unknown error occurred.")
            
    def setLastname(self, lastname):
        try:
            self.lastname = str(lastname)
        except:
            print("User.setLastname: An unknown error occurred.")
   
    def setAddress(self, address):
        try:
            self.address = str(address)
        except TypeError:
            print("User.setAddress: TypeError")
        except:
            print("User.setAddress: An unknown error occurred.")
    def setPhone(self, phone):
        try:
            self.phone = str(phone)
        except TypeError:
            print("User.setPhone: TypeError")
        except:
            print("User.setPhone: An unknown error occurred.")
    def setUID(self, userID):
        try:
            self.UID = int(userID)
        except TypeError:
            print("User.setUID: TypeError")
        except:
            print("User.setUID: An unknown error occurred.")


    #Getter Block
    def getFirstname(self):
        return self.firstname
    
    def getUsername(self):
        return self.username
   
    def getLastname(self):
        return self.lastname
    
    def getPassword(self):
        return self.password
    
    def getPhone(self):
        return self.phone

    def getAddress(self):
        return self.address

    def getUID(self):
        return self.userID
    #Login
    def login(self,username,password):
        cursor = connection.cursor()
        cursor.execute('SELECT UserName FROM user WHERE UserName == username')
        test1= cursor.fetchone()
        if (test1 == username)
            cursor.execute('SELECT Password FROM user WHERE UserName == test1')
            test2= cursor.fetchone()
            if (test2==password)
                print("login succesful")
                cursor.close()
                return True
            else print("login failed")
                cursor.close()
                return False
        elseprint("login failed")
            cursor.close()
            return False
    #Display
    def display():
        print(firstname, lastname, address, phone, username, password, cartID, userID)
