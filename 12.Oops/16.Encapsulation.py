# Public = self.a
# Private = self._b
# Protected = self.__c


class Encup:

    def __init__(self):
        self.a = 34
        self._b = 23
        self.__c = 56

    def display(self):
        print(self.a)
        print(self._b)
        print(self.__c)

Bm = Encup()
Bm.display()
print(Bm.a)
print(Bm._b)
print(Bm.__c)  # Will create error

