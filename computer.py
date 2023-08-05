from player import *
from board import *

class Computer(Player):
    def __init__(self, app):
        super().__init__(app)
        self.pieceBoard.grid = randomizeBoard(app)
        #self.guessBoard.grid = randomizeBoard(app)

# Randomly places the pieces for a user
def randomizeBoard(app):
    grid = [[None] * app.size for j in range(app.size)]
    for _ in range(app.pieces):
        row = random.randrange(0, app.size)
        col = random.randrange(0, app.size)
        while grid[row][col]:
            row = random.randrange(0, app.size)
            col = random.randrange(0, app.size)
        grid[row][col] = True
    return grid
