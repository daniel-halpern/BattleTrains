from board import *
from train import *

class Player:
    def __init__(self, app):
        self.pieces = app.pieces
        self.piecesPlaced = 0
        self.guessBoard = board(app)
        self.pieceBoard = board(app)
        self.trainList = []
    
    # Determines what happens if the top grid is pressed, no matter screen
    def topBoardPressed(self, app, x, y, atTop):
        if app.screen == 'game':
            row, col = getCell(app, x, y, atTop)
            if app.player.guessBoard.grid[row][col] != None:
                print("already guessed there")
            elif app.computer.pieceBoard.grid[row][col]:
                print("HIT")
                app.piecesLeft -= 1
                self.guessBoard.grid[row][col] = True
                app.computer.computerMakeMove(app)
            else:
                print("MISS")
                app.computer.computerMakeMove(app)
                self.guessBoard.grid[row][col] = False

    # Determines what happens if the bottom grid is pressed, no matter screen
    def bottomBoardPressed(self, app, x, y, atTop):
        if app.screen == 'boardCreation':
            row, col = getCell(app, x, y, atTop)
            # If there is already a train car in this position
            if self.pieceBoard.grid[row][col]:
                if getSourroundingCarCount(self.pieceBoard.grid, row, col) < 2:
                    for train in self.trainList:
                        for car in train.carList:
                            if car == (row, col):
                                train.removeTrain((row, col))
            elif getSourroundingCarCount(self.pieceBoard.grid, row, col) == 1:
                for train in self.trainList:
                    for car in train.carList:
                        if 0 <= row - 1 < app.size and car == (row - 1, col):
                            train.addTrain(row, col)
                        elif 0 <= col - 1 < app.size and car == (row, col - 1):
                            train.addTrain(row, col)
                        elif 0 <= row + 1 < app.size and car == (row + 1, col):
                            train.addTrain(row, col)
                        elif 0 <= col + 1 < app.size and car == (row, col + 1):
                            train.addTrain(row, col)
            elif getSourroundingCarCount(self.pieceBoard.grid, row, col) > 1:
                print("Too many surrounding cars")
                # Add an alert here saying how this violates the rules
            elif getSourroundingCarCount(self.pieceBoard.grid, row, col) == 0:
                self.trainList.append(Train(app, row, col))
            # Makes sure the player does not place too many pieces
            if getSourroundingCarCount(self.pieceBoard.grid, row, col) <= 1:
                if self.piecesPlaced == app.pieces:
                    if self.pieceBoard.grid[row][col]:
                        self.pieceBoard.grid[row][col] = (not 
                                                self.pieceBoard.grid[row][col])
                else:
                    self.pieceBoard.grid[row][col] = (not 
                                                self.pieceBoard.grid[row][col])
            self.piecesPlaced = self.updatePiecesPlacedCount(app)
            self.removeEmptyTrains()

    # Removes any empty trains in trainList
    def removeEmptyTrains(self):
        # Loop over each train in the trainList
        i = 0
        while i < len(self.trainList):
            train = self.trainList[i]
            # If the train has an empty carList, remove it from the trainList
            if len(train.carList) == 0:
                self.trainList.pop(i)
            else:
                i += 1
    
    # Updates how the count of how many pieces were placed
    def updatePiecesPlacedCount(self, app):
        count = 0
        for row in range(app.size):
            for col in range(app.size):
                if self.pieceBoard.grid[row][col]:
                    count += 1
        return count
    
# Gets the count for how many surrounding cars
def getSourroundingCarCount(grid, row, col):
    count = 0
    if 0 <= row - 1 < len(grid) and grid[row - 1][col]:
        count += 1
    if 0 <= col - 1 < len(grid) and grid[row][col - 1]:
        count += 1
    if 0 <= row + 1 < len(grid) and grid[row + 1][col]:
        count += 1
    if 0 <= col + 1 < len(grid) and grid[row][col + 1]:
        count += 1
    return count
            
# Gets the grid row and column given an x and y coord 
def getCell(app, x, y, atTop):
    cellSize = app.boardSize / app.size
    gridTop = (app.boardMargin + app.topTextHeight
               + (not atTop) * app.boardSize + (not atTop) * app.boardMargin)
    gridLeft = app.boardMargin
    row = int((y - gridTop) / cellSize)
    col = int((x - gridLeft) / cellSize)
    return row,col

