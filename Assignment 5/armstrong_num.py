# Q4) Armstrong numbers in range

start = int(input("Starting number: "))
end = int(input("Ending number: "))

for num in range(start, end + 1):
    s = 0
    temp = num
    n = len(str(num))

    while temp > 0:
        digit = temp % 10
        s += digit ** n
        temp //= 10

    if s == num:
        print(num)