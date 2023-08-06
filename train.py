class Train():
    def __init__(self, app, row, col):
        self.carList = [(row, col)]

    def addTrain(self, row, col):
        self.carList.append((row, col))

    def removeTrain(self, pos):
        self.carList.remove(pos)

