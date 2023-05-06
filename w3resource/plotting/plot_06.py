from matplotlib import pyplot as plt


plt.style.use('fivethirtyeight')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0.1,0,0]# explodes a segment out of the pie chart

#slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
#labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
#colors =['blue','red','yellow','green']



plt.pie(slices, labels=labels, explode=explode, shadow=True, 
        startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor':'black'})
        # autopct='%1.1f%%' incl the calc percentages on diagram

plt.title('My awesome Pie chart')
plt.tight_layout()
plt.show()