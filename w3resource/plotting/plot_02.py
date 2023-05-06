
from matplotlib import pyplot as plt
import numpy as np



x_list = [25,26,27,28,29,30,31,32,33,34,35]
y_list = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
py_list = [45372,48876,53850,57287,63016,65998,70003,70000,71469,75370,83640]
js_list = [37810,43515,46823,49293,53437,56373,62375,66674,68745,68746,74583]

x_indexes = np.arange(len(x_list)) # the index + the width and width=width  is the key
x_indexes
width = 0.25

# when using styles (plt.style.use('')), remove plt.grid(True), it is inbuilt
plt.style.use('fivethirtyeight')
# the index + the width and width=width  is the key
plt.bar(x_indexes-width, y_list, width=width,color ='#444444', label='All Devs',) 
plt.bar(x_indexes,py_list, width=width, color = '#008fd5', label='Python Devs') 
plt.bar(x_indexes+width,js_list, width=width, color = '#e5ae38', label='JavaScript Devs')

plt.xlabel('Age')
plt.ylabel('Median Salary')
plt.title('Median Salary (USD) by age')

plt.legend()

plt.xticks(ticks=x_indexes,labels=x_list)#? read up about ticks
plt.tight_layout()

plt.savefig('barplot.png')

plt.show()
