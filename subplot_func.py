# Subplot is used to create multiple plots in a single figure.
# plt.subplot(nrows, ncols, index) -> nrows is number of rows,
# ncols is number of columns, index is the position of the plot in the grid (starting from 1).
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.log(x + 1)

plt.subplot(2, 2, 1)  # 2 rows, 2 columns, plot 1
plt.plot(x, y1, 'r-', label='Sine Wave') # r- is red line
plt.title('Sine Function')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()

plt.subplot(2, 2, 2)  # 2 rows, 2 columns, plot 2
plt.plot(x, y2, 'b-', label='Cosine Wave')
plt.title('Cosine Function')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()

plt.subplot(2, 2, 3)  # 2 rows, 2 columns, plot 3
plt.plot(x, y3, 'g-', label='Tangent Wave')
plt.title('Tangent Function')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.ylim(-10, 10)  # Limiting y-axis to avoid extreme values
plt.legend()
plt.grid()

plt.subplot(2, 2, 4)  # 2 rows, 2
plt.plot(x, y4, 'm-', label='Logarithmic Function')
plt.title('Logarithmic Function')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.tight_layout()  # Adjusts subplot params so that subplots fit in the figure area.
plt.show()
# plt.subplots(nrows, ncols) -> returns a figure and an array of axes objects.
