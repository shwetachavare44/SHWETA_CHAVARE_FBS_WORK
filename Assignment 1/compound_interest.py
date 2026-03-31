# 5. Write a program to enter P, T, R and calculate Compound Interest.


principle = float(input('Enter Principle Amount :'))
rate = float(input('Enter annual interest rate (in %) :'))
time = float(input('Enter time (in year)  :'))


compound_interest = principle * (1 + (rate/100) ** time) - principle

print(f" Compound Interest is : {compound_interest}")
