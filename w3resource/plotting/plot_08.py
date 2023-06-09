from cProfile import label
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data2.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.style.use('seaborn-pastel')

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries > dev_salaries ), 
                 interpolate=True, alpha=0.25, label='Above Avg' ) # what is y2=?, what does interpolate do? 

plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries <= dev_salaries ), 
                 interpolate=True, color='#fc4f30', alpha=0.25, label='Below Avg' ) # what does alpha do to opaqueness? 

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()