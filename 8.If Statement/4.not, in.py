a = ['Apple', 'Grape', 'Mango']

new = 'Banana'

if new in a:
    print('yes')
else:
    a.append(new)

print(a)

print('------------------------')

new1 = 'Kiwi'

if new1 not in a:
    a.append(new1)
else:
    print('yes, is in the list')

print(a)

