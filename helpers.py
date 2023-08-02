from cmu_graphics import *
from Player import *

def restart(app):
    app.trainCars = 10
    app.size = 10
    app.pieces = 10
    app.boardMargin = app.width / 16
    app.boardHeight = (app.height // 2) - (app.boardMargin * 3)
    app.boardWidth = app.boardHeight
    app.cols = app.size
    app.rows = app.size
    app.cellBorderWidth = 2
    app.player = player(app)
    app.topTextHeight = 100
    app.screen = 'start'
    # Screen states: start, boardCreation, game, win, lose, instructions
    


### Drawing helper functions ###

## Drawing the start screen ##
def drawStartScreen(app):
    drawLabel('BattleTrains', app.width / 2, app.boardMargin * 3, size = 79)

## Draw the board ##
def drawBoard(app, grid, atTop):
    for row in range(app.size):
        for col in range(app.size):
            drawCell(app, grid, row, col, atTop)
    # Draws the black border around the board to make it even
    if atTop == True:
        drawRect(app.boardMargin, app.boardMargin + app.topTextHeight, 
             app.boardWidth, app.boardHeight,
            fill=None, border='black', borderWidth=app.cellBorderWidth*2)
    else:
        drawRect(app.boardMargin, 2 * app.boardMargin + app.topTextHeight 
                 + app.boardHeight, app.boardWidth, app.boardHeight,
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
    cellSize = app.boardWidth / app.size
    if atTop == True:
        cellTop = app.boardMargin + (row * cellSize)
    else:
        cellTop = 2 * app.boardMargin + (row * cellSize) + app.boardHeight
    # Adds room for the title at the top
    cellTop += app.topTextHeight
    cellLeft = app.boardMargin + (col * cellSize)
    return cellLeft, cellTop, cellSize
