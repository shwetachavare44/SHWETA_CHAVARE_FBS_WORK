def isPrime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return isPrime(n, i + 1)

num = int(input("Enter your Number:"))

if isPrime(num):
    print("Prime Number")
else :
    print("Not a prime number")