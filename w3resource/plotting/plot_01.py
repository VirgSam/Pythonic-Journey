from matplotlib import pyplot as plt

# https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_ 
# Matplotlib Tutorials by Corey Schafer

x_list = [25, 26,27,28,29,30,31,32,33,34,35]
y_list = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
py_list = [45372,48876,53850,57287,63016,65998,70003,70000,71469,75370,83640]
js_list = [37810,43515,46823,49293,53437,56373,62375,66674,68745,68746,74583]

#plt.xkcd()# comic plot style
plt.style.use('ggplot')# when using styles remove plt.grid(True), some styles have this inbuilt
plt.plot(x_list,y_list,'#F94814', marker='x',linestyle='--',linewidth='1',label='All Devs',)
plt.plot(x_list,py_list, color = '#444444', linestyle='-.',linewidth='1', 
        marker='o',label='Python Devs')# cleaner to read
#use a label= so you dont have to populate  plt.legend('######'?) and economical      
plt.plot(x_list,js_list,'#2CEF0D', marker='x',label='JavaScript Devs',linewidth='1')

plt.xlabel('Age')
plt.ylabel('Median Salary')
plt.title('Median Salary (USD) by age')

plt.legend()

#plt.grid(True)

plt.tight_layout()

#plt.savefig('plot.png')

plt.show()
