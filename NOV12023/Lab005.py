numbers =[11,12,13,14,5,6,-7,8,-9,10]
'''def is_positive(num):
    return num >10'''
list_numbers_greater=tuple(filter(lambda num:num>10,numbers))
print(list_numbers_greater)