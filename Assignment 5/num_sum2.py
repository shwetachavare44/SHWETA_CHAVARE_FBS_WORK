#Q 7e) x - x²/3 + x³/5 ...
x = int(input("Enter x: "))
n = int(input("Enter terms: "))
sum = 0
sign = 1

for i in range(1, n+1):
    sum += sign * (x ** i) / (2*i - 1)
    sign *= -1

print("Sum:", sum)