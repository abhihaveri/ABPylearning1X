# exception
#abnormal event during a execution of a program, But it can be handled

#error --> mistake by Devs-->specific to code--> 1gb -->1.2gb stckoverflow erroe
# 10 , 12 - Error --> It very difficult to overcome
# Memory Error

# a=10/0

try:
    #code which you think can give your exception
    a = 10 / 0
except ZeroDivisionError:
    print("Your are doing division by Zero")

print ("enter the card ")
try:
    b=10/0
except Exception as e:
    print("xx Error due to number divided by zero")

print ("Take the card ")
