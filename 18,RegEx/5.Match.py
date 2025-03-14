"""
The Match object has properties and methods
used to retrieve information about the search,
and the result:

.span() returns a tuple containing the start-, and end positions of the match.

.string returns the string passed into the function

.group() returns the part of the string where there was a match
"""


import re


t = 'How are you'

x = re.search('you', t)

print(f"Object: {x}")
print("Span :", x.span())
print("Group :", x.group())




