number = ['1', '2', '3']
dup = set()
for x in number:
    for y in number:
        for z in number:
            newNum = x + y + z
            if newNum not in dup:
                dup.add(newNum)

for num in dup:
    print(num)
