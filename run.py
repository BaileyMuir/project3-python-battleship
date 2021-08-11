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

"""
the functions below should place a
random ship for the purpose of tesing
the input method when it is added.
"""


def random_row_coordinate(grid):
    return round(randint(0, len(grid)-1))


def random_column_coordinate(grid):
    return randint(0, len(grid)-1)


random_row_coordinate(grid)
random_column_coordinate(grid)

"""
Below is a variable holding the.
random_row_coordinate data to display
the location of the ship when printed.

The same for the print
random_column_coordinate(board)
as it will also show the location.
"""
c_ship_row = random_row_coordinate(grid)
c_ship_column = random_column_coordinate(grid)

"""
This for loop goes through a range of 100
hundred as there are 100 potential places
for the ship to appear in, As a result
i've set an attemp counter in future
this will also check if a guess has
already been made and when they have
all been made or the player has been
beaten end the game.

For testing its been reduced to ten for now.
"""

for attempt in range(10):
    print(board(grid))
    print("attempt", attempt + 1)

    """
    Below are two variable both of which
    allow the user to make there guess
    using input to avoid errors i will add
    custom error messages in future.
    """

    row_guess = input("Guess the row:  \n")
    column_guess = input("Guess the column:  \n")

    if row_guess == c_ship_row and column_guess == c_ship_column:
        print("You sunk my BattleShip.\n")
    else:
        print("You, missed batter luch next time.\n")
