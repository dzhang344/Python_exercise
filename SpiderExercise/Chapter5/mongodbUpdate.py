import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
# db = client['test']  equal
collection = db.students

condition = {'name': 'Jorden'}
student = collection.find_one(condition)
student['age'] = 26
result = collection.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)