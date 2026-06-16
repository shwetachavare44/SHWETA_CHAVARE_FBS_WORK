# 1 + 2+ 3+....+n

def sum_n(n):
    return(n * (n + 1) // 2)

res = sum_n(5)

print(f"sum upto num is : {res}")