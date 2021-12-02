#Shopping cart class
class Shopping_Cart:
    #Parameter Constructor
    def __init__(self, customer_ID = 0, currentdate = 'January 1, 2021', cartItems = [], cartID = 0):
        self.customer_ID = customer_ID
        self.currentdate = currentdate
        self.cartItems = cartItems
        self.cartID = cartID
    #Add an item
    def addItem(self, itemName, itemQuantity):
        print('\nADD ITEM ' , end='\n')
        self.cartItems.append(Item(itemName, itemQuantity))
    #remove from cart
    def removeItem(itemID):
        i1 = 0
        #loop through the cart
        for item1 in self.cartItems:
            if(item1.itemName == itemID):       
                del self.cartItems[i1]
                flagvalue=True
                break
            else:
                i1 += 1
                flagvalue=False
        #If not found
        if(flagvalue==False):
            print('Item could not be found. Nothing removed')
    #Method to modify quantity of cart
    def modifyItem(self):
        print('\nCHANGE QUANTITY' , end='\n')
        name1 = str(input('Enter name: '))
        #Loop through the cart
        for item1 in self.cartItems:
            if(item1.itemName == name1):
                quantity1 = int(input('Enter quantity: '))
                item1.itemQuantity = quantity1
                flagvalue=True
                break
            else:
                flagvalue=False

        #If not found
        if(flagvalue==False):
            print('Cannot be modified')
     #Method to find number of items in cart
    def get_numberitems_cart(self):
        numitems=0
        for item1 in self.cartItems:
            numitems= numitems+item1.itemQuantity
        return numitems
    #Method to get price of the cart
    def get_valuecost_of_cart(self):
        total_valuecost = 0.0
        valuecost = 0.0
        for item1 in self.cartItems:
            valuecost = (item1.itemQuantity * item1.itemPrice)
            total_valuecost += valuecost
        return total_valuecost
    #Display total
    def displaytotal():
        total_valuecost = get_valuecost_of_cart()
        if (total_valuecost == 0.0):
            print('Empty cart')
        else:
            result_cart()
    #Clear cart
    def clearCart(self):
        self.cartItems.clear()
        print('Cart emptied')
    #Print cart
    def result_cart(self):
        new1=Shopping_Cart()
        print('\nOUTPUT', end='\n')
        print('{}\'s Shopping Cart - {}'.format(self.customer_ID, self.currentdate))
        print('Number of Items:', new1.get_numberitems_cart(), end='\n\n')
        tc1 = 0
        for item1 in self.cartItems:
            print('{} {} @ ${} = ${}'.format(item1.itemName, item1.itemQuantity,
                                             item1.itemPrice, (item1.itemQuantity * item1.itemPrice)))
            tc1 += (item1.itemQuantity * item1.itemPrice)
        print('\nTotal: ${}'.format(tc1),end='\n')
