#1! + 2! + 3! +.....+n

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def sum_fact(n):
    total = 0
    for i in range(1, n+1):
        total += factorial(i)
    return total

res = sum_fact(10)

print(f"The sum of factorial of given number is {res}.")
    
