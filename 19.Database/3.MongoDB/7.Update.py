import pymongo


myClient = pymongo.MongoClient()

myDb = myClient['Fruitify']

myCol = myDb['Fruits']


# myCol.update_one({"Item":"Mango"}, {"$set":{'Price':279}})

# myCol.update_one({"Item":"Mango"}, {"$set":{'Type':'Fruit'}})

myCol.update_many({}, {"$set":{'Type':'Fruit'}})


n = myCol.find()

for i in n:
    print(i)