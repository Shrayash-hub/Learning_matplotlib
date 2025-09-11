# we will use savefig to save the figure
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='Sine Wave')
plt.title('Sine Function')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
# Save the figure
plt.savefig('sine_wave.png')  # Save as PNG file
plt.savefig('sine_wave.pdf')  # Save as PDF file
plt.savefig('sine_wave.jpg', dpi=300)  # Save as JPG file with higher resolution
plt.show()
# dpi is used to set the resolution of the saved figure.
# bbox_inches is used to set the bounding box of the saved figure.
# plt.savefig('sine_wave.png', bbox_inches='tight') -> saves the figure with tight bounding box
# transparent is used to set the background of the saved figure to be transparent.
# plt.savefig('sine_wave.png', transparent=True) -> saves the figure with transparent background
# pad_inches is used to set the padding around the saved figure.
# plt.savefig('sine_wave.png', pad_inches=0.5) -> saves the figure with 0.5 inch padding
