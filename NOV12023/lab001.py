# Filter Function
numbers =[1,2,3,4,5,6,7,8,9,10]

#even_numbers=[2,3,4,6,8,10]
#Filter--> Number of elements can be less or equal to list

def is_even(num):
    return num %2==0
op =is_even(3)
print(op)
op =is_even(10)
print(op)

even_numbers_list= list(filter(is_even, numbers))
even_numbers_list= list(map(is_even, numbers))
print(even_numbers_list)