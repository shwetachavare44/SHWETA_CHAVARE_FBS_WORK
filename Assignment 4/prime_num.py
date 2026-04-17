num = int(input('Enter your number :'))
for i in range(2, 7):
    if( num % 2 == 0):
        print(f'{num} is not prime.')
        break
else :
    print(f'{num} is prime.')