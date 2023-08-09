from board import *
from train import *

class Player:
    def __init__(self, app):
        self.pieces = app.pieces
        self.piecesPlaced = 0
        self.guessBoard = Board(app)
        self.pieceBoard = Board(app)
        self.pieceBoardColors = Board(app)
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
            # If the box pressed has a train car on it
            if self.pieceBoard.grid[row][col]:
                if getSourroundingCarCount(self.pieceBoard.grid, row, col) < 2:
                    for train in self.trainList:
                        for car in train.carList:
                            if car == (row, col):
                                train.removeTrain(row, col)
            # Else, if there is a single surrounding train car, add to train
            elif (getSourroundingCarCount(self.pieceBoard.grid, row, col) == 1 
                    and self.checkNumTrainCars() < app.pieces):
                trainNum = 0
                for train in self.trainList:
                    firstRow, firstCol = train.carList[0]
                    color = self.pieceBoardColors.grid[firstRow][firstCol]
                    for car in train.carList:
                        if 0 <= row - 1 < app.size and car == (row - 1, col):
                            train.addTrain(row, col)
                            self.pieceBoardColors.grid[car[0]][car[1]] = color
                        elif 0 <= col - 1 < app.size and car == (row, col - 1):
                            train.addTrain(row, col)
                            self.pieceBoardColors.grid[car[0]][car[1]] = color
                        elif 0 <= row + 1 < app.size and car == (row + 1, col):
                            train.addTrain(row, col)
                            self.pieceBoardColors.grid[car[0]][car[1]] = color
                        elif 0 <= col + 1 < app.size and car == (row, col + 1):
                            train.addTrain(row, col)
                            self.pieceBoardColors.grid[car[0]][car[1]] = color
                    trainNum += 1
            elif getSourroundingCarCount(self.pieceBoard.grid, row, col) > 1:
                print("Too many surrounding cars")
                # Add an alert here saying how this violates the rules
            # Else, if there are no surrounding train cars, make a new train
            elif (getSourroundingCarCount(self.pieceBoard.grid, row, col) == 0 
                  and self.piecesPlaced < app.pieces):
                colorSet = set()
                for train in self.trainList:
                    colorSet.add(train.color)
                color = min(set(range(0,10)) - colorSet)
                self.trainList.append(Train(app, row, col, color))
                self.removeEmptyTrains()
                self.pieceBoardColors.grid[row][col] = len(self.trainList)-1
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
    
    # Updates how the count of how many pieces were placed on the grid
    def updatePiecesPlacedCount(self, app):
        count = 0
        for row in range(app.size):
            for col in range(app.size):
                if self.pieceBoard.grid[row][col]:
                    count += 1
        return count
    
    # Checks how many train cars are in the trainList
    def checkNumTrainCars(self):
        count = 0
        for train in self.trainList:
            for car in train.carList:
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

