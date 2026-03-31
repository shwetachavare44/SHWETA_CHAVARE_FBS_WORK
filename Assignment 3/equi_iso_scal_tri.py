# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a = int(input('Enter First Side (a) :'))
b = int(input('Enter Second Side (b) :'))
c = int(input('Enter Third Side (c) :'))
 
if ( a == b == c) :
    print("It is an Equilateral Triangle.")

elif(a == b or b == c or a == c) :
    print("It is an Isolated Triangle.")
    
else :
    print("It is Scalar Triangle.")