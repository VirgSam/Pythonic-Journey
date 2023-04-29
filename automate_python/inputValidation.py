while True:
    age = input("Enter your age:")
    try:
        age = int(age)
    except:
        print("Please use numeric digits.")
        continue
    if age < 1:
        print("Plese enter a positive numeber.")
        continue
    break
print(f"Your age is {age}.")
