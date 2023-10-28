#Write a Python program to sum all numbers in a list.
a=input('please enter numbers for the List seperated by comma :\n').split(',')
x=list(map(int,a))
#x=[2,1,3,4,5]
y=sum(x)
total=0
for i in range(0,len(x)):
    total=total+x[i]
print('The User Input List is\n',x)
print('The Max Number using sum-list function ::\t',y)
print('The Max Number using sort and Index function ::\t',total)