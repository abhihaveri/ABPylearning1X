# try except
# try:
#     a=10/0
# except ZeroDivisionError as e:
#     print('error')
#
# try except and nested except
try:
    num1=int(input("enter a number"))
    num2=int(input("enter a number"))

    result = num1/num2

except ZeroDivisionError:
    print("Zero Cannot be Divided i.e num2")
except ValueError:
    print("Invalid Input")
else:
    print(f"result is {result}")
finally:
    print("I will always execute")