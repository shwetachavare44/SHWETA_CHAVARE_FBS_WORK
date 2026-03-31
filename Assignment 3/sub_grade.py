# 9. Input 5 subject marks from user and display grade(eg.First class, Second class...)

sub1_marks = float(input('Enter sub1 Marks: '))
sub2_marks = float(input('Enter sub2 Marks: '))
sub3_marks = float(input('Enter sub3 Marks: '))
sub4_marks = float(input('Enter sub4 Marks: '))
sub5_marks = float(input('Enter sub5 Marks: '))

student_marks = sub1_marks + sub2_marks + sub3_marks + sub4_marks + sub5_marks
total_marks = float(input('Enter Total Marks: '))

percentage = student_marks / total_marks * 100
print(f'You got {percentage}%')

if(percentage >= 70):
    print('First Class')

elif(percentage >= 60):
    print('Second Class')

elif(percentage >= 50):
    print('Third Class')
else :
    print('Fail')

