number = [1, 2, 3,4,5]
dup = []
count = 0
for x in number:
    for y in number:
        for z in number:
            if x != y and y != z:
                newNum = 100*x + 10*y + z
                dup.append(newNum)
                count += 1
print(len(dup), dup)

# print('total number is %d', %count)
