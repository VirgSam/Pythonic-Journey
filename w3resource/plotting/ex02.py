"""
Write a Pandas program to create a line plot of the opening, closing stock prices 
of Alphabet Inc. between two specific dates
"""

import pandas as pd

df = pd.read_csv('alphabet_stock_data.csv')
df.head()
df.tail(6)
df.describe()

start_date = pd.to_datetime('2020-04-01')
end_date = pd.to_datetime('2020-08-23')
# create a new date frame and set the date column to datetime format
df2 = pd.to_datetime(df['Date'])
# get data frame with only dates
df1 = df 

