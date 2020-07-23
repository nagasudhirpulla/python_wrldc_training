'''
Lesson 9 - Day 3 - functions in python
'''
# %%
def sayHello(nameInp):
    print('executing say hello function...')
    return 'Hello {0}!, how are you...'.format(nameInp)

greeting = sayHello('Nagasudhir')
print(greeting)

names = ['Person1', 'Person2', 'Person3']
for p in names:
    print(sayHello(p))

# %%
