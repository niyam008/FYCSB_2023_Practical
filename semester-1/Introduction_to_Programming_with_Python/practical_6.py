#### Date: Mon, Sep 04th 2023

### file: practical_6.py

'''
Write Python program to implement and use lambda function in python
'''

# anonymous function

sum = lambda n1, n2: n1 + n2

print('Total =',sum(13,20))
print('Total =',sum(21,41))


g = lambda x: x**2

print('Square of a number :',g(8))

nums = range(2,50)

for i in range(2,8):
    nums=filter(lambda x: x==i or x % i , nums)

d = lambda x:x*2

print(d(5))
