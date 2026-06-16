li = [10, 22, 35, 54, 22, 35, 76]

num = int(input("Enter your number:"))
count = 0

for i in li:
    if i == num:
        count += 1

if count > 0:
    print("Present",count, "times")
else:
    print("Not prsent")
