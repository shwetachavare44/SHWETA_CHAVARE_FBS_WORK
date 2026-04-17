start = int(input("Enter your starting number :"))
end = int(input("Enter your ending number :"))

print(f"The odd numbers from {start} to {end} are :")

for i in range(start, end + 1):
    if i % 2 != 0 :
        print(i)
print()

