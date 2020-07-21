'''
Lesson 6 - Day 2 - Pandas DataFrame
* 'pandas' is a python library/module
* 'dataframe' is a data-structure provided by pandas.
It is just like excel sheet
* A dataframe as 'indexes' and 'columns'
'''
# %%
# import pandas module into a variable pd
import pandas as pd

# %%
# create a pandas dataframe from list of lists
dataArr = [
    ['PersonA', 12, 'male'],
    ['PersonB', 95, 'male'],
    ['PersonC', 84, 'female']
]

df = pd.DataFrame(dataArr,
                  columns=['name', 'age', 'sexuality'],
                  index=[114,546,987])

# %%
# read dataframe from a csv file using 'read_csv' function
df = pd.read_csv('data/personsDb.csv')

# %%
# get all the column names of the dataframe using the 'columns' attribute
colNames = df.columns.tolist()
print('The dataframe columns are {0}'.format(colNames))

# %%
# get all the names from the name column
names = df['name'].values.tolist()

print('All the names are {0}'.format(names))

# %%
# filtering the rows of a dataframe based upon its column values
# get the names of the people who are atleast 50 years
df2 = df[df['age']>=50]

# %%
# filter people who are male and atleast 50 years
df3 = df[(df['age']>=50) & (df['sexuality']=='Male')]

# %%
# get the names of only male people
df4 = df[df['sexuality'] == 'Male']
maleNames = df4['name'].values.tolist()
print('The male people are {0}'.format(', '.join(maleNames)))

# %%
