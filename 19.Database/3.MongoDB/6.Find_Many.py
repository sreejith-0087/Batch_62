import pymongo


myClient = pymongo.MongoClient()

myDb = myClient['Fruitify']

myCol = myDb['Fruits']

n = myCol.find()

for i in n:
    print(i)