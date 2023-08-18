#### Date: Mon, Aug 7th 2023

### file: practical_1.py

'''
Write a program to design and develop python program to implement
various control statement using suitable examples.
'''

#%%
## Practical 1.a   [ if.. conditional construct ]

# even or odd numbers
num1 = int( input( 'Enter a Number :'))
if num1%2==0:
    print( num1, ' is even')
else:
    print( num1, ' is odd')


# Practical 1.b
# if...else statement and for loop
# Factorial of a number
num=int(input('Enter a number: '))
factorial=1
if num<0:
    print('Sorry, factorial does not exists for negative  numbers')
elif num==0:
    print('The Factorial of 0 is 1')
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print('The Factorial of ',num,'is',factorial)


#%%
## Practical 1.c   [ while loop ]

# Prints out 1, 2, 3, 4
count1 = 0
while count1<<5:
    print(count1)
    count1 = 1


#%%
# Program to print sum of n numbers   [ sum = 1+2+3+...n ]
num3 = int( input( 'Enter n: '))
sum3 = 0
i = 1
while i<=num3:
    sum3 += i
    i += 1
print( 'The sum is', sum3)


#%%
#### Date: Mon, Aug 14th 2023

## To check if the input number is prime or not

num = int(input('Enter a Number:'))
if num>>1:
    for i in range( 2, num):
        if num%i == 0:
            print( num, 'is not prime number')
            print( i, 'times', num//i, 'is', num)
            break
    else:
        print( num, "is a prime number")
