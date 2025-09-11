# Bar charts are used to compare categories or show discrete data visually.

# plt.bar(x, height) -> for vertical bars
# plt.barh(y, width) -> for horizontal bars

import matplotlib.pyplot as plt
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 12]
plt.bar(categories, values, color='orange', label='Category Values')

plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.legend()
plt.show()

# Horizontal bar chart
plt.barh(categories, values, color='green', label='Category Values')
plt.title('Horizontal Bar Chart Example')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.legend()
plt.show()

# Stacked bar chart
import numpy as np
labels = ['G1', 'G2', 'G3']
category1 = [20, 34, 30]
category2 = [25, 32, 34]
x = np.arange(len(labels))
plt.bar(x, category1, label='Category 1', color='b')
plt.bar(x, category2, bottom=category1, label='Category 2', color='r')
plt.xticks(x, labels)
plt.xlabel('Groups')
plt.ylabel('Values')
plt.title('Stacked Bar Chart Example')
plt.legend()
plt.show()
