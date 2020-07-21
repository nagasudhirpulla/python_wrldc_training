'''
Day 2 - Lesson 4
Dictionaries in python
'''

# %%
# create an example dictionary
xDict = {
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

# %%
# access all the keys of a dictionary using 'keys' function
xKeys = list(xDict.keys())
print('The keys of dictionary are ...')
print(xKeys)

# %%
# access all the values of a dictionary using 'values' function
xVals = list(xDict.values())
print('The values of dictionary are ...')
print(xVals)

# %%
# get all the values types of dictionary into an array using list comprehension
typesArr = [type(x) for x in xDict.values()]
print(typesArr)

# %%
# inserting/editing a key-value pair in a dictionary
xDict['location'] = 'Mumbai'

# %%
# accessing dictionary values
outputStatement = 'The person name is {0} {1}.\nHe lives at {2}, his hobbies are {3}.\nHe knows {4}'\
.format(xDict['firstName'], xDict['lastname'], xDict['location'],
        ', '.join(xDict['hobbies']), ', '.join(xDict['metaData']['languages']))
print(outputStatement)


# %%
