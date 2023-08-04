from board import *

class Player:
    def __init__(self, app):
        self.pieces = app.pieces
        self.piecesPlaced = 0
        self.guessBoard = board(app)
        self.pieceBoard = board(app)
    
    def topBoardPressed(self, app, x, y, atTop):
        pass
    def bottomBoardPressed(self, app, x, y, atTop):
        if app.screen == 'boardCreation':
            row, col = getCell(app, x, y, atTop)
            self.pieceBoard.grid[row][col] = not self.pieceBoard.grid[row][col]
            self.piecesPlaced = self.updatePiecesPlacedCount(app)
    
    def updatePiecesPlacedCount(self, app):
        count = 0
        for row in range(app.size):
            for col in range(app.size):
                if self.pieceBoard.grid[row][col] == True:
                    count += 1
        return count
            

def getCell(app, x, y, atTop):
    cellSize = app.boardSize / app.size
    gridTop = (app.boardMargin + app.topTextHeight
               + (not atTop) * app.boardSize + (not atTop) * app.boardMargin)
    gridLeft = app.boardMargin
    row = int((y - gridTop) / cellSize)
    col = int((x - gridLeft) / cellSize)
    return row,col

