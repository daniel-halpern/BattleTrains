class board:
    def __init__(self, app):
        self.size = app.size
        self.grid = [[None] * app.size for j in range(app.size)]