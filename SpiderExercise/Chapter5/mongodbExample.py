import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
# db = client['test']  equal
collection = db.students

student = {
    'id ': '20120002',
    'name': 'Jorden',
    'age':  22,
    'gender': 'male'
}

result = collection.insert_one(student)
# or insert_many([stu1, stu2])
print(result)