'''
Day 2 - Lesson 3
Type of varibles in python
'''
# %%
x = 8

typ = type(x)
print(typ)

# %%
x = 5.5

typ = type(x)
print(typ)

# %%
x = "abcs"

typ = type(x)
print(typ)

# %%
x = [1, 'n', 5]

typ = type(x)
print(typ)

# %%
x = {
    'firstName': 'Nagasudhir',
    'lastname': 'Pulla',
    'age': 28,
    'hobbies': ['tv', 'playing', 'youtube'],
    'metaData': {
        'proficiency': 'level 1',
        'designation': 'Deputy Manager',
        'department': 'IT',
        'languages': ['C#', 'Javascript', 'HTML', 'CSS', 'typescript', 'python']
    }
}

typ = type(x)
print(typ)

# %%
# check the type of variable using isinstance function
x = 15.6
isNum = isinstance(x, float) or isinstance(x, int)
print(isNum)


# %%
