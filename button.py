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
            if app.player.piecesPlaced == app.pieces:
                app.screen = 'game'
