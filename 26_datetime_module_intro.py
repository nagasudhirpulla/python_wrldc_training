'''
datetime module in python
'''
#%%
import datetime as dt
import pandas as pd

#%%
# get the current time
curTime = dt.datetime.now()
print(curTime)
print(type(curTime))

# %%
# create a desired datetime object like 2020-Jul-07 15:20:00 hrs
desTime = dt.datetime(2020,7,23,15,20,0)
print(desTime)

# %%
# using strftime to print datetime in a desired format like %d-%b-%Y %H:%M:%S
# format strings available at https://raw.githubusercontent.com/nagasudhirpulla/taming_python/master/blog/skills/assets/img/datetime_format_codes.png
timeStr = dt.datetime.strftime(desTime, '%d-%b-%Y %H:%M:%S')
print(timeStr)

timeStr = dt.datetime.strftime(desTime, '%H:%M')
print(timeStr)

timeStr = dt.datetime.strftime(desTime, '%d-%m-%Y')
print(timeStr)

# %%
# using strptime to derive datetime object from string
timeStr = '2020-07-15 23:58:12'
timeObj = dt.datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S')
print(timeObj)
print(type(timeObj))

# %%
# convert string type pandas column to datetime column
dataDf = pd.DataFrame(columns=['Time'])
dataDf["Time"]= pd.to_datetime(dataDf["Time"], format='%Y-%m-%d %H:%M:%S') 

# %%
print('original object = {0}'.format(desTime))
print('day = {0}'.format(desTime.day))
print('month = {0}'.format(desTime.month))
print('year = {0}'.format(desTime.year))
print('hours = {0}'.format(desTime.hour))
print('minutes = {0}'.format(desTime.minute))
print('seconds = {0}'.format(desTime.second))
print('microseconds = {0}'.format(desTime.microsecond))
print('UNIX timestamp = {0}'.format(desTime.timestamp()))