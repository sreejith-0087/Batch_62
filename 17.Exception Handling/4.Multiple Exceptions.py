try:
    a = int(input('Enter the num:: '))
    b = int(input('Enter the num:: '))
    c = a/b

    print(f'div {c}')

except ValueError:
    print('Enter Integer Values')

except ZeroDivisionError:
    print("Can't divided by 0")

    