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



connection.close
