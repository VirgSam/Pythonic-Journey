#Matplotlib Tutorial (Part 9): Plotting Live Data in Real-Time

from cProfile import label
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = [] #[0, 1, 2, 3, 4, 5]
y_vals = [] #[0, 1, 3, 2, 3, 5]

#plt.plot(x_vals, y_vals)


index = count()

def animate(i):
    # x_vals.append(next(index)) # the append(next(index)) counts upward +1
    # y_vals.append(random.randint(0, 5)) # creates a random integer btw 0-5
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()

    plt.plot(x, y1, label='channel 1')
    plt.plot(x, y2, label='channel 2')

    plt.legend(loc='upper left')

ani = FuncAnimation(plt.gcf(), animate, interval=1000 ) 
# gcf = get current figure, pass in the func we want to run for our animation 'animate'
#  + the interval/ms = how often we want to run the func in milisecs

plt.tight_layout()
plt.show()


