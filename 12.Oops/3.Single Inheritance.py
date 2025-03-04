"""
Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.
"""

class A:
    def display(self):
        print('Class A: Method display')


class B(A):
    def display1(self):
        print('Class B: Method display1')


obj = B()

obj.display()
obj.display1()

