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


def append_board(board):
    for grid in board:
        print(" ".join(grid))

"""
the functions below should place a
random ship for the purpose of tesing
the input method when it is added.
"""


def random_row_coordinate(board):
    return round(randint(0, len(board)-1))


def random_column_coordinate(board):
    return randint(0, len(board[0])-1)


random_row_coordinate(board)
random_column_coordinate(board)

"""
Below is a variable holding the.
random_row_coordinate data to display
the location of the ship when printed.

The same for the print
random_column_coordinate(board)
as it will also show the location.
"""
c_ship_row = random_row_coordinate(board)
c_ship_col = random_column_coordinate(board)

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

def main(board,c_ship_col,c_ship_row,append_board):
    for attempt in range(10):
        print("attempt", attempt + 1)

        """
        Below are two variable both of which
        allow the user to make there guess
        using input to avoid errors i will add
        custom error messages in future.
        """
        print(c_ship_row)
        print(c_ship_col)
        row_guess = int(input("Guess the row:  \n"))
        col_guess = int(input("Guess the column:  \n"))
        print(f"Coordinates are ({row_guess},{col_guess}) Fire at will!")

        if (board[row_guess][col_guess] == "!"):
            print("Captain that ship has vessle has already been destroyed.")
        elif row_guess == c_ship_row and col_guess == c_ship_col:
            print("Target destroyed.")
            board[row_guess][col_guess] = "!"
        else:
            if (row_guess < 0 or row_guess > 9) or (col_guess < 0 or col_guess > 9):
                print("Thats not on the grid captain.")
            elif(board[row_guess][col_guess] == "X"):
                print("Captain that sector has already been targeted.")
            else:
                print ("sector was empty.")
                board[row_guess][col_guess] = "X"

print("Computers board")
append_board(board)

main(board,c_ship_col,c_ship_row,append_board)