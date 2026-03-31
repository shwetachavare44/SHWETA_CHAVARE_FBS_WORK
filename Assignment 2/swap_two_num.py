# 9. Write a program to swap two numbers without using third variable.

a = int(input('Enter First Number (a) :'))
b = int(input('Enter Second Number (b) :'))

a = a + b 
b = a - b
a = a - b

print(f'After Swapping : a ={a}, b ={b}')