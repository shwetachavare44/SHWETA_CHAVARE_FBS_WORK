li = [10, 20, 30, 40, 50]
print(li)

largest = li[0]
second_largest = li[0]

for i in li:
    if i > largest:
        second_largest = largest
        largest = i
    elif i>second_largest and i != largest:
        second_largest = i

print("Second largest element in list:",second_largest)
