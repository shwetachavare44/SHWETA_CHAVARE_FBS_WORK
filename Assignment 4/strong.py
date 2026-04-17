# Strong number = suppose 145 = 1! + 4! + 5! = 145

n = int(input("Enter your number:"))

temp = n
sum_fact = 0

while temp > 0:
    digit = temp % 10

    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    sum_fact += fact 
    temp //= 10

if sum_fact == n:
    print("Strong number.")
else :
    print(" No strong number")
