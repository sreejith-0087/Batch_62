"""
class Cal:
    def Add(self, n1, n2):
        print(f'Sum = {n1+n2}')

    def Add(self, n1, n2, n3):
        print(f'Sum = {n1+n2+n3}')

    def Add(self, n1, n2, n3, n4):
        print(f'Sum = {n1+n2+n3+n4}')

num = Cal()
num.Add(23, 67)
"""

class Cal:
    def Add(self, n1=0, n2=0, n3=0, n4=0):
        print(f'Sum = {n1+n2+n3+n4}')

ob = Cal()
ob.Add(45, 56)

