def is_armstrong(num):
    s = 0
    temp = num
    n1= len(str(num))

    while temp > 0:
        digit = temp % 10
        s += digit ** n1
        temp //= 10

    return s == num

 
res = is_armstrong(153)
if res :
    print(f"{res} is armstrong number.")
else :
    print(f"{res} is not armstrong number.")