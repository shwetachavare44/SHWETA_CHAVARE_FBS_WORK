#Q. 3 Salary Calculation

n = int(input("Enter number of employees: "))
total_salary = 0

for i in range(1, n+1):
    basic = float(input("Enter basic salary: "))

    if basic < 20000:
        da = 0.10 * basic
        ta = 0.12 * basic
        hra = 0.15 * basic
    else:
        da = 0.15 * basic
        ta = 0.18 * basic
        hra = 0.20 * basic

    total = basic + da + ta + hra
    print(f"Total salary of employee is {total}")

    total_salary = total_salary + total

print(f"Total salary of all employees are {total_salary}")