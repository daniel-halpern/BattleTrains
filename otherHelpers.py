from cmu_graphics import *
from player import *
from button import *
from computer import *
import os, pathlib # For the sound stuff

# CITATION: Shawn's soundtest.py code
def loadSound(relativePath):
    # Convert to absolute path (because pathlib.Path only takes absolute paths)
    absolutePath = os.path.abspath(relativePath)
    # Get local file URL
    url = pathlib.Path(absolutePath).as_uri()
    # Load Sound file from local URL
    return Sound(url)

# Called when the game starts or when the player wants to restart
def restart(app):
    app.trainCars = 10
    app.maxTrains = 5
    app.minTrainLength = 2
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
    app.stepsPerSecond = 120
    app.unPauseTime = 0
    app.sideGapWidth = app.width - 3 * app.boardMargin - app.boardSize
    app.midX = app.width - (app.sideGapWidth / 2) - app.boardMargin
    app.piecesLeft = app.pieces
    app.destroyed = False
    app.playerDestroyed = False
    # CITATION: Whistle from https://www.youtube.com/watch?v=fHpytok7TRA
    app.horn = loadSound('TrainWhistle.mp3')
    # CITATION: Explosion sound from https://www.youtube.com/watch?v=9FMquJzgDGQ
    app.smallExplosion = loadSound('smallExplosion.mp3')
    initializeButtons(app)

# Makes all the button objects
def initializeButtons(app):
    # Start screen buttons
    playButton = Button('Play', app.width / 2,  7 * app.height / 16, 
                        app.width / 2, app.height / 10, 'lime', 'play')
    instructionsButton = Button('The Rules', app.width / 2, 
                                9 * app.height / 16, app.width / 2, 
                                app.height / 10, 'gray', 'rules')
    app.startButtonList = [playButton, instructionsButton]
    # Rules buttons
    app.backButton = Button('Back', app.width / 2, 
                                7 * app.height / 8, app.width / 2, 
                                app.height / 10, 'lime', 'back')
    # Board creation screen buttons
    startButton = Button('Start', app.midX, app.height / 2, 
                         app.sideGapWidth, 60, 'lime', 'start')
    app.boardCreationButtonList = [startButton]
    # Game screen buttons
    app.gameButtonList = []
    # Win / Lose screen buttons
    restartButton = Button('Exit', app.midX, app.height / 2, 
                         app.sideGapWidth, 60, 'lime', 'restart')
    app.winLoseButtonList = [restartButton]

## Mouse press related functions ##
# Checks which grid the player clicked, if any
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

# Called after checking if a grid was clicked, checks if a button was clicked
def checkButtonPressed(app, button, mouseX, mouseY):
    # Checks if the mouse was clicked in the button area
    if (button.x - button.width / 2 <= mouseX <= 
        button.x + button.width / 2) and (button.y - button.height / 2 
        <= mouseY <= button.y + button.height / 2):
        if button.command != 'restart':
            button.doCommand(app)
        else:
            restart(app)

# Checks if either the player or computer has won
def checkForWin(app):
    if app.piecesLeft == 0:
        app.screen = 'win'
        app.showSolution = True
        app.paused = False
        if app.previousBestSteps == None or app.steps < app.previousBestSteps:
            app.previousBestSteps = app.steps
    elif app.computer.getPiecesLeft(app) == app.pieces:
        app.screen = 'lose'
        app.showSolution = True
        app.paused = False





    




