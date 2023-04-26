# 59. Write a Python program to convert height (in feet and inches) to centimeters.
# formula 0.0328084 foot == 1 cm
# formula 12 inch == 1 foot
# formula 0.393701 inch == 1 cm
# convert the height to units of foot/inches to only inches and convert to cm

def heightCalc(height):
    # accepts a float variable converts to cm divide feet / 30.48
    cm = height*30.48
    print(f"The result of conversion of {height} feet is: {cm} centimeters")

heightCalc(5.11)

# Alternative soln
print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)

# Alternative soln 2
def height():
  h = input("enter f for height in feets or i for height in inches: ")
  if h == 'f':
    valueF = float(input('enter height in feet: '))
    heightCms = valueF * 30.48
    return heightCms
  elif h == 'i':
    valueI = float(input('enter height in inches: '))
    heightCMs = valueI * 2.54
    return heightCMs

print(height())