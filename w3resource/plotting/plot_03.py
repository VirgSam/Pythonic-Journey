import csv
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

with open ('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # to read a single row
    # row = next(csv_reader)
    # print(row['LanguagesWorkedWith'].split(';'))
    # c = counter(['Python','JavaScript','Java','HTML/CSS'])

    language_counter = Counter()

    # to read every row and save it in a dictionary
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))
#print(language_counter.most_common(15))
languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()  
popularity.reverse() 

plt.barh(languages, popularity, color = '#e5ae38')


plt.xlabel('Number of Users')
#plt.ylabel('Programming Languages')
plt.title('Most popular Languages')
plt.tight_layout()
plt.show()