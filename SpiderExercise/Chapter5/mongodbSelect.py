import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
# db = client['test']  equal
collection = db.students

result = collection.find_one({'name': 'Jorden'})
print(type(result))
print(result)


results = collection.find({'age': {'$gt': 20}})
print(result)

count = collection.find({'age': {'$gt': 20}}).count()
print(count)

# skip ingore two items from head
# limit how many result will return
results = collection.find({'age': {'$gt': 20}}).sort('name', pymongo.ASCENDING).skip(2).limit(2)
print(result)
