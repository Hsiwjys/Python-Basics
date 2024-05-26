"""
now we are going see about class and object
Almost everything in Python is an object, with its
properties and methods.
A Class is like an object constructor, or a "blueprint"
for creating objects.

SYNTAX FOR CLASS:
      class ClassName:
         <statement-1>
         .
         .
         .
         <statement-N>

SYNTAX FOR ACCESS OF CLASS:
         variable = class_name

SYNTAX FOR ACCESS OF OBJECT:
          variable. class_function_name()
"""


class Location:
    mass = ""
    name = "nhv"

    def view(self):
        print("jolly")

    def sri(self):
        print("boring")


thiru = Location()
naveen = Location()
thiru.view()
naveen.sri()
print(naveen.name)
naveen.name = "Naveen"
print(naveen.name)
print(thiru.name)


class Laptop:
    price = 0
    Processor = ""
    Ram = ""

    def __init__(self):
        print("Demo")


hp = Laptop()
dell = Laptop()
lenovo = Laptop()
hp.price = 50000
hp.Ram = "8 GB"
hp.Processor = "intel i5"
print("hp ram is: " + hp.Ram)
"""
now we are going to see about constructor and self 
keyword :
       A constructor is a unique function that gets 
called automatically when an object is created of a class.

       The main purpose of a constructor is to initialize 
or assign values to the data members of that class.
"""


class Have:
    def member(self):
        print("ram:", self.ram)
        print("processor", self.processor)

    def __init__(self):
        print("out of this world")
        self.ram = ""
        self.processor = ""


mass = Have()
mass.ram = "8 GB"
mass.processor = "i5"
mass.member()
"""
now we are going to create empty class by using keyword:
                  pass 
"""


class Odd:
    pass


"""
1)Create a class called student
create a variable = name and register number using 
constructor.Create a function called display which 
should display the name and register number of the student
"""


class Student:
    def __init__(self):
        self.name = "naan"
        self.register = "23456"

    def display(self):
        print("Name:", self.name)
        print("Register Number:", self.register)


st1 = Student()
st2 = Student()

st1.name = "sri"
st1.register = "1"


st2.name = "piece"
st2.register = "2"


st1.display()
st2.display()

"""
Create a class called Fruit
Create a variable called color using init method
Create a object called apple "Pass the color variable 
as a parameter through object".
"""


class Fruit:
    def __init__(self, col, shape):
        self.color = col
        self.sha = shape


Apple = Fruit("red", "cylinder")
print(Apple.color)
print(Apple.sha)

"""
Create a class called teacher
Create a variable = name and register number using 
constructor. Create a function called display which 
should display the name and register number of the teacher
Create t1 and t2 object and pass the name and reg no 
value through object.
"""


class Teacher:
    def __init__(self, name, reg):
        self.name = name
        self.regNo = reg

    def display(self):
        print("Name:", self.name)
        print("Reg No:", self.regNo)


st1 = Teacher("Itachi", "1")
st1.display()

st2 = Teacher("madara", "2")
st2.display()

"""
Create a class called calculator
Create 2 variables a and b
Create a function called add,sub,mul, div all 
functions should take 2 variables as parameter.
Pass the a and b value through object().
"""


class Calculator:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def add(self):
        print("Addition of two values:", self.num1 + self.num2)

    def sub(self):
        print("subtraction of two values:", self.num1 - self.num2)

    def mul(self):
        print("multiplication of two values:", self.num1 * self.num2)

    def div(self):
        print("division of two values:", self.num1 / self.num2)


obj1 = Calculator(22, 24)
obj1.add()
obj1.sub()
obj1.mul()
obj1.div()
