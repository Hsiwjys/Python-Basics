class Laptop:
    chargertype = "C TYPE"

    def __init__(self):
        self.brand = ""
        self.price = 34

    def setprice(self, price):
        self.price = price

    def getprice(self):    # instance method
        print(self.price)

    @classmethod
    def changechargertype(cls):   # class method
        cls.chargertype = "B TYPE"
        print("Charger type changed to B")
        """
        In this method we are using function user variable  
        for access the class variable 
        """

    @staticmethod
    def info():      # static method
        print("Static method is used")


"""
In the function we are not using function variable
for the function.
"""


hp = Laptop()
hp.setprice(20000)
hp.getprice()
Laptop.changechargertype()
hp.info()
