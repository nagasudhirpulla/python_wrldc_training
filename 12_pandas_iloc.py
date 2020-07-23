'''
Lesson 1 - Day 3 - Pandas DataFrame iloc function 
iloc function is used to access dataframe data by specifying the position of row or column index
'''
# %%
import pandas as pd

# %%
# use 'skiprows' to skip lines at the top of the file
# use 'skipfooter' to skip lines at the bottom of the file
# use 'nrows' to capture only the specified number of rows
df = pd.read_csv('data/dc_data.csv', skiprows=2, skipfooter=6)

# %%
# get the shape of dataframe in the form (nrows, ncols) using shape attribute
dfShape = df.shape
print('The shape of dataframe is {0}'.format(dfShape))
print('Number of rows of dataframe is {0}'.format(dfShape[0]))
print('Number of columns of dataframe is {0}'.format(dfShape[1]))


# %%
# export the excel as csv using 'to_csv' function
# use index=False to exclude index in output file
# use header=False to exclude column names in output file
df.to_csv('data/out.csv', index=False)

# %%
# export the excel as csv using 'to_csv' function
df.to_excel('data/out.xlsx', index=False)


# %%
# using iloc function to access a cell of dataframe by its index adress
# getting the data cell of 7th row, 15th column
cellVal = df.iloc[6, 14]
print('The cell value at 7th row, 14th column is {0}'.format(cellVal))

# %%
# get the 6th row value of the column named 'KHARGONE-I(3)'
cellVal = df['KHARGONE-I(3)'].iloc[5]
print(
    'The cell value at 6th row of KHARGONE-I(3) column is {0}'.format(cellVal))

# %%
# using iloc function to access a subset of dataframe by its index and column adress ranges
# get the cells from 9 to 13 row indexes and 8 to 11 column indexes
dfSubset = df.iloc[9:14, 8:12]
print(dfSubset)

# %%
# get the cells from 9 to 13 row indexes but all columns
dfSubset = df.iloc[9:14, :]
print(dfSubset)

# %%
# get the cells from 8 to 11 column indexes but all rows
dfSubset = df.iloc[:, 8:12]
print(dfSubset)

# %%
# access only a list of column names
dfSubset = df[['Time Block', 'KAPS(0)', 'KHARGONE-I(3)']]

# %%
# select only the rows in which 'Time Block' column value is between 10 and 21
dfSubset = df[(df['Time Block'] >= 10) & (df['Time Block'] <= 21)]

# %%
# select only the rows in which 'Time Block' column value is between 10 and 21
# and only the generators 'CGPL(0)', 'KAWAS-APM(0)', 'LARA-I(0)'
dfSubset = df[(df['Time Block'] >= 10) & (df['Time Block'] <= 21)][['Time Block', 'CGPL(0)', 'KAWAS-APM(0)', 'LARA-I(0)']]
