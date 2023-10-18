'''2. Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number'''
print('\n The Program to compare two numbers')
x=float(input('enter the first number \n'))
y=float(input('enter the second number \n'))

result = "greater than" if x>y else "less than" if x<y else "Equal to"
print(f"{x} is {result} {y} ")