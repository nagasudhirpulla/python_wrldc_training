'''
perform aggregation on pandas dataframe
'''
# %% 
import pandas as pd

# %%
# read dc data from csv and skip first 2 rows and skip last 6 rows
df = pd.read_csv('data/dc_data.csv', skipfooter=6, skiprows=2)

# %%
# calculate average value of a column using mean() function
avgVal = df['KHARGONE-I(3)'].mean()
print('average value of the column KHARGONE-I(3) is {0:.2f}'.format(avgVal))

# %%
# calculate sum of a column using sum() function
sumVal = df['KHARGONE-I(3)'].sum()
print('sum of values of the column KHARGONE-I(3) is {0:.2f}'.format(sumVal))

# %%
# calculate average using for loop
avgVal = 0
for itr in range(df.shape[0]):
    avgVal = avgVal + df['KHARGONE-I(3)'].iloc[itr]

avgVal = avgVal/df.shape[0]
print('average value of the column KHARGONE-I(3) is {0:.2f}'.format(avgVal))

# %%
# create a new column called 'Total' which is the sum of all columns but exclude 1st 2 columns and last column
sumVals = []
for itr in range(df.shape[0]):
    sum = 0
    for col in df.columns.tolist()[2:-1]:
        sum += df[col].iloc[itr]
    sumVals.append(sum)

df['Total'] = sumVals


# %%
# implementing the above task in one line
df['Total1'] = df[df.columns.tolist()[2:-2]].sum(axis=1)

# %%
