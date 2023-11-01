numbers =[1,-2,-3,-4,5,6,-7,8,-9,10]
def is_positive(num):
    return num >0

def is_negative(num):
    return num <0

positives=list(filter(is_positive,numbers))
print(positives)
positives=list(map(is_positive,numbers))
print(positives)
negative=list(filter(is_negative,numbers))
print(negative)