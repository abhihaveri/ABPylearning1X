# Fibonacci Series :: Take an input and print the series.
#Research What is Fibonacci series and Factorial.
n=int(input('Please enter a number :\n'))
a=0
b=1
if n==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        b=a
        a=c
        print(c)