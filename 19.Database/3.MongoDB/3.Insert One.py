import pymongo


myClient = pymongo.MongoClient()

myDb = myClient['Fruitify']

myCol = myDb['Fruits']


#Record
new_red = {'Item': 'Apple', "Price": 299}
n = myCol.insert_one(new_red)
print('Inserted_Id', n.inserted_id)


#Record
new_red = {'_id': 1, 'Item': 'Orange', "Price": 80}
n = myCol.insert_one(new_red)
print('Inserted_Id', n.inserted_id)

