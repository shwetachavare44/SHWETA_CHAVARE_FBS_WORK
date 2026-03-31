# 4. Write a program to input all sides of a triangle and check whether triangle is valid or not.

a = int(input('Enter First Side (a) :'))
b = int(input('Enter Second Side (b) :'))
c = int(input('Enter Third Side (c) :'))

if a + b > c and a + c > b and b + c > a :
    print("Triangle is Valid.")

else :
    print("Triangle is not valid.")