# as opposed to looping over a list using the range and lens technique range(len(NameOfList))
supplies = ["pens", "staplers", "flamethrowers", "binders"]
for index, item in enumerate(supplies):
    print("index " + str(index) + " in supplies is: " + item)
