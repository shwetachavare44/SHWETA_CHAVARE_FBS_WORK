def sum_odd(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 != 0 :
            total += i
    return total 

res = sum_odd(3)
print(f"Sum of odd numbers are :{res}.")