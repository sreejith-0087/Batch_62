Age = int(input('Enter the age:: '))

if Age >= 1:
    if Age <= 12:
        print('Child')
    elif Age <= 19:
        print('Teenager')
    elif Age <= 59:
        print('Adult')
    else:
        print('Senior Citizen')
else:
    print('Invaild Age')

    