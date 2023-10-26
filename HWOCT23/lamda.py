#Create a Lambda expression to triple power 2**3 a number
x=int(input('please enter a number\n'))
cube = lambda x : x**3
print(f"The Cube of given number {x} ,using lambda function is {cube(x)}")
