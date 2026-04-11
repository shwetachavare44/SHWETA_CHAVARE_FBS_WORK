# Q. 1.Write a program to print first n prime numbers 


num = int(input('Enter your number :'))
for i in range(1, num+1):
    if( num % 2 == 0):
        print(f'{num} is not prime.')
        break
else :
    print(f'{num} is prime.')
