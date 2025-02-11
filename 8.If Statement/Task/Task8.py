d = {
    1: " one", 2: " two", 3: " three", 4: " four", 5: " five",
    6: " six", 7: " seven", 8: " eight", 9: " nine", 10: " ten",
    11: " eleven", 12: " twelve", 13: " thirteen", 14: " fourteen",
    15: " fifteen", 16: " sixteen", 17: " seventeen", 18: " eighteen",
    19: " ninteen", 20: " twenty", 30: " thirty", 40: " fourty",
    50: " fifty", 60: " sixty", 70: " seventy", 80: " eighty", 90: " ninty",
    100: " hundred"
}

n = int(input('Enter the number:: '))

if n<=100 and n>=1:
    if n in d:
        a = d.get(n)
        print(a)
    else:
        b = n%10
        b = d.get(b)
        c = n//10
        c = c * 10
        c = d.get(c)
        z = c + b
        print(z)
else:
    print('Invaild')