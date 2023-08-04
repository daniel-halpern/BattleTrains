from cmu_graphics import *
from player import *
from button import *

def restart(app):
    app.trainCars = 10
    app.size = 8
    app.pieces = 10
    app.boardMargin = app.width / 16
    app.boardSize = (app.height // 2) - (app.boardMargin * 3)
    app.cellBorderWidth = 2
    app.player = Player(app)
    app.computer = Player(app)
    app.topTextHeight = 100
    app.screen = 'start'
    # Screen states: start, boardCreation, game, win, lose, instructions
    initializeButtons(app)
    
def initializeButtons(app):
    # Start screen buttons
    playButton = Button('Play', app.width / 2, app.height / 2, 100, 50, 'lime', 
                        'play')
    app.startButtonList = [playButton]
    # Board creation screen buttons
    startButton = Button('Start', app.height / 2, app.width - app.boardMargin, 
                         100, 50, 'lime', 'start')
    app.boardCreationButtonList = [startButton]

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

### Drawing helper functions ###

## Drawing the start screen ##
def drawStartScreen(app):
    drawLabel('BattleTrains', app.width / 2, app.boardMargin * 3, size = 79)
    for button in app.startButtonList:
        Button.drawButton(button, app)

## Draw the board creation screen ##
def drawBoardCreation(app):
    drawLabel('Create your board', app.width / 2, app.boardMargin * 2, 
              size = 50)
    drawBoard(app, app.player.guessBoard.grid, atTop=True)
    drawBoard(app, app.player.pieceBoard.grid, atTop=False)
    for button in app.boardCreationButtonList:
        if button.command == 'start':
            if app.player.piecesPlaced < app.pieces:
                button.color = 'gray'
            else:
                button.color = 'lime'
        Button.drawButton(button, app)

## Draw the board ##
def drawBoard(app, grid, atTop):
    for row in range(app.size):
        for col in range(app.size):
            drawCell(app, grid, row, col, atTop)
    # Draws the black border around the board to make it even
    if atTop == True:
        drawRect(app.boardMargin, app.boardMargin + app.topTextHeight, 
             app.boardSize, app.boardSize,
            fill=None, border='black', borderWidth=app.cellBorderWidth*2)
    else:
        drawRect(app.boardMargin, 2 * app.boardMargin + app.topTextHeight 
                 + app.boardSize, app.boardSize, app.boardSize,
                fill=None, border='black', borderWidth=app.cellBorderWidth*2)


# Draws each indiviual cell
def drawCell(app, grid, row, col, atTop):
    cellLeft, cellTop, cellSize = getCellLeftTop(app, row, col, atTop)
    if grid[row][col] == True:
        color = 'red'
    else:
        color = None
    drawRect(cellLeft, cellTop, cellSize, cellSize,
             fill=color, border='black',
             borderWidth=app.cellBorderWidth)

# Gets the x and y position for each cell given a row and column
def getCellLeftTop(app, row, col, atTop):
    cellSize = app.boardSize / app.size
    if atTop == True:
        cellTop = app.boardMargin + (row * cellSize)
    else:
        cellTop = 2 * app.boardMargin + (row * cellSize) + app.boardSize
    # Adds room for the title at the top
    cellTop += app.topTextHeight
    cellLeft = app.boardMargin + (col * cellSize)
    return cellLeft, cellTop, cellSize
