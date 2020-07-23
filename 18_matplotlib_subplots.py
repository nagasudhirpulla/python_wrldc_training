'''
Lesson 7 - Day 3 - matplotlib multiple plots in a figure using subplots
'''
# %%
import matplotlib.pyplot as plt
import pandas as pd
from fetchers.dcFetcher import fetchSampleDcDf

# %%
# read dc data from csv and skip first 2 rows and skip last 6 rows
df = fetchSampleDcDf()

# %%
# get data series from dataframe
timeBlks = df['Time Block']
v1Dc = df['VSTPS I(5)']
khDc = df['KHARGONE-I(3)']
gRlngDc = df['GANDHAR-RLNG(1)']
gApmDc = df['GANDHAR-APM(1)']

# %%
# create a figure with multiple subplots handle using 'plt.subplots(nrows, ncols)' function
fig, axs = plt.subplots(nrows=2, ncols=1, constrained_layout=True)

# plot x and y values using 'plot' function on the axis handle and get a plot artist in return
la1, = axs[0].plot(timeBlks, v1Dc, color='magenta')
la2, = axs[1].plot(timeBlks, khDc, color='orange')

# set the axis titles
axs[0].set_title('VSTPS I DC')
axs[1].set_title('KHARGONE-I DC')

# set the figure title
fig.suptitle('Mutiple plots example', fontsize=20)

# show the plot
plt.show()

# %%
# create a figure with multiple subplots handle using 'plt.subplots(nrows, ncols)' function
fig, axs = plt.subplots(nrows=2, ncols=2, constrained_layout=True)

# plot x and y values using 'plot' function on the axis handle and get a plot artist in return
la1, = axs[0, 0].plot(timeBlks, v1Dc, color='magenta')
la2, = axs[0, 1].plot(timeBlks, khDc, color='orange')
la3, = axs[1, 0].plot(timeBlks, gRlngDc, color='green')
la4, = axs[1, 1].plot(timeBlks, gApmDc, color='blue')

# set the axis titles
axs[0, 0].set_title('VSTPS I DC')
axs[0, 1].set_title('KHARGONE-I DC')
axs[1, 0].set_title('GANDHAR-RLNG DC')
axs[1, 1].set_title('GANDHAR-APM DC')

# iterate through each axis
for ax in axs.reshape(-1):
    # explicitly specify x ticks positions
    # ax.set_xticks(list(range(1,96,10)))
    # specify the interval of ticks as mutiples of 10
    ax.xaxis.set_major_locator(plt.MultipleLocator(10))
    # explicitly specify x axis limits
    ax.set_xlim(1, 96)

# set the figure title
fig.suptitle('DC Plots example', fontsize=20)

# show the plot
plt.show()

# %%
