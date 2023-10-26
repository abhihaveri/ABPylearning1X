'''digit=1234
mod=digit%10
print(mod)
digit=123
mod1=digit%10
print(mod1)'''


num =int(input('please enter a number\n'))
sum=0
while num!=0:
    digit=num%10
    sum=sum+ digit
    num =int (num /10)

print(sum)