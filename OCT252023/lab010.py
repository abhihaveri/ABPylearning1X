# map and filter in the List

square = lambda x: x * x
result = square(5)
print(result)

# Map Functions
numbers = [1, 2, 3, 4, 5]
square_list = []
for i in numbers:
    square_list.append(square(i))
print(square_list)

# we can do the same thing using Map function
'''square = lambda x: x * x
square_list = []
for i in numbers:
    square_list.append(square(i))'''
sq_number2 = list(map(lambda x:x*x ,numbers))
print(type(sq_number2))
print(sq_number2)

# generaly Map is adviceble to use for lambda expressions:-
def triple(a):
    return a*3
sq_number3= list(map(triple,numbers))
print(numbers)
print(sq_number3)

