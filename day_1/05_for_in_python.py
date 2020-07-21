'''
Lesson 5 - 'for' statement in python and using it with 'range' function
'''

# looping for 10 times
for itr in range(10):
    print('executing...')
    print('x is {0}'.format(itr))

print('execution complete with range(10)...\n\n')

# looping with each element of an array
for itr in [1,5,8,7,45]:
    print('executing...')
    print('x is {0}'.format(itr))

print('execution complete with arrays...\n\n')

# looping on numbers from 4 to 8
for itr in range(4,9):
    print('executing...')
    print('x is {0}'.format(itr))

print('execution complete with range(4,9)...\n\n')

# looping on numbers from 4 to 11 with step interval of 2
for itr in range(4,12,2):
    print('executing...')
    print('x is {0}'.format(itr))

print('execution complete with range(4,12,2)...\n\n')

print('new changes')