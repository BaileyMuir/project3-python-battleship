# python code goes here
from random import randint
"""
Created an empty variable for the board
which the water and other contents of
the game will fix inside.
"""

board = []
player_board = []

def start_game():
    print("Welcome to Battleship")
    print("the rules are as followed")
    print("1) the aim of the game is to destroy your\n opponets ships")
    print("2) each row uses a coordinate system of (0,9)\n there are ten rows")
    print("3) all imputs must be between(0,9) for both\n row and column")
    print("4) water is represented by ~, misses are \nrepresented by X, hits are represented by !\nand your ship is represented by #")
    print("5) enjoy yourself")
    
start_game()

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

for x in range(10):
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
Create grid for player
"""

for i in range(10):
    player_board.append(["~"] * 10)


def append_p_board(player_board):
    for grids in player_board:
        print(" ".join(grids))


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


def main(board, c_ship_col, c_ship_row, append_board, player_board):

    p_ship_destroyed = 0
    c_ship_destroyed = 0

    player_name = input("what is your name:")

    p_ship_row = int(input("pick ship row:  \n"))
    p_ship_col = int(input("pick ship column:  \n"))
    if (p_ship_row < 0 or p_ship_row > 9) or (p_ship_col < 0 or p_ship_row > 9):
        print("That's not on the grid captain.")
        print("must be between (0-9)")
        p_ship_row = int(input("pick ship row between (0-9):  \n"))
        p_ship_col = int(input("pick ship column between (0-9):  \n"))
    else:
        player_board[p_ship_row][p_ship_col] = "#"

    for attempt in range(10):

        print("attempt", attempt + 1)
        """
        Below are two variable both of which
        allow the user to make there guess
        using input to avoid errors i will add
        custom error messages in future.
        """
        
        print(f"{c_ship_row},{c_ship_col}")

        print(f"{p_ship_row},{p_ship_col}")
        
        # print("Computers board")
        # append_board(board)
        # print("Players board")
        # append_p_board(player_board)
        row_guess = int(input("Guess the row:  \n"))
        col_guess = int(input("Guess the column:  \n"))
        print(f"Coordinates are ({row_guess},{col_guess}) Fire at will!")

        def c_row_coordinate(player_board):
            return round(randint(0, len(board)-1))

        def c_column_coordinate(player_board):
            return randint(0, len(board[0])-1)
        c_row_coordinate(player_board)
        c_column_coordinate(player_board)

        com_guess_row = c_row_coordinate(player_board)
        com_guess_col = c_column_coordinate(player_board)

        if (row_guess < 0 or row_guess > 9) or (col_guess < 0 or col_guess > 9):
                print("Thats not on the radar captain.")
        elif (board[row_guess][col_guess] == "!"):
            print("Captain that vessle has already been destroyed.")
        elif row_guess == c_ship_row and col_guess == c_ship_col:
            print("Target destroyed.")
            board[row_guess][col_guess] = "!"
            c_ship_destroyed += 1
        else:
            if (row_guess < 0 or row_guess > 9) or (col_guess < 0 or col_guess > 9):
                print("That's not on the grid captain.")
            elif(board[row_guess][col_guess] == "X"):
                print("Captain that sector has already been targeted.")
            else:
                print ("sector was empty.")
                board[row_guess][col_guess] = "X"

        if com_guess_row == p_ship_row and com_guess_col == p_ship_col:
            player_board[com_guess_row][com_guess_col] = "!"
            print("Computer destroyed one of your vessles Captain.")
            p_ship_destroyed += 1
        else:
            player_board[com_guess_row][com_guess_col] = "X"
            print("Enemy has missed our vessles Captain.")

        print("Computers board")
        append_board(board)
        print(f"{player_name} board")
        append_p_board(player_board)

        if attempt == 10:
            print("Game over, our torpedos have run out.")
            break
        else:
            print("Loading torpedos.")

        if c_ship_destroyed == 1:
            print("you win all enemy vessles have been destroyed")
            break

        if p_ship_destroyed == 1:
            print("Game over, all our vessles have been destroyed")
            break


main(board, c_ship_col, c_ship_row, append_board, player_board)
