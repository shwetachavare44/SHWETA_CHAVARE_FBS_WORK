# 1. Write a program to check if the given number is positive or negative.

num = int(input('Enter your number :'))

if(num == 0):
    print(f'{num} is neutral.')

elif (num > 0):
    print(f'{num} is positive.')

else :
    print(f'{num} is negative.')