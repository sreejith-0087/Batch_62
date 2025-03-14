"""
  function replaces the matches with the text of your choice
"""

import re

t = 'rain rain go away'

x = re.sub('^rain','thunder', t)
print(x)

x = re.sub('away$','far', t)
print(x)

x = re.sub('[b-j]','*', t)
print(x)

x = re.sub('[^b-j]','-', t)
print(x)

