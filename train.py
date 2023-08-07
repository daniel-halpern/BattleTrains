class Train():
    def __init__(self, app, row, col):
        self.carList = [(row, col)]

    def addTrain(self, row, col):
        self.carList.append((row, col))

    def removeTrain(self, row, col):
        self.carList.remove((row, col))

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
        

