# Character Picture Grid
# Say you have a list of lists where each value in the inner lists is a one-character string, like this:

# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]

# Think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters.
# The (0, 0) origin is in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase
# going down.

# Copy the previous grid value, and write code that uses it to print the image.

# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....

# Hint: You will need to use a loop in a loop in order to print grid[0][0], then grid[1][0], then grid[2][0],
# and so on, up to grid[8][0]. This will finish the first row, so then print a newline.
# Then your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on.
# The last thing your program will print is grid[8][5].

# Also, remember to pass the end keyword argument to print() if you don’t want a newline printed automatically
# after each print() call.

import random, time, copy

WIDTH = 5  # width in above grid is 0 - 5
HEIGHT = 8  # height in above grid is 0 - 8

# Create a list of list for cells:
nextCells = []

for x in range(WIDTH):
    column = []  # Create a new column.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append("#")  # Add a living cell
        else:
            column.append(" ")  # Add a dead cell
    nextCells.append(column)  # nextCells is a list of column lists

while True:  # Main program loop
    print("\n\n\n\n\n")  # separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end="")  # Print the # or the space.
        print()  # Print a newline at the end of the row.

    # Calculate the enst step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coodinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count nuber of living neighbours:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == "#":
                numNeighbors += 1  # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == "#":
                numNeighbors += 1  # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == "#":
                numNeighbors += 1  # Top right neighbor is alive.
            if currentCells[leftCoord][y] == "#":
                numNeighbors += 1  # Left neighbor is alive.
            if currentCells[rightCoord][y] == "#":
                numNeighbors += 1  # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == "#":
                numNeighbors += 1  # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == "#":
                numNeighbors += 1  # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == "#":
                numNeighbors += 1  # Bottom-right neighbors is alive.

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = "#"
            elif currentCells[x][y] == " " and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = "#"
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = " "
    time.sleep(1)  # Add a 1-second pause to reduce flickering
