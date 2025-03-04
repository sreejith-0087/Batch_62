class A:
    def display(self):
        print('Class A: Method display')

class B(A):
    def display1(self):
        print('Class B: Method display1')

class C(A):
    def display2(self):
        print('Class C: Method display2')


k = B()
l = C()

k.display()
k.display1()

l.display()
l.display2()

