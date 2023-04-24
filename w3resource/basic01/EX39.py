# 39. Write a Python program to compute the future value of a 
# specified principal amount, rate of interest, and a number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79
# The formula for future value with compound interest is FV = P(1 + r/n)^nt.
# FV = the future value;
# P = the principal;
# r = the annual interest rate expressed as a decimal;
# n = the number of times interest is paid each year;
# t = time in years.

# def interestCalc(principal,int_rate,yrs):
#     interest = principal * (int_rate/100) * yrs
#     total_amt = principal + interest
#     print( str(round(total_amt,3)))

    
# interestCalc(10000,3.5,7)
# interestCalc(3000 ,4.99,7)

# Alternative approach
amt = 10000
int = 3.5
years = 7
future_value = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))


# how to control the decimal point in a print output == https://stackoverflow.com/a/20457284/15404996