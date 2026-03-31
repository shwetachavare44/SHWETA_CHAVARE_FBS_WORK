# 8. Write a program to swap two numbers using third variable.

a = int(input('Enter First Number (a) :'))
b = int(input('Enter Second Number (b) :'))

temp = a 
a = b
b = temp

print(f'After Swapping : a ={a}, b ={b}')