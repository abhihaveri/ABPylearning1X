'''Triangle Classifier:
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides, determine if the triangle is equilateral
(all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.'''

side1= float(input('enter the side one\n'))
side2= float(input('enter the side two\n'))
side3= float(input('enter the side three\n'))

if side1==side2 and side2==side3 and side3==side1:
    print(f'The Traingle is a equilateral Triangle as {side1},{side2},{side3}')
elif side1==side2 and side2!=side3 and side3!=side1:
    print(f'The Traingle is a isosceles Triangle as {side1},{side2},{side3}')
elif side1!=side2 and side2!=side3 and side3!=side1:
    print(f'The Traingle is a scalene Triangle as {side1},{side2},{side3}')