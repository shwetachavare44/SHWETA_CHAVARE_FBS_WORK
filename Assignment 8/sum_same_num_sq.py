# 1^ 1 + 2^2 + 3^3 +....+n

def sum_power(n):
    total = 0
    for i in range(1, n+1):
        total += i**i
    return total

res = sum_power(6)

print(f"Sum of power of given number is : {res}.")

