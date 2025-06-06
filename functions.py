"""
functions are create using to keyword def
Syntax:
def fun_name(Arguments):
    your code with or without return type
"""


def naan():
    print("hi any one is here?")  # Creating a FUNCTION


naan()    # Calling the function


def add(n1, n2):
    print(n1 + n2)


def sub(n1, n2):
    print(n1 - n2)


def mul(n1, n2):
    print(n1 * n2)


def div(n1, n2):
    print(n1 / n2)


def find_odd_or_even(n1):
    if n1 % 2 == 0:
        print("given no is even")
    else:
        print("give no is odd")


def pass_or_fail(n1):
    if n1 >= 35:
        print("Pass")
    else:
        print("Fail")


def print_range(n1, n2):
    for i in range(n1, n2):
        print(i, end="")


a = int(input("Enter the value  of a:"))
b = int(input("Enter the value of b:"))
add(a, b)
sub(a, b)
mul(a, b)
div(a, b)
find_odd_or_even(a)
pass_or_fail(a)
print_range(a, b)
"""
now we are going to use the return keyword
"""


def return_keyword():
    return "I am using return keyword"


return_keyword()
print(return_keyword())


s_username = "Emc"
s_password = "123"
uname = input("user name:")
password = input("password:")


def validate(n1, n2):
    if n1 == s_username and n2 == s_password:
        return True
    else:
        return False


print(validate(uname, password))
