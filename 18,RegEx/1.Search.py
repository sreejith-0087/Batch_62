"""
searches the string for a match, and returns a Match object
if there is a match.If there is more than one match,
only the first occurrence of the match will be returned

"""

import re

t = 'rain rain go away'

x = re.search("^rain", t) #Start with 'rain'
print(x)

x = re.search("away$", t) #Ends with 'away'
print(x)

x = re.search("[b-j]", t) #Contains b to j
print(x)

x = re.search("[^b-j]", t) #not Contains b to j
print(x)

