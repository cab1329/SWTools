import mysql.connector
import sys
from user import User
from item import Item
from shopping_cart import Shopping_Cart


class Storefront:
    
    def __init__(self, inventory, users, orders):
        self.inventory = inventory
        self.users = users
        self.orders = orders

    def displayMenu(self):
        choice = True
        while choice == True:
            print("1. View all items\n2. Cart Information\n3. Account information\n")
            print("4. Logout")

            num = int(input("Please enter the number of your choice: "))

            if num == 1:
                self.checkInventory()
            else if num == 2:
                print("1. View Cart\n2.Remove item from cart\n3. Add item to cart\n")
                print("4. Add item to cart\n5. Empty cart\n6. Check out\n7. Go back\n")

                cartNum = int(input("Please enter the number of your choice: " ))

                if cartNum == 1:
                else if cartNum == 2:
                else if cartNum == 3:
                else if cartNum == 4:
                else if cartNum == 5:
                else if cartNum == 6:
                else if cartNum == 7:
                    pass
                else:
                    print("Invalid answer, returning to main menu")
            else if num == 3:
                print("1. View user information\n2. View Order history\n")
                print("3. Edit information\n4. Go back\n")

                accountNum = int(input("Please enter the number of your choice: "))

                if accountNum == 1:
                else if accountNum == 2:
                else if accountNum == 3:
                    print("1. Edit shipping address\n2. Edit username\n3. Edit password\n")
                    print("4. Edit first name\n5. Edit last name\n6. Edit phone number\n7. Go Back\n")

                    editNum == int(input("Please enter the number of your choice: "))

                    if editNum == 1:
                    else if editNum == 2:
                    else if editNum == 3:
                    else if editNum == 4:
                    else if editNum == 5:
                    else if editNum == 6:
                    else if editNum == 7:
                        pass
                    else:
                        print("Invalid answer, returning to main menu")
                else if accountNum == 4:
                    pass
                else:
                    print("Invalid answer, returning to main menu")
            else if num == 4:
                print("Thank you for shopping!")
                choice = False
            else:
                print("Invalid answer, returning to main menu")
            
            
    def checkOut(self, """whatever the cart object is called"""):

    def loadInventory(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM items")
        result = cursor.fetchall()

        self.inventory = []
        
        for x in result:
            self.inventory.append(x)

        cursor.close()
        connection.close()
        
    def checkInventory(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM items")
        result = cursor.fetchall()

        for x in result:
            print(x)

        cursor.close()
        connection.close()
        
    def loadUsers(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()

        self.users = []

        for x in result:
            self.users.append(x)

        cursor.close()
        connection.close()
            
    def loadOrders(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM orders")
        result = cursor.fetchall()

        self.orders = []

        for x in result:
            self.orders.append(x)

        cursor.close()
        connection.close()
        
    def writeOrders(self):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO orders (whatever the hell goes here idk)")
        connection.commit()

        cursor.close()
        connection.close()
        
    def writeCart(self):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO cart (whatever the hell goes here idk)")
        connection.commit()

        cursor.close()
        connection.close()

    def writeItem(self, item):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO items item")
        connection.commit()

        cursor.close()
        connection.close()
