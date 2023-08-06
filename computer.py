from player import *
from board import *

class Computer(Player):
    def __init__(self, app):
        super().__init__(app)
        self.pieceBoard.grid = randomizeBoard(app)

    # Random guess
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

    # Gets how many pieces the computer has hit / the player has left
    def getPiecesLeft(self, app):
            count = 0
            for row in range(app.size):
                for col in range(app.size):
                    if (self.guessBoard.grid[row][col] and 
                        app.player.pieceBoard.grid[row][col]):
                        count += 1
            return count
        

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

# Recursive function to get a number of trains with corresponding car lengths
def getTrainLengths(pieces, trainLenList):
    newTrain = random.randrange(2, pieces)
    trainLenList.append(newTrain)
    if pieces == sum(trainLenList):
        return trainLenList
    if pieces - sum(trainLenList) < 2:
        return getTrainLengths(pieces, trainLenList[0:-1])
    else: 
        return getTrainLengths(pieces, trainLenList)
