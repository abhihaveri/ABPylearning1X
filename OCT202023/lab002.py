# functions

output =max(1,3) # built in function
print(output)

# Block of code
# 1. build in - which are created by python people
# for you so that you ca use them without
# creating your own


# Custome funtion - you can create a func which is a block of code anyone can reuse it

'''a=int(input ("enter a\n"))
b=int(input ("enter b\n"))
print(a+b)'''

# writtem some code

def sum(a,b):
    return a+b
a=int(input ("enter a\n"))
b=int(input ("enter b\n"))
print(f'the sum {a},{b} is ::{sum(a,b)}')

