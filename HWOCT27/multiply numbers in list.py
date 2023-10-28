#Write a Python program to multiply all numbers in a list.
import math
a=input('please enter numbers for the List seperated by comma :\n').split(',')
x=list(map(int,a))
#x=[2,1,3,4,5]
y=math.prod(x)
prod=1
for i in range(0,len(x)):
    prod=prod*x[i]
print('The User Input List is\n',x)
print('The Max Number using math Prod  function ::\t',y)
print('The Max Number using sort and Index function ::\t',prod)