from board import *

class player:
    def __init__(self, app):
        self.pieces = app.pieces
        self.guessBoard = board(app)
        self.guessBoard.grid[0][0] = True
        self.pieceBoard = board(app)
