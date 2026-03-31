# 12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input('Enter your Number :'))
temp = num

d1 = temp % 10
temp = temp // 10
d2 = temp % 10
temp = temp // 10
d3 = temp % 10
temp //= 10
rev = d1*100 + d2*10 + d3

if(num == rev):
    print(f'{num} is a palindrome number.')
else:
    print(f'{num} is not a palindrome number.')