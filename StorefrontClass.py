import mysql.connector
import sys
from user import User
from item import Item
from shopping_cart import Shopping_Cart


class Storefront:
    
    def __init__(self, inventory = Shopping_Cart("store", "permanent", None), users = [], orders = [], cart = Shopping_Cart(), currentUser = "0" ):
        self.inventory = inventory
        self.users = users
        self.orders = orders
        self.cart = cart
        self.currentUser = currentUser

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
                print("4. Empty cart\n5. Check out\n6. Modify quantity of item in cart\n7. Go back\n")

                cartNum = int(input("Please enter the number of your choice: " ))

                if cartNum == 1:
                    self.cart.result_cart() 
                else if cartNum == 2:
                    print("Which item would you like to remove?\n")
                    self.cart.result_cart()
                    itemID = int(input("Please enter the item ID of the item you would like to remove: "))
                    itemFound == False
                    for x in self.cart:
                        tempItem = self.cart(x)
                        if itemID == tempItem.getID():
                            itemFound = True

                    if itemFound == False:
                        print("Item not found, please try again.\n")

                    else if itemFound == True:
                        self.cart.removeItem(itemID)
                        print("Item removed from cart.\n")

                    else:
                        print("An error has occured, returning to main menu\n")
                            
                else if cartNum == 3:
                    print("Which item would you like to add?\n")
                    self.inventory.result_cart()
                    itemID = int(input("Please enter the item ID of the item you would like to add: "))
                    itemFound == False
                    for x in self.inventory:
                        tempItem = self.inventory(x)
                        if itemID == tempItem.getID():
                            itemFound = True
                            itemIndex = x

                    if itemFound == False:
                        print("Item not found, please try again.\n")

                    else if itemFound == True:
                        itemQuantity = int(input("Please enter the quantity you would like to order: "))
                        if itemQuantity > 0:
                            tempItem = self.inventory(itemIndex)
                            if tempItem.getQuantity() <= itemQuantity:
                                self.cart.addItem(itemID, itemQuantity)
                                print("Item has been added to cart\n")

                            else if tempItem.getQuantity() > itemQuantity:
                                print("Item cannot be added to cart because the quantity you want to exceeds the quantity in stock\n")

                            else:
                                print("An error has occured, returning to main menu\n")

                        else if itemQuantity < 1:
                            print("The item quantity cannot be zero or negative\n")

                        else:
                            print("An error has occured, returning to main menu\n")
                        
                    else:
                        print("An error has occured, returning to main menu\n")
                    
                else if cartNum == 4:
                    self.cart.clearCart()
                else if cartNum == 5:
                    self.checkout()
                else if cartNum == 6:
                    self.cart.modifyItem()
                else if cartNum == 7:
                    pass
                else:
                    print("Invalid answer, returning to main menu")
            else if num == 3:
                print("1. View user information\n2. View Order history\n")
                print("3. Edit information\n4. Go back\n")

                accountNum = int(input("Please enter the number of your choice: "))

                if accountNum == 1:
                    currentUser.display()
                else if accountNum == 2:
                    for x in orders:
                        #displaying orders, figure out later 
                else if accountNum == 3:
                    print("1. Edit shipping address\n2. Edit username\n3. Edit password\n")
                    print("4. Edit first name\n5. Edit last name\n6. Edit phone number\n7. Go Back\n")

                    editNum == int(input("Please enter the number of your choice: "))

                    if editNum == 1:
                        editAddress = input("Enter your new address: ")
                        self.currentUser.setAddress(editAddress)
                    else if editNum == 2:
                        editUsername = input("Enter your new username: ")
                        self.currentUser.setUsername(editUsername)
                    else if editNum == 3:
                        editPassword = input("Enter your new password: ")
                        self.currentUser.setPassword(editPassword)
                    else if editNum == 4:
                        editFirst = input("Enter your new first name: ")
                        self.currentUser.setFirstname(editFirst)
                    else if editNum == 5:
                        editLast = input("Enter your new last name: ")
                        self.currentUser.setLastname(editLast)
                    else if editNum == 6:
                        editNumber = input("Enter your new phone number: ")
                        self.currentUser.setPhone(editNumber)
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
            
            
    def checkOut(self):
        self.cart.result_cart()
        print("Total: $", self.cart.get_valuecost_of_cart(), "\n")
        checkout = input("Would you like to check out? y/n: ")
        if checkout == y:
            #none of these save to anything on purpose, this can be changed if you want to
            input("Please enter your card number: ")
            input("Please enter the expiration: ")
            input("Please enter the CVV: ")

            addressCheck = input("Is this address correct?\n", self.currentUser.getAddress(), "\n y/n: ")

            if addressCheck == y:
                self.orders.append(self.cart)
                self.cart.clear()
                print("Order has been placed, thank you for ordering!\n")

            else if addressCheck == n:
                print("Please edit your address in the Edit information tab and try again.")

            else:
                print("Invalid Answer, returning to main menu")

        else if checkout == n:
            pass
        else:
            print("Invalid Answer, returning to main menu")

    def loadInventory(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM items")
        result = cursor.fetchall()

        self.inventory = []
        
        for x in result:
            self.inventory.addItem()

        cursor.close()
        
    def checkInventory(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM items")
        result = cursor.fetchall()

        for x in result:
            print(x)

        cursor.close()
        
    def loadUsers(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()

        self.users = []

        for x in result:
            self.users.append(x)

        cursor.close()
            
    def loadOrders(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM orders")
        result = cursor.fetchall()

        self.orders = []

        for x in result:
            self.orders.append(x)

        cursor.close()
        
    def writeOrders(self):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO orders (whatever the hell goes here idk)")
        connection.commit()

        cursor.close()
        
    def writeCart(self):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO cart (whatever the hell goes here idk)")
        connection.commit()

        cursor.close()

    def writeItem(self, item):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO items item")
        connection.commit()

        cursor.close()

    def setCurrUser(self, userID):
        self.currentUser = userID
