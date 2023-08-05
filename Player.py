from board import *

class Player:
    def __init__(self, app):
        self.pieces = app.pieces
        self.piecesPlaced = 0
        self.guessBoard = board(app)
        self.pieceBoard = board(app)
    
    def topBoardPressed(self, app, x, y, atTop):
        if app.screen == 'game':
            row, col = getCell(app, x, y, atTop)
            print(row, col)
            if app.computer.pieceBoard.grid[row][col]:
                print("HIT")
                self.guessBoard.grid[row][col] = True
            else:
                print("MISS")
                self.guessBoard.grid[row][col] = False

    def bottomBoardPressed(self, app, x, y, atTop):
        if app.screen == 'boardCreation':
            row, col = getCell(app, x, y, atTop)
            if self.piecesPlaced == app.pieces:
                if self.pieceBoard.grid[row][col]:
                    self.pieceBoard.grid[row][col] = not self.pieceBoard.grid[row][col]
            else:
                self.pieceBoard.grid[row][col] = not self.pieceBoard.grid[row][col]
            self.piecesPlaced = self.updatePiecesPlacedCount(app)
    
    def updatePiecesPlacedCount(self, app):
        count = 0
        for row in range(app.size):
            for col in range(app.size):
                if self.pieceBoard.grid[row][col]:
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

