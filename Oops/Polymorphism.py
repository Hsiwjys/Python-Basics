"""
The word polymorphism means having many forms.
In programming, polymorphism means the same function
 name (but different signatures) being used for different
 types. The key difference is the data types and number of
  arguments used in function.
"""


def add(a=10, b=20, c=30):
    print(a+b+c)


add()
add(1)
add(1, 2)
add(1, 2, 3)

"""
Create a class called Animal with a method sound() that 
prints "Animal makes a sound." Create a derived class 
called Dog that inherits from Animal and overrides the 
sound() method to print "Dog barks." Create another 
derived class called Bird that inherits from Animal and 
overrides the sound() method to print "Birds Sing."
"""


class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):  # method over riding
        print("Dog Barks")


class Bird(Animal):
    def sound(self):
        print("Bird Sing")


obj = Dog()
obj.sound()
obj1 = Bird()
obj1.sound()
