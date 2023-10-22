'''Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.
n = 12345
sum = 15

n = 123
sum = 6'''

def sum(n):
   # n='123'
    sum=0
    for i in n:
        sum=sum+int(i)
    return(sum)
n =input('Please enter a number: \n')
print(sum(n))