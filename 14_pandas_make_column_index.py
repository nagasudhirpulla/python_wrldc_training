'''
Lesson 3 - Day 3 - make a column as index in a pandas DataFrame 
'''

# %% 
import pandas as pd

# %%
# read dc data from csv and skip first 2 rows and skip last 6 rows
df = pd.read_csv('data/dc_data.csv', skipfooter=6, skiprows=2)


# %%
# make the column 'Time Block' as index
df = df.set_index('Time Block')

# %%
# access the rows with index from 10 to 21
dfSubset = df.loc[range(10,22), :]
