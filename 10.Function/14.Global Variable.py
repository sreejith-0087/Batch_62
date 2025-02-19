'''
Variables that are created outside of a function  are known as global variables.
'''


a = 45

def fun():
    print(a + 23)

fun()

print(a + 67)

