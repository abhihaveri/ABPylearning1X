#Right Triangle Star Pattern
n= int(input(" please enter the number of rows"))
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print('')

# Inverted Right Angle triangle star

for i in range(n):
    for j in range(i,n):
        print("*",end=' ')
    print('')

# Right sided Traiangle

for i in range(n):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print('')

# Left sided Traiangle

for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n):
        print("*",end=' ')
    print('')
