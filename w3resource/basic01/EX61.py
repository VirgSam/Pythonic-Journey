# 61. Write a Python program to convert the distance (in feet) to inches, yards, and miles
# feet = miles * 5,280
# feet = inches / 12 
# feet = yards  * 3

# input variable of feet
feet = int(input("Please enter the distance (in feet) to receive your output"))

# conversion to miles
miles = feet/5280

# conversion to inches
inches = feet * 12

# conversion to yards
yards = feet/3

print(f'{feet} Feet in distance is converted to {round(miles, 6)} miles, {inches} inches and {yards} yards')

#Alternative solution
d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)
