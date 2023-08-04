import random
class board:
    def __init__(self, app):
        self.size = app.size
        self.grid = [[None] * app.size for j in range(app.size)]

    def randomizeBoard(self, app):
        for _ in range(len(app.pieces)):
            row = random.randrange(0, app.size)
            col = random.randrange(0, app.size)
            while self.grid[row][col] == True:
                row = random.randrange(0, app.size)
                col = random.randrange(0, app.size)
            self.grid[row][col] = True
        print(self.grid)