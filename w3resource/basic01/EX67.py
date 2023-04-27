# 67. Write a Python program to convert pressure in kilopascals to pounds per square inch,
#  a millimeter of mercury (mmHg) and atmosphere pressure.
# psi for an approximate result, divide the pressure value by 6,895
# atm for an approximate result, divide the pressure value by 101,3
# mmHg for an approximate result, multiply the pressure value by 7,501

user_input=int(input("Please enter pressure value in kilopascals: "))
psi = user_input / 6.895
atm = user_input / 101.3
mmHg = user_input * 7.501 

print(f" {user_input} KPa Kilopascals of pressure when converted to Millimeters of mercury is: {mmHg}  mmHg")
print(f" {user_input} KPa Kilopascals of pressure when converted to Atmosphere pressure is: {atm} atm")
print(f" {user_input} KPa Kilopascals of pressure when converted to Pounds per square inch is: {psi} psi")
