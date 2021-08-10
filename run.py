# python code goes here

"""
Created an empty variable for the board which the water and other 
contents of the game will fix inside.
"""

board = []

"""
Here is a for loop that first goes through the process of producing a row of 10 inside of our
board variable, inside which it will place "~" to represent the waves in the game and 
produce 10 columns.
After which it will goes through another loop to remove the [] present in the board variable from
showing up when the grid is printed.
"""

for x in range(0, 10):
    board.append(["~"]*10)


for x in board:
    grid = (" ".join(x))
    print(grid)
