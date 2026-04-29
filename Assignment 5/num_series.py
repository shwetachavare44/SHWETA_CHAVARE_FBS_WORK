#Q. 7b) N + N² + N³ ...

n = int(input("Enter number : "))
sum = 0

for i in range(1, n+1):
    sum += n ** i

print("Sum:", sum)