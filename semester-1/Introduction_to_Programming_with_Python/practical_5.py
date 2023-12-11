#### Date: Mon, Aug 28th 2023

### file: practical_5.py

'''
Write suitable Python program to implement recursion for problems such as Fibonacci
series, Factorial, Tower of Hanoi etc.
'''

## Practical 5.a

'''
Write suitable Python program to implement recursion for problems
such as Fibonacci series
'''

# fibonaci using recursion

def recur_fibo(n):
    if n<=1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)

nterms = int(input('Enter how many numbers you want to see? '))

if nterms<=0:
    print("Please enter a positive integer.")
else:
    print('Fibonacci Square')
    for i in range(nterms):
        print(recur_fibo(i))


# $$ $$ $$ $$ $$
print()

#### Date: Mon, Sep 04th 2023

## Practical 5.b
# factorial using recursion

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x*factorial(x-1))

num = int(input('Enter a number :'))
print("The factorial of",f'{num}!','is',factorial(num))


# $$ $$ $$ $$ $$
print()

## Practical 5.c
# Tower of Hanoi

def moveTower(height, fromPole, toPole, withPole):
    if height>=1:
        moveTower(height -1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print('Moving disk from', fp,'to',tp)

moveTower(3,'A','B','C')


