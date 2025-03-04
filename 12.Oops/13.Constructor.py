"""
a constructor is a special method that is called when an object is created.
The purpose of a python constructor is to assign values to the data members within the class
when an object is initialized. The name of the constructor method is always __init__.

Two types of Constructor:
1.Parameterized Constructor
2.Non-Parameterized Constructor
"""


class Car:

    def __init__(self):
        print('Non-Parameterized Constructor')

n = Car()


class Student:

    def __init__(self, name, age):
        self.nm = name
        self.ag = age

    def show(self):
        print(self.nm)
        print(self.ag)

std = Student('Ajith', 21)
std.show()
