start = int(input("Enter your starting  number :"))
end = int(input("Enter your ending number:"))
num = int(input("Enter your divisor number:"))
for i in range (start, end+1):
    if (i % num == 0):
        print(i)