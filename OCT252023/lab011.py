# Filter

ages =[8,10,18,25,31]

def ages_func(x):
    if x<18:
        return False
    else:
        return True
adults= filter(ages_func,ages)
print(list(adults))