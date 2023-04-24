# https://www.w3resource.com/python-exercises/python-basic-exercises.php
# 37. Write a Python program to display your details like name, age, address in three different lines.

name = input("Please enter your first and last name: ")
age = int(input("Please enter your age: "))
address = input("Please enter your address: ")

print(f"Name: {name} \nAge: {age} \nAddress: {address}" )

# Alternative approach

# def personal_details():
#     name, age = "Simon", 19
#     address = "Bangalore, Karnataka, India"
#     print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

# personal_details()
