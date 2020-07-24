'''
Lesson 1 - Day 4 - iterate thorough all files of a folder using glob module
'''
# %%
import glob

# %%
# iterate through all filenames in a folder
for fName in glob.glob('data/*'):
    print('filename is {0}'.format(fName))
    print('processing it...')

# %%
# get all filenames of the folder in an array

fNames = [fName for fName in glob.glob('data/*')]

# %%
# iterate through xlsx files only in a folder
for fName in glob.glob('data/*.xlsx'):
    print('filename is {0}'.format(fName))
    print('processing it...')

# %%
