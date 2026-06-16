li = [10, 27, 30, 49, 56]
print(li)

m = int(input("Enter m: "))
n = int(input("Enter n: "))

for i in li:
    if i % m == 0 and i % n == 0:
        print(i)