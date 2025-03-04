class Car:
    def Model_1(self):
        print('Class Car: Method Model_1')

    def Model_2(self):
        print('Class Car: Method Model_2')

class Bike:
    def Model_1(self):
        print('Class Bike: Method Model_1')

    def Model_2(self):
        print('Class Bike: Method Model_2')

ob = Car()
ob1 = Bike()

for i in (ob, ob1):
    i.Model_1()
    i.Model_2()