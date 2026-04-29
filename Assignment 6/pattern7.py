#      A 
#     A B C 
#    A B C D E 
#   A B C D E F G 
#  A B C D E F G H I 

n = 5
char_code = 65

for i in range(1, n + 1):
    print(" "*(n-i), end=" ")

    num_chars = 2 * i - 1
    for j in range(num_chars):
        print(chr(64 + (j + 1)), end=" ")
        
    print()