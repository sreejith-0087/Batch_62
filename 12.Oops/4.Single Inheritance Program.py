class A:
    def Read(self):
        self.num1 = int(input('Enter the num:: '))
        self.num2 = int(input('Enter the num:: '))


class B(A):
    def Sum(self):
        self.s = self.num1 + self.num2
        print(self.s)


add = B()

add.Read()
add.Sum()