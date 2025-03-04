class A:
    def display(self):
        print('Class A: Method display')

class B:
    def display1(self):
        print('Class B: Method display1')


class C(A, B):
    def display2(self):
        print('Class C: Method display2')


m = C()

m.display()
m.display1()
m.display2()

