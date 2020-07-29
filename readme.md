This code base is created with a goal of creating a knowledge base and uniform coding practices/habits among the developers therby aiding easier learning and collaboration

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

## Python session on 21 Jul 2020, day 2

### pushing code to remote git repositories like GitHub

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
* get all desired command line inputs into an object

### 'Pandas' DataFrame Introduction
* Intro and terminologies in a pandas dataframe
* create a dataframe from list of lists
* read dataframe from a csv/excel file using 'read_csv', 'read_excel' function
* get all the column names of the dataframe using the 'columns' attribute
* get all the items of a specific column name
* filtering the rows of a dataframe based upon its column values

## Python session on 23 Jul 2020, day 3
### 'Pandas' DataFrame concepts
* Pandas dataframe excel/csv loading options sheet_name, skiprows, skipfooter, nrows, usecols
* get the shape of dataframe in the form (nrows, ncols) using shape attribute
* Pandas export csv or excel using 'to_csv', 'to_excel' methods
* using iloc function to access a cell of dataframe by its index adress
* using iloc function to access a subset of dataframe by its index and column adress ranges
* pandas loc function to access dataframe data by specifying the row index values or column values
* make a column as index in a pandas DataFrame
* calculate average value of a dataframe column using mean() function
* calculate sum of a dataframe column using sum() function
* calculate aggregation of dataframe using 'for' loop
* create a new column in a dataframe

### 'Matplotlib' module for plotting
* Basic line plot
* set title for the plot
* set label to x and y axes
* enable legends for the plot
* control the location of legends in the plot
* save the figure as png/pdf/jpg using savefig function
* changing color of the line plot
* changing linestyle can be 'solid', 'dashed', 'dashdot', 'dotted', 'None'
* plot markers in the plot
* control plot markers style and size

### Multiple plots in one figure
* Multiple lines in one plot using ax.plot function
* use subplots function to create multiple plots in one figure
* iterate through each axis through reshape
* set the figure title

### sizing the plots
* using figsize option in subplots function to control size in inches

### centering of matplotlib axes so that 0,0 point is in the middle of the figure
* hiding/changing the color of spines
* setting the position of spines

## Python session on 24 Jul 2020, day 3
### functions

### functions and variables in diffrerent files and folders for implementing Separation of Concerns paradigm

### using glob module for iterating files of a folder
* iterate through all the files of a folder
* iterate through all the files of a desired file extension in a folder

### read and write text files
* using read mode, write mode, append mode while reading and writing files

### datetime module in python
* get the current time
* create a desired datetime object using dt.datetime function
* using strftime to print datetime in a desired format like %d-%m-%Y %H:%M:%S
* using strptime to derive datetime object from string
* convert string type pandas dataframe column to datetime column
* access the components of a datetime object

### timedeltas in datetime module
* create a desired time interval using dt.timedelta function
* get the difference between 2 datetimes
* access the components of a timedelta object
* get the total seconds in the time span using total_seconds function
* add time period to existing time period

### using pyinstaller to deploy a python script as an executable

### using smtplib module to send mail from posoco mail id

### using psycopg2 module to interface with a postgreSQL database


