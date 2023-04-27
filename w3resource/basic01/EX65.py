# 65. Write a Python program to convert seconds to day, hour, minutes and seconds.

try:
    # request for input for seconds
    tSecs= int(input("Please enter the number of Seconds to be converted: "))
    print(tSecs,"seconds")
    # convert seconds into day tsecs/86400 
    tDay= int(tSecs/86400) 
    print(tDay,"days")
    # save whole number in day variable and capture frac_result_day
    frac_result_day = (tSecs/86400) - tDay
    print(frac_result_day,"fraction from day")
    # convert frac_result_day to hours: frac_result_day x 24
    tHrs= frac_result_day * 24
    print(tHrs,"Hours")
    # save whole number in hour variable, and capture frac_result_min
    frac_result_min = (frac_result_day * 24) - int(frac_result_day * 24)
    print(frac_result_min,"Fraction from mins")
    # convert frac_result_min to seconds: frac_result_min x 60
    # save whole number and add to frac_result_sec
    # print out varDay,varHrs. 
except ValueError:
    print("Please use an integer,**syntax-error**") 

# Alternative soln
time = float(input("Input time in secs: "))
day = time // (24*3600)
time = time % (24*3600)
hour = time //3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s -> %d:%d:%d:%d" %(day, hour,minutes,seconds) )