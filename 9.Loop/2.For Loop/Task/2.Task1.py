# 1. Program for read values from keyboard into list and find sum ?


a = str(input('Enter the Values:: '))

li = a.split()

print(li)

sum = 0

for value in li:
    sum = sum+int(value)
print(f'list sum = {sum}')

