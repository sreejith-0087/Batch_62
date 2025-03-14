import pymongo


myClient = pymongo.MongoClient()

myDb = myClient['Fruitify']

myCol = myDb['Fruits']

rec = [
    {'_id': 2, 'Item': 'Kiwi', "Price": 568},
    {'_id': 3, 'Item': 'Mango', "Price": 249},
    {'_id': 4, 'Item': 'Banana', "Price": 63},
    {'_id': 5, 'Item': 'Grape', "Price": 100},
    {'_id': 6, 'Item': 'Papaya', "Price": 45},
]

n = myCol.insert_many(rec)

print('Insert_Id', n.inserted_ids)

