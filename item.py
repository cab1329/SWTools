#cab1329

class Item:
    
    #Constructor
    def __init__(self, itemPrice, itemName, itemQuantity, itemID):
        try:
            self.itemName = str(itemName)
        except:
            print("Item.itemName: An unknown error occurred.")

        try:
            self.itemPrice = float(itemPrice)
        except TypeError:
            print("Item.itemPrice: TypeError")
        except:
            print("Item.itemPrice: An unknown error occurred.")

        try:
            self.itemQuantity = int(itemQuantity)
        except TypeError:
            print("Item.itemQuantity: TypeError")
        except:
            print("Item.itemQuantity: An unknown error occurred.")

        try:
            self.itemID = int(itemID)
        except TypeError:
            print("Item.itemID: TypeError")
        except:
            print("Item.itemID: An unknown error occurred.")

    #Setter Block
    def setName(self, itemName):
        try:
            self.itemName = str(itemName)
        except:
            print("Item.setName: An unknown error occurred.")

    def setPrice(self, itemPrice):
        try:
            self.itemPrice = float(itemPrice)
        except TypeError:
            print("Item.setPrice: TypeError")
        except:
            print("Item.setPrice: An unknown error occurred.")

    def setQuantity(self, itemQuantity):
        try:
            self.itemQuantity = int(itemQuantity)
        except TypeError:
            print("Item.setQuantity: TypeError")
        except:
            print("Item.setQuantity: An unknown error occurred.")

    def setID(self, itemID):
        try:
            self.itemID = int(itemID)
        except TypeError:
            print("Item.setID: TypeError")
        except:
            print("Item.setID: An unknown error occurred.")


    #Getter Block
    def getName(self):
        return self.itemName
    
    def getPrice(self):
        return self.itemPrice

    def getQuantity(self):
        return self.itemQuantity

    def getID(self):
        return self.itemID

    #Destructor
    def __del__(self):
        del self
