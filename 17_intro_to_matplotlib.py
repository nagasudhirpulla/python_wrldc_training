'''
intro to matplotlib library in python for plotting
pip install matplotlib
'''
# %%
import matplotlib.pyplot as plt

# %%
# create x and y arrays for plotting
x = [1,2,3,4]
y = [10,20,58,64]

# create a figure and axis handle using 'plt.subplots' function
fig, ax = plt.subplots()

# plot x and y values using 'plot' function on the axis handle and get a plot artist in return 
la1, = ax.plot(x, y)
la2, = ax.plot(x, [14,54,78,36])

# set title for the plot
ax.set_title('Basic matplotlib plot')

# set label to x and y axes
ax.set_xlabel('X axis label')
ax.set_ylabel('Y axis label')

# set label to plot artist for legend purpose
la1.set_label('awesome_data')
la2.set_label('normal_data')

# enable legends
# control location of legend using the 'loc' input
ax.legend(loc='best')

# show the plot
plt.show()

# %%
# save the figure as png
fig.savefig('dumps/out.png')

# save the figure as pdf
fig.savefig('dumps/out.pdf')

# %%
