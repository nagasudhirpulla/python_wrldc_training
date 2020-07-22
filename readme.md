## Python session on 20 Jul 2020

### Software installed
* python - for running python
* Visual Studio Code / VS Code - code editor for python code
* git - source control system for managing python code

### Topics covered
* Opened a folder in vs code
* Created a new python file
* print hello world using 'print' function in python
* commenting python code using '#'
* multi line commenting of python code using '''
* create variables (like strings and numbers) in python
* formatting strings with variable substitution in python
* if, else, elif in python
* while statement in python
* for statement in python
* intro to using git

### initialize a git repository in a folder
* In the folder right click->open git bash here
* use command 'git init'
* use command 'git status' to see the status of files
* use command 'git add .' to add all untracked files and changes for staging to get committed
* use command git commit -am 'commit comment' to commit the changes of your code to git 

## Python session on 21 Jul 2020, day 2

### pushing code to remote git repositories like GitHub
* Create an account in sites like GitHub, Bitbucket
* Create a repository in your account
* In the folder right click and select 'Git bash here' to open git command prompt
* add remote repo url to local git using the command ```git remote add origin <your_repo_url>```
* Pull remote code to local git folder using the command ```git pull origin master```
For unrelated histories issue use command ```git pull origin master --allow-unrelated-histories```
* Push code to remote repository using the command ```git push origin master```

### VS Code shortcuts
* ```Ctrl /``` to comment /uncomment code
* ```Alt Shift F``` to format the code
* ```Ctrl s``` to save files
* ```Ctrl +``` to zoom in, ```Ctrl -``` to zoom out
* ```Ctrl ~``` to open/close command prompt

### Lists in python
* find the length of list using 'len' function
* access a list item using its zero-indexed position
* append a value to a list using 'append' function
* append a list of values using 'extend' function
* insert a value at a desired position in the list using 'insert' function
* find the position of a value in a list using 'index' function
* create a list from another list using 'list comprehension' with filtering only numbers
* adding numbers to a list repeatedly using 'for' loop and 'append' functions
* sort the list of values using the 'sorted' function
* sort the list of values in descending order using the 'sorted' function with reverse input as True
* clone the original list to another variable using 'copy' module
* slicing the list
* clone the list using copy module
* reverse a list using 'reverse' function

### using jupyter cells in python for easy debugging
* use ```# %%``` to create a jupyter cell in python code

### type of variable
* use 'type' function to get the type of variable
* check the type of variable using 'isinstance' function

### dictionaries in python
* create an example dictionary
* access all the keys of a dictionary using 'keys' function
* access all the values of a dictionary using 'values' function
* get all the values types of dictionary into an array using list comprehension
* inserting/editing a key-value pair in a dictionary
* accessing dictionary values

### installing modules using pip install command

### read command line inputs using the 'argparse' module

### 'Pandas' DataFrame
* Intro and terminologies in a pandas dataframe
* create a dataframe from list of lists
* read dataframe from a csv file using 'read_csv' function
* get all the column names of the dataframe using the 'columns' attribute
* get all the items of a specific column name
* filtering the rows of a dataframe based upon its column values