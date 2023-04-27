# 66. Write a Python program to calculate body mass index.
# BMI = weight/height^2 in kg/m^2

weight= float(input("Please enter body weight in kilograms: "))
height= float(input("Please enter height in meters: "))
bmi = weight/height**2
print(f"For a height of: {height} and a weight of: {weight}, the BMI is: {bmi}")


def bmi_calc(weight,height):
    """
    calculates BMI
    """
    bmi = weight/height**2
    print(f"For a height of: {height} and a weight of: {weight}, the BMI is: {bmi}")

bmi_calc(74.4, 1.8034)

# Alternative solution 1
height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))

# Alternative solution 2
def bmi(weight,height):
    bmi = round(weight/height**2, 1)
    if bmi < 18.5:
        print("Your body mass index is {} which is below normal weight".format(bmi))
    elif bmi >= 18.5 and bmi < 25:
        print("Your body mass index is {} which is normal weight".format(bmi))
    elif bmi >= 30 and bmi <35:
        print("Your body mass index is {} which means you're overweight".format(bmi))
    elif bmi >=35:
        print("Your body mass index is {} which means obesity".format(bmi))

bmi(46, 1.73) #Your body mass index is 15.4 which is below normal weight
