"""
The filter() function in Python takes in a function and a list as arguments.

The function is called with all the items in the list and a new list is returned which
contains items for which the function evaluates to True.

"""


# Program to filter out only the even items from a list

li = [12, 43, 67, 50, 28, 9]

a = list(filter(lambda x: x%2==0, li))

print(a)

