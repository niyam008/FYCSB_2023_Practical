#### Date: Mon, Jul 31th 2023

### file: age_cal.py

## for calculating the age using birth year and current year
name = input( 'Enter your Name : ')
yob = int( input( 'Enter your birth year : '))
current_year = int( input( 'Enter current year : '))
age = current_year - yob
print( 'Dear', name, "!!! You are", age, 'year old')

### file: area.py

## for finding area of Rectangle
width = float( input( 'Enter the Width of Rectriangle : '))
height = float( input( 'Enter the Height of Rectriangle : '))
area = width * height
print('Area of a rectange is: ',area)

print()
## python program to find the area of circle
pi = 3.14
radius = float( input( 'Please Enter the Radius of Circle : '))
area = pi*( radius**2)
print( 'Area for Circle = ',area)

### file: swap.py

## program to swap two numbers
x = input( 'Enter value of x : ')
y = input( 'Enter value of y : ')
print( 'Before Swapping')
print( 'x = ', x)
print( 'y = ', y)
temp = x
x = y
y = temp
print('\nAfter Swapping')
print( 'x = ', x)
print( 'y = ', y)
