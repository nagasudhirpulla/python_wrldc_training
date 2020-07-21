'''
Lesson 3
Using if, elif, else in python
'''

x = 10

if x == 1:
    print('processing...')
    print('x is one')
elif x==2:
    print('processing...')
    print('x is two')
elif x==4:
    print('processing...')
    print('x is four')
else:
    print('processing...')
    print('condition not hit :-(')
    print('x is {0}'.format(x))

print('execution complete')