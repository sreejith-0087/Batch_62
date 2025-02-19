l = ['Apple', 'Orange', 'Apple', 'Grape', 'Kiwi', 'Grape']

emp = []

for i in l:
    if i not in emp:
        emp.append(i)
print(emp)
        