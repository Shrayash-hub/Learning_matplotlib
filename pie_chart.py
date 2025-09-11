# pie chart is used to show proportions of a whole.
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, explode=explode, shadow=True)

# autopct is used to display the percentage value on each slice of the pie chart.
# startangle is used to rotate the start of the pie chart by given angle.
# explode is used to "explode" or offset a slice from the pie for emphasis.
# shadow is used to add a shadow effect to the pie chart.

import matplotlib.pyplot as plt
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode the 1st slice
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, explode=explode, shadow=True)
plt.title('Pie Chart Example')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Donut chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, explode=explode, shadow=True, wedgeprops={'width':0.3})
plt.title('Donut Chart Example')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# %1.1f%% in autopct means 1 digit before decimal, 1 digit after decimal and %% is used to display the percentage sign.