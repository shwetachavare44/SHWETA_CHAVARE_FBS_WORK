# 10. Write a program to check if person is eligible to marry or not (male age 21 and female age-18)

gender = input("Enter Gender(M/F) :")
age = int(input('Enter Age:'))

if gender in (['F', 'f', 'FEMALE', 'Female', 'female']):
    if(age >= 18):
        print('Eligible for marriage.')
    else:
        print('Not Eligible for marriage.')
        
else :
    if(age >= 21):
        print('Eligible for marriage.')
    else:
        print('Not Eligible for marriage.')