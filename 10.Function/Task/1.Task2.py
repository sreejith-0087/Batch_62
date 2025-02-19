db = []


def create():
    limit = int(input('Enter the limit:: '))

    for i in range(limit):
        values = int(input('Enter the Value:: '))
        db.append(values)
    print(db)


def search():
    search = int(input('Enter the key for search:: '))

    if search in db:
        print(f'yes, {search} is in the list')
    else:
        print(f'{search} is not in the list')


def remove():
    rem = int(input('Enter the value for remove:: '))

    if rem in db:
        db.remove(rem)
    else:
        print(f'{rem} is not in the list')
    print(db)


while True:
    options = int(input('1.Create \n2.Search \n3.Remove \nEnter your option:: '))

    if options == 1:
        create()
    elif options == 2:
        search()
    elif options == 3:
        remove()
    else:
        break