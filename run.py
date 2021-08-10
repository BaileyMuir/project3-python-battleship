# python code goes here
board = []

for x in range(0, 10):
    board.append(["~"]*10)

print(board)

def board_col(board):
    for x in board:
        print(" ".join(x))
