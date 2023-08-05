from cmu_graphics import *
from player import *
from button import *
from computer import *

def restart(app):
    app.trainCars = 10
    app.size = 8
    app.pieces = 10
    app.boardMargin = app.width / 16
    app.boardSize = (app.height // 2) - (app.boardMargin * 3)
    app.cellBorderWidth = 2
    app.player = Player(app)
    app.computer = Computer(app)
    app.topTextHeight = 100
    app.screen = 'start'
    app.yourTurn = True
    app.showSolution = False
    app.paused = False
    app.steps = 0
    app.unPauseTime = 0
    initializeButtons(app)
    
def initializeButtons(app):
    # Start screen buttons
    playButton = Button('Play', app.width / 2, app.height / 4, app.width / 2, 
                        app.height / 10, 'lime', 'play')
    settingsButton = Button('Settings', app.width / 2, 3 * app.height / 8, 
                            app.width / 2, app.height / 10, 'gray', 'settings')
    instructionsButton = Button('Instructions', app.width / 2, app.height / 2, 
                                app.width / 2, app.height / 10, 'gray', 
                                'instructions')
    app.startButtonList = [playButton, settingsButton, instructionsButton]
    # Board creation screen buttons
    startButton = Button('Start', app.height / 2, app.width - app.boardMargin, 
                         100, 50, 'lime', 'start')
    app.boardCreationButtonList = [startButton]
    app.gameButtonList = []

## Mouse press related functions ##
def checkButtonPressed(app, button, mouseX, mouseY):
    # Checks if the mouse was clicked in the button area
    if (button.x - button.width / 2 <= mouseX <= 
        button.x + button.width / 2) and (button.y - button.height / 2 
        <= mouseY <= button.y + button.height / 2):
        button.doCommand(app)

def checkGridPressed(app, mouseX, mouseY):
    # Checks if the mouse was clicked in the top grid area
    if (app.boardMargin <= mouseX <= app.boardMargin + app.boardSize) and (
        app.boardMargin + app.topTextHeight <= mouseY <= 
        app.boardMargin + app.topTextHeight + app.boardSize):
        return True, True
    # Checks if the mouse was clicked in the bottom grid areaxss
    elif (app.boardMargin <= mouseX <= app.boardMargin + app.boardSize) and (
        2 * app.boardMargin + app.topTextHeight + app.boardSize <= mouseY <= 
        2 * app.boardMargin + app.topTextHeight + app.boardSize * 2):
        return True, False
    else:
        return False, 