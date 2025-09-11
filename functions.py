import matplotlib.pyplot as plt

months = [1,2,3,4]
sales = [250,300,400,450]


# syntex of plot function is plt.plot(x, y, color='',marker='marker symbol', linestyle='', linewidth=value,markersize=value, label='label name')
plt.plot(months, sales, color='blue', marker='o', linestyle='--', linewidth=2, markersize=8, label='Sales Data')

plt.title('Monthly Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales')


# syntex of legend function is plt.legend(loc='location', fontsize=value, title='title name', title_fontsize=value)
plt.legend(loc='upper left', fontsize=10, title='Legend')


# syntex of grid function is plt.grid(color='color name', linestyle='line style', linewidth=value)
plt.grid(color='gray', linestyle=':', linewidth=0.5)


# xlim and ylim is used to set the limit of x and y axis
plt.xlim(0, 5)
plt.ylim(200, 500)

# syntex of xticks and yticks is plt.xticks(ticks=[list of positions], labels=[list of labels]) and plt.yticks(ticks=[list of positions], labels=[list of labels]) , it is used to set the custom ticks and labels on x and y axis
plt.xticks([1, 2, 3, 4], ['Jan', 'Feb', 'Mar', 'Apr'])
plt.yticks([250, 300, 350, 400, 450], ['250k', '300k', '350k', '400k', '450k'])
plt.show()