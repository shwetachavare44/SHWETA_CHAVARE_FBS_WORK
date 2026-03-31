# 4. Write a program to enter P. T. R and calculate simple Interest.

principle = float(input('Enter Principle Amount :'))
rate = float(input('Enter annual interest rate (in %) :'))
time = float(input('Enter time (in year)  :'))

simple_interest = (principle * rate * time) / 100

print(f"Simple Interest is : {simple_interest}")
