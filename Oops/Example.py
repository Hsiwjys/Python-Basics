class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def area(self):
        a = int(input("Enter the length of rectangle:"))
        b = int(input("Enter the breath of rectangle:"))
        print("Area of Rectangle is:", a*b)


A = Rectangle()
A.area()

"""
Create a base class called Person with a constructor 
that takes a name as a parameter. Create a derived 
class called Student that inherits from Person and 
has a constructor that takes a parameter called grade. 
Write a method in Student to display the name and grade
of the student. Use Super keyword to achieve.
"""


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        print("Name is:", name)
        print("Grade is:", grade)


obj = Student("Siva", "A")

"""
Create a base class called Vehicle with a method 
start() that prints "Vehicle started." Create a 
derived class called Car that inherits from Vehicle 
and overrides the start() method to print "Car started."
"""


class Vehicle:
    def start(self):
        print("vehicle Started")


class Car(Vehicle):
    def start(self):
        print("Car Started")


obj1 = Car()
obj1.start()

"""
create a base class called Employee with properties 
name and salary. Create a derived class called Manager 
that inherits from Employee and adds a property 
department. Write a method in Manager to display the 
name, salary, and department of the manager.
"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)


obj2 = Manager("Siva", "70000", "EEE")
obj2.display()
