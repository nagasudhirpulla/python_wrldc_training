'''
Lesson 4 - Day 4 - timedeltas in datetime module
'''
# %%
import datetime as dt
# %%
# create a desired time interval
timePeriod = dt.timedelta(
    days=5, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

print(timePeriod)
print(type(timePeriod))


# %%
# get the difference between 2 datetimes
nowTime = dt.datetime.now()
xTime = dt.datetime(2020,5,1,13,24,0)

tPeriod = nowTime - xTime
print(tPeriod)

# %%
# get the components of a time interval
print('days = {0}'.format(tPeriod.days))
print('seconds = {0}'.format(tPeriod.seconds))
print('microseconds = {0}'.format(tPeriod.microseconds))

# %%
# get the total seconds in the time span using total_seconds function
totSecs = tPeriod.total_seconds()
print(totSecs)

# %%
# add 10 hrs to existing time period
tPeriodNew = tPeriod+dt.timedelta(hours=10)
print(tPeriod)
print(tPeriodNew)

# %%
