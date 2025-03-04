class Parent:
    def Property1(self):
        print('Class Parent: Method Property1')

    def Property2(self):
        print('Class Parent: Method Property2')

class Child(Parent):
    def Property1(self):
        print('Class Child: Method Property1')

    def Property2(self):
        print('Class Child: Method Property2')


mn = Child()
mn.Property1()
mn.Property2()

