#Write a Python program to find the smallest number in a list.
x=input('please enter the List seperated by comma :\n').split(',')
#x=[11,687,53,420,5]
y=min(x)
x.sort()
z=x[0]
print('The User Input List is\n',x)
print('The Max Number using min-list function ::\t',y)
print('The Max Number using sort and Index function ::\t',z)