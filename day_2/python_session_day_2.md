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
* TODO write topics

### installing modules using pip install command

### reading command line inputs using 'argparse' module