from abc import ABC, abstractmethod


class ATM(ABC):

    @abstractmethod
    def Balance(self):
        pass


class User1(ATM):
    def Balance(self):
        print('Balance = 2000')

class User2(ATM):
    def Balance(self):
        print('Balance = 1358')


us = User2()
us.Balance()

