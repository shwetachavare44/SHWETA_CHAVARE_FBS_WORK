# 8. Write a program to convert days into years. weeks and days. 

days = int(input("Enter total days: "))
years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7

print(f"{years} Years, {weeks} Weeks, {remaining_days} Days")