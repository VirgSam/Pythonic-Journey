from matplotlib import pyplot as plt


plt.style.use('fivethirtyeight')

slices = [60,40,30,20]
labels = ['Sixty','Forty', 'extra1','extra2' ]
#colors =['blue','red','yellow','green']
colors =['#008fd5','#fc4f30','#e5ae37','#6d904f']


plt.pie(slices,labels=labels,colors=colors,wedgeprops={'edgecolor':'black'})

plt.title('My awesome Pie chart')
plt.tight_layout()
plt.show()

#Colors:
#Blue = #008fd5
#Red = #fc4f30
#Yellow = #e5ae37
#Green = #6d904f

# matplotlib styles
# ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 
# 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 
# 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 
# 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 
# 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 
# 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 
# 'tableau-colorblind10']