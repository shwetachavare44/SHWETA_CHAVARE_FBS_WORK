n = int(input("Enter your Number of elements for create list:"))
li =[]

for i in range(n):
    num = int(input("Enter Element:"))
    li.append(num)

even =[]
odd =[]

for i in li:
    if i % 2 == 0:
        even.append(i)
    else :
        odd.append(i)

print("List:",li)
print("Even elements in List:", even)
print("Odd elements in List:", odd)