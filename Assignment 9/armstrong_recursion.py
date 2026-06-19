def armstrong(num, power):
    if num == 0:
        return 0
    digit = num % 10
    return digit ** power + armstrong(num // 10, power)

num = int(input("Enter a number:"))
power = len(str(num))

if armstrong(num, power) == num:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")