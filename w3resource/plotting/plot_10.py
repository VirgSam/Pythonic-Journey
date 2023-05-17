#Matplotlib Tutorial (Part 7): Scatter Plots
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

# x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
# y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
# colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
# sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
#          538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]








data = pd.read_csv('2019-05-31-data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter( view_count, likes, c=ratio, cmap='summer', edgecolors='black', linewidths=1, alpha=0.75 ) #marker='X', s=sizes, (c=colors, cmap='Reds': come in pairs) learn other techniques on how to use cmap

cbar = plt.colorbar() # plots horizontal bar in scatterplot
cbar.set_label('Like/Dislike Ration') # these work together as a set

plt.xscale('log')# how to deal with outliers in the data
plt.yscale('log')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()