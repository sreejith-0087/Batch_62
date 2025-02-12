'''
continue statement we can stop the current iteration, and continue with the next
'''

s = 0

while s<10:
    s = s+1
    if s == 5:
        continue
    print(s)
