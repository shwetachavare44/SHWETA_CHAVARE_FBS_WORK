def is_leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return y
    return False
res = is_leap_year(2009)

if res:
    print(f"{res} is leap year.")
else :
    print(f"{res} is not leap year.")