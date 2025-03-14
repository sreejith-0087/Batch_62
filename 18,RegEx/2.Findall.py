"""
function returns a list containing all matches
"""


import re

t = 'rain rain go away'

x = re.findall('rain', t)
print(x)

x = re.findall('away$', t)
print(x)

x = re.findall('[b-j]', t)
print(x)

x = re.findall('[^b-j]', t)
print(x)

