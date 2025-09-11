# Histogram is used to represent the distribution of numerical data by dividing the entire range of values into a series of intervals (bins) and counting how many values fall into each interval.
# plt.hist(data, bins=number of bins, color='color name', edgecolor='color name', alpha=value, orientation='vertical/horizontal', cumulative=True/False)

import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(1000)  # Generating random data
plt.hist(data, bins=30, color='blue', edgecolor='black', alpha=0.7, orientation='vertical', cumulative=False)
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
# bins is used to set the number of bins in the histogram.
# edgecolor is used to set the color of the edges of the bars in the histogram.
# alpha is used to set the transparency level of the bars in the histogram (0 is fully transparent, 1 is fully opaque).
# orientation is used to set the orientation of the bars in the histogram (vertical or horizontal).
# cumulative is used to set whether to display the cumulative frequency or not (True or False).
# np.random.randn(1000) generates 1000 random numbers from a standard normal distribution (mean=0, std=1).
# You can change the parameters to see how they affect the histogram.
# taller bars indicate a higher frequency of data points within that range, while shorter bars indicate a lower frequency.