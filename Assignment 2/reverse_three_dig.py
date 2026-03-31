#10. Write a program to reverse three-dig

num = int(input('Enter your three-digit Number :'))
temp = num

d1 = temp % 10
temp = temp // 10
d2 = temp % 10
temp = temp // 10
d3 = temp % 10
temp //= 10
rev = d1*100 + d2*10 + d3

print(f'Reversed Number : {rev}')