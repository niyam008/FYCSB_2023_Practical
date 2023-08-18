#### Date: Mon, Aug 14th 2023

### file: practical_3.py

'''
Write Python program to demonstrate different types of function arguments.
'''

# a simple calculator

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print('select operation:')
print('    1. Add')
print('    2. Substract')
print('    3. Multiply')
print('    4. Divide')

choice = int(input('Enter your Choice (1/2/3/4) :'))

if choice==1:
    n1 = int(input('Enter a Number: '))
    n2 = int(input('Enter a number: '))
    print(n1,'+',n2,'=',add(n1,n2))
elif choice==2:
    n1 = int(input('Enter a Number: '))
    n2 = int(input('Enter a number: '))
    print(n1,'-',n2,'=',subtract(n1,n2))
elif choice==3:
    n1 = int(input('Enter a Number: '))
    n2 = int(input('Enter a number: '))
    print(n1,'*',n2,'=',multiply(n1,n2))
elif choice==4:
    n1 = int(input('Enter a Number: '))
    n2 = int(input('Enter a number: '))
    print(n1,'/',n2,'=',divide(n1,n2))
else:
    print('invalid choice')
