import numpy as np

WIDTH = 6  # width in above grid is 0 - 5
HEIGHT = 9  # height in above grid is 0 - 8

# Create a list of list for cells:
nextCells = []
for x in range(WIDTH):
    column = []  # Create a new column.
    for y in range(HEIGHT):
        if True:
            column.append(".")  # Add a living cell
        else:
            column.append("o")  # Add a dead cell
    nextCells.append(column)  # nextCells is a list of column lists

testCell = np.array(nextCells)
print(testCell)
testCell[0][1]
