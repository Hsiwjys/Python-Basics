"""
# for loop
for i in "apple":
    print(i)
for i in range(5):  # print numbers in range function
    print(i)
for i in range(1, 5):
    print(i)
print("printing 2 tables")
for i in range(1, 11):
    print("2 x", i, "=", 2 * i)
# printing numbers from given range
inputNum3 = int(input("start:"))
inputNum4 = int(input("end:"))
for i in range(inputNum3 + 1, inputNum4):
    print(i)
# finding no odd,even num in 1 to 10
count = 0
count1 = 0
for i in range(1, 11):
    if i % 2 == 0:
        count = count + 1
    else:
        count1 = count1 + 1
print("total no of even num in 1 to 10:", count)
print("total no of odd num in 1 to 10:", count1)
count2 = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        count2 = count2 + 1
print("total no of num divisible by 3 & 5 from 1 to 100:", count2)
# sum of natural numbers using for loop
snn = 0
for i in range(1, 6):
    snn = snn + i
print("sum of natural num 1 to 5 :", snn)
# sum of natural numbers without using for loop
a = int(input("Enter the n vale for sum of natural numbers:"))
a = (a*(a+1))/2
print(a)

"""
# NESTED FOR LOOP
for i in range(1, 3):
    print("Week " + str(i))
    for j in range(1, 4):
        print("Day " + str(j))
for i in range(5):
    print("*", end="")
"""
To print the values
1
1 2
1 2 3
1 2 3 4 
"""
for i in range(1, 5):
    print()
    for j in range(1, i+1):
        print(j, end="")
"""
To print 
*
* *
* * *
* * * *
"""
for i in range(1, 5):
    print()
    for j in range(1, i+1):
        print("*", end="")
"""
END OF FOR LOOP

NOW WE ARE STARTING WHILE LOOP
syntax
         while (Condition):
            statements
"""
"""
to print number 10,20,30,40,......,200 using while
"""
print()
variable = 10
while variable <= 200:
    print(variable, end=",")
    variable = variable + 10
"""
find the factorial of a number
"""
"""
inp = int(input("\nenter the number"))
fact = 1
while inp > 0:
    fact = fact * inp
    inp = inp - 1
print(fact)
"""
# to print sum of digit
a = int(input("\nEnter the number:"))
b, c, d = 0, 0, 0
while a > 0:
    b = a % 10
    c = b + c
    a = a / 10
    if c > 9:
        d = c % 10

print(int(c))
