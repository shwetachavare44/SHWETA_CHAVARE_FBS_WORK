#eg : 7 + 6 = 13

def sum_digits(num):
    if num == 0:
        return 0
    return num % 10 + sum_digits(num // 10)

num = int(input("Enter a number:"))
print("Sum of digits:",sum_digits(num))