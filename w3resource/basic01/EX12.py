#Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
import calendar
#dd = int(input("Please input the Day: "))
mm = int(input("Please input the Month: "))
yy = int(input("Please input the Year: "))


print(calendar.month(yy,mm))
#print(calendar.isleap(yy))
#print(calendar.leapdays (1976,2022))
#print(calendar.weekday(yy,mm,dd))