import pymongo


myClient = pymongo.MongoClient()

myDb = myClient['Fruitify']

myCol = myDb['Fruits']

n = myCol.find_one(5)

print(n)