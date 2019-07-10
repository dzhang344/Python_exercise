import pymysql

# id = '20120001'
# user = 'Bob'
# age = 20
#
# db = pymysql.connect(host='localhost', user='root', password='Bo123wen!', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'INSERT INTO student(id, name, age) values (%s, %s, %s)'
# try:
#     cursor.execute(sql, (id, user, age))
#     db.commit()
# except:
#     db.rollback()
# db.close()

db = pymysql.connect(host='localhost', user='root', password='Bo123wen!', port=3306, db='spiders')
cursor = db.cursor()
data = {
    'id ': '20120002',
    'name': 'Jorden',
    'age':  22
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s']*len(data))
sql = 'INSERT INTO {table}({keys}) values ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except pymysql.InternalError as error:
    print('Failed', error.args)
    db.rollback()
db.close()


