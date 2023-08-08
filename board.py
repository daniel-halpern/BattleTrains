import random
class Board:
    def __init__(self, app):
        self.size = app.size
        self.grid = [[None] * app.size for j in range(app.size)]
        self.colorGrid = [[None] * app.size for j in range(app.size)]
