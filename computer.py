from player import *
from board import *
from time import *
import random

class Computer(Player):
    def __init__(self, app):
        super().__init__(app)
        self.pieceBoard.grid, self.pieceBoardColors.grid = randomizeBoard(app)

    # Relatively smart guess
    def guess(self, app):
        row = random.randrange(0, app.size)
        col = random.randrange(0, app.size)
        while self.guessBoard.grid[row][col] != None:
            row = random.randrange(0, app.size)
            col = random.randrange(0, app.size)
        if self.hitsExposed(app) != False:
            row, col = self.hitsExposed(app)
        if app.player.pieceBoard.grid[row][col]:
            self.guessBoard.grid[row][col] = True
        else:
            self.guessBoard.grid[row][col] = False

# Returns if, and if there is, where there is a not guessed piece next to a hit
    def hitsExposed(self, app):
        for row in range(app.size):
            for col in range(app.size):
                if self.guessBoard.grid[row][col]:
                    if (0 <= row - 1 < app.size and 
                        self.guessBoard.grid[row - 1][col] == None):
                        return row - 1, col
                    elif (0 <= col - 1 < app.size and 
                          self.guessBoard.grid[row][col - 1] == None):
                        return row, col - 1
                    elif (0 <= row + 1 < app.size and 
                            self.guessBoard.grid[row + 1][col] == None):
                        return row + 1, col
                    elif (0 <= col + 1 < app.size and
                            self.guessBoard.grid[row][col + 1] == None):
                        return row, col + 1
        return False

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

# Makes a new, randomized board
def randomizeBoard(app):
    grid = [[None] * (app.size) for j in range(app.size)] 
    colorGrid = [[None] * (app.size) for j in range(app.size)] 
    trainDict = makeRandomTrainObjects(app)
    # Prevents the program softlocking if it cannot find a legal solution
    while fillTrainObjects(trainDict, app.size) == False:
        trainDict = makeRandomTrainObjects(app)
    grid, colorGrid = turnTrainDictIntoGrid(trainDict, grid, colorGrid)
    return grid, colorGrid

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
        trainDict[Train(app, row, col, len(trainDict))] = trainLengths[i]
    return trainDict

# Checks if the positions of all the trains are legal
def isTrainLegal(trainDict, size):
    seen = set()
    for train in trainDict:
        for car in train.carList:
            if car in seen:
                return False
            elif car[0] < 0 or car[0] >= size or car[1] < 0 or car[1] >= size:
                return False 
            else:
                # Makes sure two trains aren't touching
                for train2 in trainDict:
                    if train2 != train:
                        for car2 in train2.carList:
                            if (car2 == (car[0] + 1, car[1]) or
                                car2 == (car[0], car[1] + 1) or
                                car2 == (car[0] - 1, car[1]) or
                                car2 == (car[0], car[1] + 1)): 
                                return False
                # If all these cases are passed, add the car
                seen.add(car)
    return True

# Counts how many surrounding cars there are to a point
def getSourroundingFromPoint(car, train):
    count = 0
    for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if (car[0] + dx, car[1] + dy) in train.carList:
            count += 1
    return count

# Given a dictionary of train objects and lengths, adds cars onto each train
# object until each train reaches the desired length specified
def fillTrainObjects(trainDict, size):
    directions = [(0, 1), (1,0), (0, -1), (-1, 0)]
    for train in trainDict:
        initialDx, initialDy = directions[random.randrange(0, 4)]
        iterations = 0
        while len(train.carList) < trainDict[train]:
            if iterations == 10:
                return False
            iterations += 1
            # Weights going in the initial direction more
            # CITATION: https://stackoverflow.com/questions/6824681/
            if random.choice([True, True, True, True, True, False]):
                x, y = train.carList[-1]
                train.addTrain(x + initialDx, y + initialDy)
                if isTrainLegal(trainDict, size) == False:
                    train.removeTrain(x + initialDx, y + initialDy)
                continue
            pos = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
            if len(train.carList) == trainDict[train]:
                break
            for x, y in reversed(train.carList):
                if len(train.carList) == trainDict[train]:
                    break
                if (x + pos[0] < 0 or x + pos[0] >= size or y + pos[1] < 0 
                    or y + pos[1] >= size):
                    continue
                train.addTrain(x + pos[0], y + pos[1])
                if isTrainLegal(trainDict, size) == False:
                    train.removeTrain(x + pos[0], y + pos[1])
                    continue

# Takes the train dict and converts all the coordinate points of train cars
# into actual points on the grid
def turnTrainDictIntoGrid(trainDict, grid, colorGrid):
    trainNum = 0
    for train in trainDict:
        for car in train.carList:
            grid[car[0]][car[1]] = True
            colorGrid[car[0]][car[1]] = trainNum
        trainNum += 1
    return grid, colorGrid

