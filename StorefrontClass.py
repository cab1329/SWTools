#postgres variant
import psycopg2  
import psycopg2.extras
import sys
from user import User
from item import Item
from shopping_cart import Shopping_Cart


class Storefront:
    
    def __init__(self, inventory = Shopping_Cart(0, "permanent", None, 0), users = [], orders = [], cart = Shopping_Cart(1, "Today", None, 0), currentUser = "0" ):
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
            elif num == 2:
                print("1. View Cart\n2.Remove item from cart\n3. Add item to cart\n")
                print("4. Empty cart\n5. Check out\n6. Modify quantity of item in cart\n7. Go back\n")

                cartNum = int(input("Please enter the number of your choice: " ))

                if cartNum == 1:
                    self.cart.result_cart() 
                elif cartNum == 2:
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

                    elif itemFound == True:
                        self.cart.removeItem(itemID)
                        print("Item removed from cart.\n")

                    else:
                        print("An error has occured, returning to main menu\n")
                            
                elif cartNum == 3:
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

                    elif itemFound == True:
                        itemQuantity = int(input("Please enter the quantity you would like to order: "))
                        if itemQuantity > 0:
                            tempItem = self.inventory(itemIndex)
                            if tempItem.getQuantity() <= itemQuantity:
                                self.cart.addItem(itemID, itemQuantity)
                                print("Item has been added to cart\n")

                            elif tempItem.getQuantity() > itemQuantity:
                                print("Item cannot be added to cart because the quantity you want to exceeds the quantity in stock\n")

                            else:
                                print("An error has occured, returning to main menu\n")

                        elif itemQuantity < 1:
                            print("The item quantity cannot be zero or negative\n")

                        else:
                            print("An error has occured, returning to main menu\n")
                        
                    else:
                        print("An error has occured, returning to main menu\n")
                    
                elif cartNum == 4:
                    self.cart.clearCart()
                elif cartNum == 5:
                    self.checkout()
                elif cartNum == 6:
                    self.cart.modifyItem()
                elif cartNum == 7:
                    pass
                else:
                    print("Invalid answer, returning to main menu")
            elif num == 3:
                print("1. View user information\n2. View Order history\n")
                print("3. Edit information\n4.Delete Account\n5. Go back\n")

                accountNum = int(input("Please enter the number of your choice: "))

                if accountNum == 1:
                    currentUser.display()
                elif accountNum == 2:
                    for x in orders:
                        pass
                        #displaying orders, figure out later 
                elif accountNum == 3:
                    print("1. Edit shipping address\n2. Edit username\n3. Edit password\n4. Edit first name\n5. Edit last name\n6. Edit phone number\n7. Go Back\n")

                    editNum == int(input("Please enter the number of your choice: "))

                    if editNum == 1:
                        editAddress = input("Enter your new address: ")
                        self.currentUser.setAddress(editAddress)
                    elif editNum == 2:
                        editUsername = input("Enter your new username: ")
                        self.currentUser.setUsername(editUsername)
                    elif editNum == 3:
                        editPassword = input("Enter your new password: ")
                        self.currentUser.setPassword(editPassword)
                    elif editNum == 4:
                        editFirst = input("Enter your new first name: ")
                        self.currentUser.setFirstname(editFirst)
                    elif editNum == 5:
                        editLast = input("Enter your new last name: ")
                        self.currentUser.setLastname(editLast)
                    elif editNum == 6:
                        editNumber = input("Enter your new phone number: ")
                        self.currentUser.setPhone(editNumber)
                    elif editNum == 7:
                        pass
                    else:
                        print("Invalid answer, returning to main menu")
                elif accountNum == 4:
                    cursor = connection.cursor()
                    deleteID = int(input("Please enter your User ID to confirm deletion"))
                    cursor.execute("DELETE * FROM users WHERE userID = deleteID")
                    connection.commit()
                    print("User deleted")
                    cursor.close()

                    choice == False
                    
                elif accountNum == 5:
                    pass
                else:
                    print("Invalid answer, returning to main menu")
            elif num == 4:
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

            elif addressCheck == n:
                print("Please edit your address in the Edit information tab and try again.")

            else:
                print("Invalid Answer, returning to main menu")

        elif checkout == n:
            pass
        else:
            print("Invalid Answer, returning to main menu")

    def loadInventory(self, cursor):
        cursor.execute("SELECT * FROM items")
        result = cursor.fetchall()

        self.inventory = []
        
        for x in result:
            self.inventory.addItem()

        
    def checkInventory(self):
        cursor.execute("SELECT * FROM items")
        result = cursor.fetchall()

        for x in result:
            print(x)

        
    def loadUsers(self, cursor):
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()

        self.users = []

        for x in result:
            self.users.append(x)
            
    def loadOrders(self, cursor):
        cursor.execute("SELECT * FROM orders")
        result = cursor.fetchall()

        self.orders = []

        for x in result:
            self.orders.append(x)

        
    def writeOrders(self, cursor):
        cursor.execute("INSERT INTO orders orders")
        connection.commit()

        
    def writeCart(self, cursor):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO cart cart)")
        connection.commit()


    def writeItem(self, item, cursor):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO items item")
        connection.commit()


    def setCurrUser(self, userID):
        self.currentUser = userID
