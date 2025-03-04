class A:
    def display(self):
        print('Class A: Method display')

class B(A):
    def display1(self):
        print('Class B: Method display1')

class C(A):
    def display2(self):
        print('Class C: Method display2')

class D(B, C):
    def display3(self):
        print('Class D: Method display3')


p = D()

p.display()
p.display1()
p.display2()
p.display3()
