def list_product(l):
    s = 1

    for i in l:
        s *= i

    print(f'Product = {s}')

li = [34, 65, 56, 45]
list_product(li)
