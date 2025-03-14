import pymongo


myClient = pymongo.MongoClient()


#Select/Create Database
myDb = myClient['Fruitify']


#Select/Create Collection
myCol = myDb['Fruits']