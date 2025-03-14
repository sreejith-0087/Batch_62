"""
The raise keyword is used to raise an exception.
you can define what kind of error to raise, and the text to print to the user.
"""


def check(n):
    if n<0: raise Exception

    print(f'Accepted {n}')


try:
    a = int(input('Enter Value: '))
    check(a)

except ValueError as e:
    print('only integer allowed!!\n', e)

except Exception as e:
    print('Negative values not allowed', e)

