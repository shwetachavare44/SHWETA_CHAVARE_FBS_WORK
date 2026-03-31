# Python Assignment-1 (Basics)

# 1. Write a program to calculate the percentage of student based on marks of any 5 subjects.

sub1_marks = float(input('Enter sub1 Marks: '))
sub2_marks = float(input('Enter sub2 Marks: '))
sub3_marks = float(input('Enter sub3 Marks: '))
sub4_marks = float(input('Enter sub4 Marks: '))
sub5_marks = float(input('Enter sub5 Marks: '))

student_marks = sub1_marks + sub2_marks + sub3_marks + sub4_marks + sub5_marks
total_marks = float(input('Enter Total Marks: '))

percentage = student_marks / total_marks * 100

print(f'Your total score is {percentage} %.')