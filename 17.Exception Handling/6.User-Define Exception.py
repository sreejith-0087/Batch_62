class NagVal(Exception):
    def __init__(self, value):
        self.val = value
    def __str__(self):
        return self.val


def check(n):
    if n<0: raise NagVal('Negative values not allowed')

    print(f'Accepted {n}')


try:
    a = int(input('Enter Value: '))
    check(a)

except ValueError as e:
    print('only integer allowed!!\n', e)

except Exception as e:
    print(e)


