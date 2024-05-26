class Grandpa:
    def money(self):
        print("My money")


class Father(Grandpa):
    def phone(self):
        print("dad's mobile")


# single inheritance

class Mother:
    def sweet(self):
        print("my sweet")


class Son1(Father):
    def laptop(self):
        print("Son's laptop")

# multiple Inheritance


class Son2(Father, Mother):
    def head_phone(self):
        print("it's my headphone")


class Son3(Father):
    pass


sri = Son1()
google = Son2()
it = Son3()
it.phone()  # Hierarchical inheritance
sri.laptop()
sri.phone()
google.sweet()
google.head_phone()
google.phone()
sri.money()   # Multi level inheritance
google.money()

"""
now we are going to SUPER KEYWORD in INHERITANCE
"""


class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        super().__init__()
        print("B")

    def you(self):
        print("suma")


class C(B, A):
    def __init__(self):
        super().__init__()
        print("C")


ob1 = C()
