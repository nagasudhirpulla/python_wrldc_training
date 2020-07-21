'''
Day 2 - Lesson 1
Lists in python
'''


lst = [1, 2, 3, 'asdas', 'dfwa']

# find the length of list using 'len' function
lstLen = len(lst)
print('length of list is {0}\n\n'.format(lstLen))

# access a list item using its zero-indexed position
thrdVal = lst[2]
print('Third value in list is {0}\n\n'.format(thrdVal))

# append a value to a list using 'append' function
newVal = 10
lst.append(newVal)
print('New list after appending a value is...')
print(lst)
print('\n\n')

# append a list of values using 'extend' function
newValsLst = [15, 'abc', 48]
lst.extend(newValsLst)
print('New list after appending a list is...')
print(lst)
print('\n\n')

# insert a value at a desired position in the list using 'insert' function
lst.insert(0, 'xyz')
print('New list after inserting at the start is...')
print(lst)
print('\n\n')

# find the position of a value in a list using 'index' function
posOf15 = lst.index(15)
print('15 is at the position {0} in the list'.format(posOf15))
print('\n\n')

# create a list from another list using 'list comprehension' with filtering only numbers
numLst = [x for x in lst if not(isinstance(x, str))]

# implementing the above statement using for loop
numLst = []
for x in lst:
    if not(isinstance(x, str)):
        numLst.append(x)

print('numbers in the list = {0}'.format(numLst))
print('\n\n')


# sort the list of values using the 'sorted' function
sortedLst = sorted(numLst)
print('New list after sorting is...')
print(sortedLst)
print('\n\n')

# sort the list of values in descending order using the 'sorted' function with reverse input as True
sortedLst = sorted(numLst, reverse=True)
print('New list after descending sorting is...')
print(sortedLst)
print('\n\n')

# slicing the list from a desired position till end
slicedLst = numLst[2:]
print('New list after slicing from 2nd position till end is...')
print(slicedLst)
print('\n\n')

# slicing the list between two desired positions
slicedLst = numLst[2:5]
print('New list after slicing from 2nd position till 4th position is...')
print(slicedLst)
print('\n\n')

# slicing the list with negative indexes for position from last
slicedLst = numLst[2:-2]
print('New list after slicing from 2nd position from start till 2nd position from end...')
print(slicedLst)
print('\n\n')

# importing the copy module
import copy
# clone the list using copy module
revLst = copy.copy(numLst)
# reverse a list using 'reverse' function
revLst.reverse()
print('Reversed list is ...')
print(revLst)
print('\n\n')

# 