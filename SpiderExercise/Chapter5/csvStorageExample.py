import csv

with open('data.csv', 'w') as csvfile:
    # delimiter 修改分隔符
    # writer = csv.writer(csvfile, delimiter=' ')
    # writer.writerow(['id', 'name', 'age'])
    # writer.writerow(['10001', 'Mike', 20])
    # writer.writerow(['10002', 'Bob', 22])
    # writer.writerow(['10003', 'Jordan', 21])

    fieldname = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldname)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})


with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)