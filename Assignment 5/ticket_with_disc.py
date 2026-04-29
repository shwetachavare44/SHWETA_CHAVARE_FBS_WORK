#Q. 3) Ticket cost with discount
n = int(input("Enter number of passengers: "))
cost = float(input("Enter ticket cost: "))
total = 0

for i in range(n):
    age = int(input(f"Enter age of passenger {i+1}: "))
    
    if age < 12:
        price = cost * 0.7
    elif age > 59:
        price = cost * 0.5
    else:
        price = cost
    
    total += price

print("Total amount:", total)