from player import *
from board import *

class Computer(Player):
    def __init__(self, app):
        super().__init__(app)
        self.pieceBoard.grid = randomizeBoard(app)

    def guess(self, app):
        row = random.randrange(0, app.size)
        col = random.randrange(0, app.size)
        while self.guessBoard.grid[row][col] != None:
            row = random.randrange(0, app.size)
            col = random.randrange(0, app.size)
        if app.player.pieceBoard.grid[row][col]:
            self.guessBoard.grid[row][col] = True
        else:
            self.guessBoard.grid[row][col] = False

    def computerMakeMove(self, app):
        # Adds a delay between player's guess and computer's guess
        app.unPauseTime = app.steps + random.randrange(25, 50)
        app.paused = True
        app.yourTurn = False
        

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
