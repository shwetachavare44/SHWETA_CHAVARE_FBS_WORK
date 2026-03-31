# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.

a = int(input('Enter First Angle (a) :'))
b = int(input('Enter Second Angle (b) :'))
c = int(input('Enter Third Angle (c) :'))

if(a + b + c == 180):
    print("Triangle is Valid.")

else :
    print("Triangle is not valid.")