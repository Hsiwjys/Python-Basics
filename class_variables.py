"""
In this we are going see about Instance Variable
       self is the Instance Variable in the class
       by using self we access the class n number of times
"""


class Phone:
    def __init__(self, brand, price, chargerType):
        self.brand = brand
        self.price = price
        self.chargerType = chargerType

    def display(self):
        print("Brand:", self.brand)
        print("price:", self.price)
        print("Charger type:", self.chargerType)


Samsung = Phone("samsung", 13000, "B- type")
Samsung.display()

"""
class variables
   it is variable in the class can be accessed any in the
   program , it is used for access permanent values by 
   using variable 
"""


class Mobile:
    chargerType = "C-Type"

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("price:", self.price)
        print("Charger type:", self.chargerType)


Samsung = Mobile("samsung", 13000)
Samsung.display()
Mobile.chargerType = "B- Type"
Samsung.display()

