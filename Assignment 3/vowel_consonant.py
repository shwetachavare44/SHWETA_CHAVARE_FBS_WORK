# 2. Write a program to input any alphabet and check whether it is vowel or consonant.

x = input('Enter any Alphabet :')

if x in (['A'], ['a'], ['E'], ['e'], ['I'], ['i'], ['O'], ['o'], ['U'], ['u']):
    print(f"{x} is an Vowel.")
else :
    print(f'{x} is consonant.')