#Q1. Login with 3 attempts

user_id_correct = "admin"
user_pass_correct = "1234"

for i in range (3):
    user_id = input("Enter user Id :")
    user_pass = input("Enter user Password:")

    if user_id_correct == user_id and user_pass_correct == user_pass :
         print("Login Successful!")
    else:
         print("Invalid Credential")
else :
     print("Account Locked!")          
              