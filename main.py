import mysql.connector
import sys
from user import User
from item import Item
from shopping_cart import Shopping_Cart
from StorefrontClass import Storefront

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="methods"
    )

except:
    print("Failed connection.")
    sys.exit()
username = input("Please enter username: ")
password = input("Please enter password: ")
tempUser = User(None, None, None, None, None, None, None)
login = tempUser.login(username, password)

if login == True:
    store = Storefront(None, None, None, None, None)

elif login == False:
    print("Login Failed, exiting program")
    
store.loadUsers()
store.loadOrders()
store.loadInventory()

store.setCurrUser(store.users[0].getuserID())

store.displayMenu()

store.writeOrders()
store.writeCart()
store.writeItem()

connection.close()
