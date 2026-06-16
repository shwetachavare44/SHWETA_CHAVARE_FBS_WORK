def is_palindrome(num):
    rev = 0
    while num > 0 :
        rev = rev * 10 + num % 10
        num //= 10
    return rev
def reverse_number(num):
    return num == reverse_number(num)

print(is_palindrome(121))