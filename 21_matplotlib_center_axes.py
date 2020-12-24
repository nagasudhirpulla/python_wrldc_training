'''
centering of matplotlib axes so that 0,0 point is in the middle of the figure
'''
# %%
import matplotlib.pyplot as plt
x = []
y = []

# create a plotting area and get the figure, axes handle in return
fig, ax = plt.subplots()

# plot data on the axes handle
ax.plot(x, y)

# Move left y-axis and bottim x-axis to centre by setting position as 'center'
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate top and right axes by setting spline color as 'none'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# print the plot
plt.show()