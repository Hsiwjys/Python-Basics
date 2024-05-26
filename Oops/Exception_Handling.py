"""
Exception Handling is also called as error handling, it has
three types :
      Compile time error
      Logical error
      Run time error
"""
print("hi")
# printr("hello") ---> compile time error
er = 23
rt = 34
# cal sum of above two num
print(er + er)    # logical error
ty = int(input("ty:"))
yu = int(input("yu:"))
print(ty * yu)    # runtime error
try:
    sf = int(input("as:"))
    hj = int(input("hj:"))
    print(sf + hj)
except TypeError as e:
    print("Type Error", e)
except ValueError as e:
    print("Value Error", e)
except NameError as e:
    print("Name Error", e)
except Exception as e:
    print("Error", e)
finally:
    print("Completed")
