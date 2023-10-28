squares=[1,4,9,16,25]
my_list=[True,1,2,3,'A']

#my_list.sort() #TypeError: '<' not supported between instances of 'str' and 'int'
print(my_list)

l=squares
l2=squares.copy()
print(squares)
print(l)
print(l2)
squares[0]=22
print(squares)
print(l)
print(l2)

