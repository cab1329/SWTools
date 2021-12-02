#postgres variant main
import psycopg2  
import psycopg2.extras
import sys
from user import User
from item import Item
from shopping_cart import Shopping_Cart
from StorefrontClass import Storefront

conn = None
try:
    conn = psycopg2.connect(user="postgres",  # same as pgAdmin
                            password="123",  # same as pgAdmin
                            host="127.0.0.1",
                            database="SWTools")  # same as the name of the 
                                                 # company database in pgAdmin
    
except psycopg2.Error as err:
    print("PostgreSQL Error: %s" % err.args[0])
    print()
    sys.exit(-1)

username = input("Please enter username: ")
password = input("Please enter password: ")
tempUser = User(None, None, None, None, None, None, None, None)
login = tempUser.login(username, password)

if login == True:
    store = Storefront(None, None, None, None, None)

elif login == False:
    print("Login Failed, exiting program")
    
Storefront.loadUsers()
Storefront.loadOrders()
Storefront.loadInventory()

Storefront.displayMenu()

Storefront.writeOrders()
Storefront.writeCart()
Storefront.writeItem()

conn.close()
