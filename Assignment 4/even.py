# for all numbers
start = int(input('Enter the Starting no :'))
end = int(input('Enter the Ending no:'))
print(f'The even number from {start} to {end} are :')

for i in range ( start, end + 1):
         if i % 2 == 0 :
            print(i)

print()