import pymongo  #pip install pymongo

myClient = pymongo.MongoClient()

print(myClient.list_database_names())