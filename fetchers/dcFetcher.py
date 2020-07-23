import pandas as pd
'''
This function returns a sample dataframe that has dc data
'''
def fetchSampleDcDf():
    df = pd.read_csv('data/dc_data.csv', skipfooter=6, skiprows=2)
    return df
