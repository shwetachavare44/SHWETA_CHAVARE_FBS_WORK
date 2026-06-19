def reverse(num, rev=0):
    if num == 0:
        return rev
    return reverse(num // 10, rev * 10 + num % 10)

num = int(input("Enter your Number:"))
print("Reversed Number:",reverse(num))