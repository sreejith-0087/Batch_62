import pymongo


myClient = pymongo.MongoClient()

myDb = myClient['Fruitify']

myCol = myDb['Fruits']

myCol.delete_one({})

myCol.delete_one({'_id': 6})

myCol.delete_many({})

n = myCol.find()

for i in n:
    print(i)

