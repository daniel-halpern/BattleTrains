from helpers import *

class player:
    def __init__(self, app):
        self.pieces = app.pieces
        self.guessBoard = board(app)
        self.pieceBoard = board(app)


class board:
    def __init__(self, app):
        self.size = app.size
        self.grid = [[[None] * app.size] for j in range(app.size)]

class computer(player):
    pass

class button:
    pass