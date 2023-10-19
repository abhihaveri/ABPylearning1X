# factorial Function ::::
import math
number = int(input('Please enter a number which you want Factorial to be calculated:\n'))
fact=1

for i in range(1,number+1):
    fact=fact*i
print(f'The Factorial for  {number} is {fact}')
print(f'The Factorial using math  the {number} is {math.factorial(number)}')