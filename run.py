# python code goes here
from random import randint
"""
Created an empty variable for the board
which the water and other contents of
the game will fix inside.
"""

board = []

"""
Here is a for loop that first goes through
the process of producing a row of 10 inside
 of our board variable, inside which it will
place "~" to represent the waves in the game
and produce 10 columns.

After which it will goes through another
loop to remove the [] present in the
board variable fromshowing up when
the grid is printed.
"""

for x in range(0, 10):
    board.append(["~"] * 10)


for x in board:
    grid = (" ".join(x))
    print(grid)


"""
the functions below should place a
random ship for the purpose of tesing
the input method when it is added.
"""


def random_row_coordinate(board):
    return round(randint(0, len(board) -1))


def random_column_coordinate(board):
    return randint(0, len(board[0]) -1)


random_row_coordinate(board)
random_column_coordinate(board)

"""
Below are two variable both of which
allow the user to make there guess 
using input to avoid errors i will add
custom error messages in future.
"""
row_guess = input("Guess the row:  \n")
column_guess = input("Guess the column:  \n")

"""
Below is a variable holding the.
random_row_coordinate data to display
the location of the ship when printed.

The same for the print 
random_column_coordinate(board)
as it will also show the location.
"""
random_ship = random_row_coordinate(board)

print(random_ship)
print(random_column_coordinate(board))