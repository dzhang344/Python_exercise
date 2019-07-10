import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
# db = client['test']  equal
collection = db.students

condition = {'name': 'Jorden'}
result = collection.delete_one(condition)
# result = collection.delete_many({'age', {'$lt': 25}})