# python code goes here
board = []

for x in range(0, 10):
    board.append(["~"]*10)


for x in board:
    grid = (" ".join(x))
    print(grid)
