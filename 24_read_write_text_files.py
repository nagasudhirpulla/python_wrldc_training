'''
Lesson 2 - Day 4 - read or write text files in python
'''

# %%
# read a text file
# open the file for reading
with open("dumps/test.txt", mode='r') as f:
   # read all the file content   
   fStr = f.read()
   # please note that once again calling f.read() will return empty string
   
   print(fStr)
   # this will print the whole file contents

# %%
# load all lines into a list
with open("dumps/test.txt", mode='r') as f:
   # load all the lines of the file into an array
   textLines = f.readlines()
   
   print(textLines)

# %%
# writing text to a file
# with mode = 'w', old text will be deleted
# with mode = 'a', the new text will be appended to the old text
with open("dumps/test.txt", mode='w') as f:   
   f.write("The first line\n")
   f.write("This is the second line\nThis the third line")

# %%
