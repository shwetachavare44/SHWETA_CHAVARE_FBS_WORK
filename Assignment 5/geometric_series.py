# Q. 7c. Geometric series (ratio = 2)
n = int(input("Enter number: "))
sum = 0

for i in range(n):
    sum += 2 ** i

print("Sum:", sum)