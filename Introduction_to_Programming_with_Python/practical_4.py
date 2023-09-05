#### Date: Mon, Aug 28th 2023

### file: practical_4.py

'''
Write a Python program to demonstrate the precedence and associativity of operators.
'''

a=20
b=10
c=15
d=5

#operator precedence
print('b+a*c =',b+a*c)
print('(b+a)*c =',(b+a)*c)
print('a+b/d =',a+b/d)

#associativity of operator
print('(a+b)+c =',(a+b)+c)
print('a+(b+c) =',a+(b+c))

print('(a/b)/c =',(a/b)/c)
print('a/(b/c) =',a/(b/c))
