# 7. Write a program to check if user has entered correct userid and password.

uid = input('Enter User id :')
pwd = input('Enter Password :')

if(uid == 'Admin' and pwd == '9875'):
    print('Login Successful!')

else :
    print('Wrong user id or password')