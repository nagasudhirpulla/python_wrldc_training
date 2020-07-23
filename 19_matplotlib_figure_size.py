'''
Lesson 8 - Day 3 - sizing of matplotlib plots
'''
#%%
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 2, 3]

# create a new figure and get figure, axes handle in return
# here we are setting width = 3 inches, height = 2 inches
fig, ax = plt.subplots(figsize=(3,2))

# using color keyword itn plot function to control color
ax.plot(x,y)

# print figure
plt.show()

# %%
