"""""
print("enter the values of a & b")
a=int(input())
b=int(input())
if(a>b):
    print(a)
else:
    print(b)
print("win"=="win") # equal operator
print("win"=="winm")
Mass=input("Meghna is died or not?")
if(Mass=="died"):
    print("s meet p")
else:
    print("s weeds m")
print("finding a is divide by 3 and 5")
if(a%3==0 and a%5==0): # logical and operator
    print("a is divide by 3 and 5")
else:
    print("a is not divide by 3 and 5")
mark=int(input("your mark"))
if(mark<=35):
    print("poor student")
elif(mark>35 and mark<=70): # else if condition
    print("average student")
elif(mark>70 and mark<=100):
    print("good student")
    name=input("enter your name")
    department=input("enter the department name")
    print("your name is",name,"and your department is",department)
else:
    print("invalid number")
number1=int(input("enter the value of number1"))
number2=int(input("enter the value of number2"))
operation=input("addition/subtraction/multiplication/division")
if(operation=="addition"):
    print("addition of two number is",number1+number2)
elif(operation=="subtraction"):
    print("the subtraction of two numbers is:",number1-number2)
elif(operation=="multiplication"):
    print("the multiplication of two numbers is:",number1*number2)
elif(operation=="dvision"):
    print("the division of two numbers is:",number1/number2)
else:
    print("Invalid operation")
salary=int(input("Enter you salary"))
age=int(input("Enter your age"))
if(salary>2000 or age<=25): # logical or operator
    loanAmount=int(input("Enter the loan amount"))
    if(loanAmount<=50000):
        print("your are eligible")
    else:
        print("maximum loan amount is 50000")
else:
    print("you are not eligible")
"""""
print("enter the five subject marks")
sub1 = int(input("Enter the sub1 mark"))
sub2 = int(input("Enter the sub2 mark"))
sub3 = int(input("Enter the sub3 mark"))
sub4 = int(input("Enter the sub4 mark"))
sub5 = int(input("Enter the sub5 mark"))
totalMarks = sub1+sub2+sub3+sub4+sub5
average = totalMarks / 5
if average < 35:
    print("additional class is required")
else:
    print("you are good to go")
