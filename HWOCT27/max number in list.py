# Write a Python program to find the largest number in a list.
x=input('please enter the List seperated by comma :\n').split(',')
#x=[11,687,53,420,5]
y=max(x)
x.sort()
z=x[-1]
print('The User Input List is\n',x)
print('The Max Number using Max-list function ::\t',y)
print('The Max Number using sort and Index function ::\t',z)
