# Scatterplots are used to visualize the relationship between two continuous variables.

import matplotlib.pyplot as plt

hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 80, 85, 90]

plt.scatter(hours_studied, scores, color='blue', marker='o', label='Scores vs Hours Studied')
plt.title('Scatterplot Example')
plt.xlabel('Hours Studied')
plt.ylabel('Scores')
plt.legend()
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()
# color is used to set the color of the points in the scatterplot.
# marker is used to set the shape of the points in the scatterplot.
# label is used to set the label for the legend.
# used to find the correlation between two variables.
# in regression analysis, scatterplots help visualize the fit of a regression line to the data points.
# can also be used to identify outliers in the data.


# if we want to compare multiple datagrup in a single scatterplot

import numpy as np
# Generating random data for two groups
group1_x = np.random.rand(50) * 10
group1_y = np.random.rand(50) * 100
group2_x = np.random.rand(50) * 10
group2_y = np.random.rand(50) * 100
plt.scatter(group1_x, group1_y, color='red', marker='o', label='Group 1')
plt.scatter(group2_x, group2_y, color='green', marker='^', label='Group 2')
plt.title('Scatterplot with Multiple Groups')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.legend()
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()