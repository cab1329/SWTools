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

else if login == False:
    print("Login Failed, exiting program")
    
Storefront.loadUsers()
Storefront.loadOrders()
Storefront.loadInventory()

Storefront.displayMenu()

Storefront.writeOrders()
Storefront.writeCart()
Storefront.writeItem()

connection.close()
