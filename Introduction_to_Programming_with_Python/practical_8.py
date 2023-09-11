#### Date: Mon, Sep 11th 2023

### file: practical_8.py

'''
Write a python program to implement list in python for
suitable problem. demonstrate various operation on it.
'''

# list creation
fycs = [1,2,3,4,5]

print('Total elements:',len(fycs))
print('Min element:',min(fycs))
print('Max element:',max(fycs))
print("the elements of the list:\n",fycs)
print('First elements of the list:',fycs[0])
fycs.append(6)
print('Adding new elements:\n',fycs)
list1 = [10,20,30]
fycs.extend(list1)
print(fycs)
fycs.insert(4,90)
print(fycs)
fycs.pop()
print(fycs)
fycs.reverse()
print(fycs)
fycs.sort()
print(fycs)
