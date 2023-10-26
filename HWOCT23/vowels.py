# Program to find Number of Vowels in a given string ::

x=input('please enter the string \n')

vowels=['a','A','e','E','i','I','o','O','u','U']
count =0

# using for-each loop, character is reference to a letter in the string
for character in x:
    if character in vowels:
        count+=1
print("The Number of vowels in given string is ::",count)