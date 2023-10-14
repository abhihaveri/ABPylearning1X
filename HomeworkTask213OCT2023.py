#Task #2
'''1. Write a Python program to calculate the area of a circle given its radius using the formula area=π×r^2 ( Take pie as 3.14)'''
print('\n The Program to find area of circle using radius as input')
radius=float(input('enter the radius of the Circle\n'))
print(f'{(radius**2)*3.14} is the area of the circle for the given Radius equal to {radius}')

'''2. Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number'''
print('\n The Program to compare two numbers')
x=float(input('enter the first number \n'))
y=float(input('enter the second number \n'))
print('the numbers are equal' if x==y else 'The first number is greater' if x>y else 'The second number is greater')

'''3. Use the ternary operator to find the maximum of three numbers entered by the user.'''
print('\n The ternary Magic Program to find max of three numbers')
a=float(input('enter the first number \n'))
b=float(input('enter the second number \n'))
c=float(input('enter the third number \n'))
print(f'The 1st number {a}  is greater ' if a>b and a>c else f'The 2nd number {b}  is greater' if b>a and b>c else f'The 3rd number {c} number is greater')

'''4. Develop a Python script that calculates the square and cube of a given number.'''
print('\n programe to find square and cube of a number')
number=int(input('Please enter a number\n'))
print(f'The Cube of the {number} is {number**3}, The Square of the {number} is {number**2}')