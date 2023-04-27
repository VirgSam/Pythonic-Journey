#62. Write a Python program to convert all units of time into seconds.


try:
    # request for input days
    tDays= int(input("Please enter the number of Days to be converted: "))
    # request for input hours
    tHrs= int(input("Please enter the number of Hours to be converted: "))
    # request for minutes
    tMin= int(input("Please enter the number of Minutes to be converted: "))
    # request for minutes
    tSec= int(input("Please enter the number of seconds to be converted: "))
    # covert days into seconds
    tSecd= 3600 * 24 * tDays
    # covert hours into seconds
    tSech= 3600 * tHrs
    # covert minutes into seconds
    tSecm= 60 * tMin
    # add them all up 
    tSecs = tSec
    tSecT = tSecs + tSecm + tSech + tSecd
    # print out output
    print(f"The conversion for {tDays} Days, {tHrs} Hours, {tMin} minutes and {tSec} seconds is {tSecT} seconds")
except ValueError:
    print("Please use an integer,**syntax-error**")

    # Alternative soln
# days = int(input("Input days: ")) * 3600 * 24
# hours = int(input("Input hours: ")) * 3600
# minutes = int(input("Input minutes: ")) * 60
# seconds = int(input("Input seconds: "))

# time = days + hours + minutes + seconds

# print("The  amounts of seconds", time)

