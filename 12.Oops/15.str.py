# The string representation of an object with the __str__() function.


class Student:

    def __init__(self, name, age):
        self.nm = name
        self.ag = age

    def __str__(self):
        return f'Name: {self.nm}, Age:{self.ag}'

std = Student('Ajith', 21)
print(std)

