from abc import ABC, abstractmethod


#Abstract Class
class BankAccount(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_Balance(self):
        pass


#Concrete Class
class SavingAccount(BankAccount):

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, Current balance: {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient Balance!')
        else:
            self.balance -= amount
            print(f'withdraw {amount}. Current Balance: {self.balance}')

    def check_Balance(self):
        print(f'Current Balance: {self.balance}')


account = SavingAccount()
account.deposit(5000)
account.withdraw(1500)
account.check_Balance()