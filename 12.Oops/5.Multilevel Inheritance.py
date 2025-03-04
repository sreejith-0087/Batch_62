'''
Multi-level inheritance enables a derived class to inherit properties from an immediate
parent class which in turn inherits properties from his parent class.
'''

class A:
    def display(self):
        print('Class A: Method display')


class B(A):
    def display1(self):
        print('Class B: Method display1')

class C(B):
    def display2(self):
        print('Class C: Method display2')


obj = C()

obj.display()
obj.display1()
obj.display2()