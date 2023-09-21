#### Date: Mon, Sep 17th 2023

### file: practical_10.py

'''
Write a program to implement dictionary in Python for suitable
problem. Demonstrate various operations on it.
'''


#   dictionary methods

dict1 = { 'name':'student', 'age':20, 'class':'FYCS'}
dict2 = dict1.copy()
print('Copied dictionary:',dict2)
print('Dictionary keys:',dict1.keys())
print('Dictionary Values:',dict1.values())
print('Printing dictionary:',dict1.items())
dict3 = {'ddress':'Nerul'}
dict1.update(dict3)
print('Updated dictionary:',dict1)
print("Value of 'Name':",dict1.get('Name'))
seq1 = ('name','age','class','address')
dict4=dict1.fromkeys(seq1)
print('New dictionary:',dict4)
