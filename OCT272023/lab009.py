num =30

def multiple_by_10(n):
    n*=10
    num =n  #changing thevalue inside the function
    print('Value of num inside function:',num)
    return n

op = multiple_by_10(num)
print(op)
print('Value of num outside function:',num)
