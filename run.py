# python code goes here
from random import randint

"""
Created an empty variable for the board
which the water and other contents of
the game will fix inside.

The Player board works the same but will 
hold another value of # representing their ship.
"""

board = []
player_board = []

"""
Below is the start game function, which prints out the game's
rules before you start to play in case they have never played
battleship before. To do this, I have used simple print statements.
"""

def start_game():
    print("Welcome to Battleship.")
    print("The rules are as followed.")
    print("1) The aim of the game is to destroy your\n opponets ships.")
    print("2) Each row uses a coordinate system of (0,9)\n there are ten rows.")
    print("3) All imputs must be between(0,7) for both\n row and column starting at (0, 0).")
    print("4) Water is represented by ~, misses are \nrepresented by X, hits are represented by !\nand your ship is represented by #")
    print("5) You have 50 attempts to find the other \nship before the game ends.") 
    print("5) Enjoy yourself.")
    
start_game()

"""
Here is a for loop that first goes through
the process of producing a row of eight inside
of our board variable, inside which it will
place "~" to represent the waves in the game
and produce eight columns.

After which it will go through another
loop to remove the [] present in the
board variable from showing up when
the grid is printed.
"""


for x in range(8):
    board.append(["~"] * 8)


def append_board(board):
    for grid in board:
        print(" ".join(grid))


"""
The functions below selects a random location on the
grid stating at 0 and covering the length of the grid
8 to amend it back to 7 I have the -1.
"""

def random_row_coordinate(board):
    return round(randint(0, len(board)-1))


def random_column_coordinate(board):
    return randint(0, len(board[0])-1)


random_row_coordinate(board)
random_column_coordinate(board)

"""
Below is where the location of the opponent's
ship will be stored for easy readability
further on.
"""

c_ship_row = random_row_coordinate(board)
c_ship_col = random_column_coordinate(board)

"""
Create a grid for the player to store their vessel,
allowing the on and allowing them to play with an
automated opponent.
"""

for i in range(8):
    player_board.append(["~"] * 8)


def append_p_board(player_board):
    for grids in player_board:
        print(" ".join(grids))

"""
Here is the primary function.
The purpose of this is to execute
all the tasks needed to run the game.
"""


def main(board, c_ship_col, c_ship_row, append_board, player_board):

    """
    Stores the number of ships currently
    on both player's boards to check for
    an end game function later.
    """

    p_ship_destroyed = 0
    c_ship_destroyed = 0

    """
    This input allows the player to decide
    their name, allowing more involvement
    and control while only using a simple input.
    """

    player_name = input("what is your name:   \n")
    print(f"Welcome {player_name}.")

    """
    The function bellow allows the player
    to decide the coordinates to place
    their ship on the grid. The if/else
    statement checks it's within the range
    of the board; otherwise, it prompts a
    new input. If not done correctly again,
    they have to start the game over again.
    Otherwise, it places their ship.
    """

    p_ship_row = int(input("pick ship row:  \n"))
    p_ship_col = int(input("pick ship column:  \n"))
    if (p_ship_row < 0 or p_ship_row > 7) or (p_ship_col < 0 or p_ship_row > 7):
        print("That's not on the grid captain.")
        print("must be between (0-7)")
        p_ship_row = int(input("pick ship row between (0-7):  \n"))
        p_ship_col = int(input("pick ship column between (0-7):  \n"))
    else:
        player_board[p_ship_row][p_ship_col] = "#"

    """
    for attempt in range(50):
    allows the functions to each 
    execute a set amount of times,
    in this case, 50 before it stops.
    It's also to make the game harder
    by limiting attempts.
    """

    for attempt in range(50):

        print("attempt", attempt + 1)
        
        """
        Below are two variables, both of which
        allow the user to make their guess
        using input and prints a message of 
        where they have selected on the grid.
        """

        row_guess = int(input("Guess the row:  \n"))
        col_guess = int(input("Guess the column:  \n"))
        print(f"Coordinates are ({row_guess},{col_guess}) Fire at will!")

        """
        Like with the input above, I have
        repurposed the random ship location
        into a way for the opponent to guess
        the location of the player's ship.
        """

        def c_row_coordinate(player_board):
            return round(randint(0, len(board)-1))

        def c_column_coordinate(player_board):
            return randint(0, len(board[0])-1)
        c_row_coordinate(player_board)
        c_column_coordinate(player_board)

        com_guess_row = c_row_coordinate(player_board)
        com_guess_col = c_column_coordinate(player_board)

        """
        The if/else statements below, in short,
        check the location of the coordinates given
        to make sure they fit a set of parameters,
        print the correct corresponding message,
        and update the boards appropriately.
        
        If they hit a ship, the use of -= 1 removes
        1 from the number of ships the player or
        computer has.
        """

        if (row_guess < 0 or row_guess > 7) or (col_guess < 0 or col_guess > 7):
                print("Thats not on the radar captain.")
        elif (board[row_guess][col_guess] == "!"):
            print("Captain that vessle has already been destroyed.")
        elif row_guess == c_ship_row and col_guess == c_ship_col:
            print("Target destroyed.")
            board[row_guess][col_guess] = "!"
            c_ship_destroyed += 1
        else:
            if (row_guess < 0 or row_guess > 7) or (col_guess < 0 or col_guess > 7):
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

        """
        the use of print, as shown before,
        displays a message but the
        append_board(board), for example,
        calls back to the function it's from and
        prints the updated board.
        """

        print("Computers board")
        append_board(board)
        print(f"{player_name} board")
        append_p_board(player_board)

        """
        The if/else statements below take a set
        of parameters and, if reached, print a
        message explaining why the games are over.
        I have incorporated the break function to
        stop the code from running after that
        parameter is reached.
        
        The attempts must equal 49 and not 50
        because the computer starts its count
        from 0.
        """

        if attempt == 49:
            print("Game over, our torpedos have run out.")
            print("To play again, press run program \nbutton above terminal.")
            break
        else:
            print("Loading torpedos.")

        if c_ship_destroyed == 1:
            print("you win all enemy vessles have been destroyed.")
            print("To play again, press run program \nbutton above terminal.")
            break

        if p_ship_destroyed == 1:
            print("Game over, all our vessles have been destroyed.")
            print("To play again, press run program \nbutton above terminal.")
            break

main(board, c_ship_col, c_ship_row, append_board, player_board)
