li = [10, 22, 35, 54, 22, 35, 76, 10]
newLi = []

for i in li:
    found = False
    for j in newLi:
        if i==j:
            found = True
            break
    if not found:
        newLi.append(i)
    
print(newLi)