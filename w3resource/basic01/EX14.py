# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import datetime

day_1 = datetime.strptime("2014/7/2","%Y/%m/%d")
day_2 = datetime.strptime("2014/7/11","%Y/%m/%d")
output = day_2 - day_1
print (output.days)
