li = [10, 18, 7, 45, 77, 34,7]
print(li)

num = int(input("Enter element to remove:"))
newLi = []
for i in li:
    if i != num:
        newLi.append(i)

print(newLi)