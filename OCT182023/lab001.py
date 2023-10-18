year =2027
is_a_leap_Year= False

if (year%4==0 and year%100 !=0) or (year%400==0):
    is_a_leap_Year=True
'''else:
    is_a_leap_Year=False'''
print(f'{year} is {is_a_leap_Year}')