'''
Pandas DataFrame loc function 
loc function is used to access dataframe data by specifying the row index values or column values
'''
#%%
import pandas as pd

# create a dataframe
df = pd.DataFrame([[2, 3], [5, 6], [8, 9]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])
print(df)

# %%
# select rows with index as 'viper', 'cobra' but all columns
df2 = df.loc[['viper', 'cobra'], :]

# %%
# select rows with index as 'viper', 'cobra' and columns as 'max_speed'
df2 = df.loc[['viper', 'cobra'], ['max_speed']]

# %%
