num = int(input('Enter the number:: '))

s = 0

while num>0:
    b = num%10
    s = s*10+b
    num = num//10

print(s)

