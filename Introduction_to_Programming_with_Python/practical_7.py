#### Date: Mon, Sep 11th 2023

### file: practical_7.py

'''
Write a python program to create and manipulate array
in python. Also demonstrate use of slicing and indexing
for accessing elements of array
'''

# importing module
import array as a

print()
# creating an array
arr = a.array('i',[20,40,60,80,100])
print(arr)

print()
# manupulating an array
arr.insert(2,5)
print(arr)

print()
# indexing for accessing an array
print('First element :',arr[0])
print('Last element :',arr[-1])
print('Second element :',arr[1])

print()
# slicing for accessing an array
print('third to fifth \n',arr[2:5])
print('from begainning to third\n',arr[:3])
print('forth to end\n',arr[3:])
print('strat to end\n',arr[:])
