#7d) S = a + a²/2 + ...

a = int(input("Enter a: "))
sum = 0

for i in range(1, 11):
    sum += (a ** i) / i

print("Sum:", sum)