# Matplotlib Tutorial (Part 8): Plotting Time Series Data

import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

# dates = [
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30)
# ]

# y = [0, 1, 3, 4, 6, 5, 7] # list of 7 random values


# date_format = mpl_dates.DateFormatter('%b,%d %Y') # where does one get the info in the brackets?

# plt.gca().xaxis.set_major_formatter(date_format) # get current axis

data = pd.read_csv('data4.csv')

data['Date']= pd.to_datetime(data['Date'])# pd.to_datetime() is important for time series data
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')# take note of this mtd

plt.gcf().autofmt_xdate()# runs autoformat on the dates

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()

