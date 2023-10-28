# Write a Python program to count the number of strings in a list where the string length is 2 or more and the first and last character
# are the same.
a = input('please enter string for the List seperated by comma :\n').split(',')
if len(a)>=2 and a[0]==a[-1]:
    x=len(a)
    print('The Length of the String is ::',x)
else:
    print('The Length of the string is less than 2 or the 1st and last character of the string is not same!!')


