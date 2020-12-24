'''
Reshape a dataframe using pivot function
https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html
https://stackoverflow.com/a/24291232/2746323
'''
# %%
import pandas as pd
import datetime as dt

# %%
# read dataframe from csv
dbDcdf = pd.read_csv('assets/data/dc_db_fmt.csv')

# %%
dcDf = dbDcdf.pivot(index="Time Block", columns="util_name", values="dc_val")

# %%
dbSchdf = pd.read_excel('assets/data/sch_db_data.xlsx')


# %%
schDf = dbSchdf.pivot(index=["sch_date", "sch_blk"], columns=[
                      "util_name", "sch_type"], values="sch_val")

# %%
schDf.columns = ['{0}|{1}'.format(a, b) for a, b in schDf.columns]
schDf.index = [x[0] + dt.timedelta(minutes=15*int(x[1]-1))
               for x in schDf.index]
