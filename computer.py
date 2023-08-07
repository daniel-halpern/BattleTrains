from player import *
from board import *
from time import *

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
# def randomizeBoard(app):
#     grid = [[None] * app.size for j in range(app.size)]
#     for _ in range(app.pieces):
#         row = random.randrange(0, app.size)
#         col = random.randrange(0, app.size)
#         while grid[row][col]:
#             row = random.randrange(0, app.size)
#             col = random.randrange(0, app.size)
#         grid[row][col] = True
#     return grid

def randomizeBoard(app):
    grid = [[None] * (app.size) for j in range(app.size)] # TEMPORARY
    trainDict = makeRandomTrainObjects(app)
    fillTrainObjects(trainDict)
    grid = turnTrainDictIntoGrid(trainDict, grid)
    return grid

# def randomizeBoard(app):
#     while computerAddPiece(app.computer, app, random.randrange(0, app.size), 
#                                         random.randrange(0, app.size)):
#         pass


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

# Makes a dictionary of train objects with random car lengths
def makeRandomTrainObjects(app):
    trainLengths = getTrainLengths(app.pieces, [])
    trainDict = dict()
    for i in range(len(trainLengths)):
        row = random.randrange(0, app.size-1)
        col = random.randrange(0, app.size-1)
        for train in trainDict:
            car = train.carList[0]
            while abs(car[0] - row) < 2 or abs(car[1] - col) < 2:
                row = random.randrange(0, app.size-1)
                col = random.randrange(0, app.size-1)
        trainDict[Train(app, row, col)] = trainLengths[i]
    return trainDict

def isTrainLegal(trainDict):
    seen = set()
    for train in trainDict:
        for car in train.carList:
            if car in seen:
                return False
            else:
                seen.add(car)
    return True

def fillTrainObjects(trainDict):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    newTrainDict = dict()
    for train in trainDict:
        for _ in range(trainDict[train]):
            for x, y in reversed(train.carList):
                if len(train.carList) == trainDict[train]:
                    continue
                for (dx, dy) in directions:
                    train.addTrain(x + dx, y + dy)
                    if len(train.carList) == trainDict[train]:
                        break
                    if isTrainLegal(trainDict) == False:
                        train.removeTrain(x + dx, y + dy)
                    else:
                        continue

def turnTrainDictIntoGrid(trainDict, grid):
    for train in trainDict:
        for car in train.carList:
            grid[car[0]][car[1]] = True
    return grid

