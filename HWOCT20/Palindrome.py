'''Palindrome Checker:
Create a function that checks if a given string is a palindrome (reads the same forwards and backward). 121
Example - pramod
madam - reverse(madam) -> same
Naman -> reverse -> same
Malayalam
Compare String with the Revserse of the string'''
'''a='Abhi'
b=a[::-1]
print(a)
print(b)
'''
def ispalindrome(a):
    a=a.upper()
    b=a[::-1]
    if a==b:
        return 'is a palindrome'
    else:
        return 'is not a palindrome'

a=input('please enter the string\n')
print(ispalindrome(a))