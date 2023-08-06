from cmu_graphics import *
class Button:
    def __init__(self, text, x, y, width, height, color, command):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.command = command

    def drawButton(self, app):
        drawRect(self.x, self.y, self.width, self.height, 
                 fill=self.color, border='black', align = 'center')
        drawLabel(self.text, self.x, self.y, size = self.height/2)
        
    def doCommand(self, app):
        if self.command == 'play':
            app.screen = 'boardCreation'
        elif self.command == 'settings':
            app.screen = 'settings'
        elif self.command == 'instructions':
            print("instruct")
            app.screen = 'instructions'
        elif self.command == 'start':
            # Only lets you start game if requirements are fufilled
            if (app.player.piecesPlaced == app.pieces and 
                len(app.player.trainList) <= app.maxTrains):
                for train in app.player.trainList:
                    # Returns if any car is shorter than 2 long
                    if len(train.carList) < 2:
                        return
                app.screen = 'game'
