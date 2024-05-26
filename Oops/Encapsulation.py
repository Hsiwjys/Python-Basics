"""
Encapsulation describes the idea of wrapping data and
the methods that work on data within one unit.This puts
restrictions on accessing variables and methods directly
and can prevent the accidental modification of data.
To prevent accidental change, an object’s variable can
only be changed by an object’s method. Those types of
variables are known as private variables.
"""


class Company:
    def __init__(self):
        self.__companyName = "CLOCK"  # private variable
        self._companyN = "FAN"        # protected variable

    def company(self):
        print(self.__companyName)


class Company1(Company):
    def print(self):
        print(self._companyN)


obj = Company()
obj1 = Company1()
obj.company()
obj1.print()
