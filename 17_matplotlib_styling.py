'''
Lesson 6 - Day 3 - styling matplotlib plot
'''
#%%
import matplotlib.pyplot as plt
import pandas as pd

# %%
# read dc data from csv and skip first 2 rows and skip last 6 rows
df = pd.read_csv('data/dc_data.csv', skipfooter=6, skiprows=2)

# %%
xData = df['Time Block']
yData = df['VSTPS I(5)']

# %%
# changing color of the line
# create a figure and axis handle using 'plt.subplots' function
fig, ax = plt.subplots()

# plot x and y values using 'plot' function on the axis handle and get a plot artist in return 
la, = ax.plot(xData, yData, color='red')

# show the plot
plt.show()

# %%
# linestyle to linestyle can be 'solid', 'dashed', 'dashdot', 'dotted', 'None'
# changing color of the line
# create a figure and axis handle using 'plt.subplots' function
fig, ax = plt.subplots()

# plot x and y values using 'plot' function on the axis handle and get a plot artist in return 
la, = ax.plot(xData, yData, linestyle='dashdot', color='green')

# show the plot
plt.show()

# %%
# plot markers
''''
marker string can be used to control the marker style
For example 'o' means circle marker, '.' means point marker
all marker style strings can be found at https://matplotlib.org/2.1.1/api/markers_api.html#module-matplotlib.markers

other marker styling options are
--------------------------------
markeredgecolor / mec - control the color of marker edge / outline

markeredgewidth / mew - a number that can control the marker outline/edge width

markerfacecolor / mfc - control the color of marker filling inside the outline

markersize / ms - a number that can control the size of the marker
'''
# create a figure and axis handle using 'plt.subplots' function
fig, ax = plt.subplots()

# plot x and y values using 'plot' function on the axis handle and get a plot artist in return 
la, = ax.plot(xData, yData, linestyle='solid', marker='*', mfc='red', ms=15, mec='green', mew=2)

# show the plot
plt.show()

# %%
