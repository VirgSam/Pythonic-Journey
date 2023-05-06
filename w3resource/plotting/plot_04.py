import collections
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

df = pd.read_csv('data.csv')
#df.head()
#df.describe

ids = df['Responder_id']
lang_responses = df['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()  
popularity.reverse() 

plt.barh(languages, popularity, color = '#444444')


plt.xlabel('Number of Users')
plt.title('Most popular Languages')
plt.tight_layout()
plt.show()