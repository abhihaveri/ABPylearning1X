#Task #1
#1. Explain the difference between the = operator and the == operator in Python.
#answer
"""The '=' assigns a value to a variable , while '==' verifies the operands are equal
or not if equal it will return True , else False"""

x=2
y=3
print (f'{x} and {y}') #assignment
print(x==y) #False


#2. What does the ** operator do in Python, and how is it used?
#answer
'''its and Arthimatic operator i.e mathematical exponential operator'''

print('The exponentional of 3 power 2 is ',y**x)

#3. What does the ^ operator do in Python, and in what context is it commonly used?

'''^ is a XOR operator sets each bit to 1 if only one is 1,
if both are 1 or if both are 0 then it will set to 0'''

print(x ^ x)  # returns 0 as both are same here
print(y ^ x)  # returns 1 as both are different  here