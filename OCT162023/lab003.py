'''3. Use the ternary operator to find the maximum of three numbers entered by the user.'''
print('\n The ternary Magic Program to find max of three numbers')
a=float(input('enter the first number \n'))
b=float(input('enter the second number \n'))
c=float(input('enter the third number \n'))

max_number = a if (a>b and a>c) else (b if b>c else c)

print(f'The maximum of the {a},{b},{c} is :: {max_number}')