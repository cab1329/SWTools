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

store = Storefront(None, None, None, None, None)

Storefront.loadUsers()
Storefront.loadOrders()
Storefront.loadInventory()

Storefront.displayMenu()

Storefront.writeOrders()
Storefront.writeCart()
Storefront.writeItem()

connection.close
