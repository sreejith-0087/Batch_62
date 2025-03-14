"""
function returns a list where the string has been split at each match
"""

import re

t = 'rain rain go away'

x = re.split('^rain', t)
print(x)

x = re.split('away$', t)
print(x)

x = re.split('[b-j]', t)
print(x)

x = re.split('[^b-j]', t)
print(x)

