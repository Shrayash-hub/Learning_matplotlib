# Building a bakery sales plot using matplotlib
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sales = [150, 200, 250, 300, 400, 500, 600]

plt.plot(days, sales)
plt.title('Bakery Sales Over a Week')
plt.xlabel('Days of the Week')  
plt.ylabel('Number of Sales')
plt.show()

