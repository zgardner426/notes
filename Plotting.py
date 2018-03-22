# Plotting
# matplotlib is the plotting library for python


import matplotlib.pyplot as plt

plt.figure(1)

plt.plot([1, 2, 3, 4, 10])  # when no x is specified, just assigns according to index

plt.plot([10, 4, 3, 2, 1])  # plots to the same graph


plt.figure(2)  # opens new window
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])  # can spescify x and y "lists"

# customize your graph/plot using kwargs
plt.plot([1, 2, 3, 4], [1, 2, 3, 4], c='green', linestyle='--', marker='+', markersize=10, alpha=.5)
'''
c or color = color as a string
linestyle or ls = "-" solid line, "--" dashed, "-." dot dash, ":" dotted
marker = '.', '+', '^', 'o'
markersize = float (pixels)
alpha = transparency from 0 to 1
'''

plt.axis([0, 10, 0, 10])  # x-min, x-max, y-min, y-max
plt.ylabel('my data (units)')
plt.xlabel('My scale (units)')

# plt.figure(3)

plt.show()

