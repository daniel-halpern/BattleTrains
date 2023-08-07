from cmu_graphics import *
from player import *
from button import *
from computer import *

# Drawing the start screen
def drawStartScreen(app):
    drawLabel('BattleTrains', app.width / 2, app.boardMargin * 3, size = 79)
    for button in app.startButtonList:
        Button.drawButton(button, app)

# Draw the game in progress screen
def drawGameScreen(app):
    if app.yourTurn:
        drawLabel('Your turn', app.width / 2, app.boardMargin * 2, size = 70)
    else:
        drawLabel("Computer's turn", app.width / 2, app.boardMargin * 2, 
                  size = 65)
    drawBoard(app, app.computer.pieceBoard.grid, atTop=True)
    drawBoard(app, app.player.pieceBoard.grid, atTop=False)
    drawBoard(app, app.player.guessBoard.grid, atTop=True)
    for button in app.gameButtonList:
        Button.drawButton(button, app)
    # Draw time elapsed sidebar label
    drawLabel('Time elapsed:', app.midX, 2 * app.boardMargin + 
              app.topTextHeight, size = 20)
    if (app.steps // 60) % 60 // 10 == 0:
        drawLabel(f'{app.steps // 60 // 60}:0{app.steps // 60 % 60}', app.midX,
                  2 * app.boardMargin + app.topTextHeight + 50, size = 50)
    else:
        drawLabel(f'{app.steps // 60 // 60}:{app.steps // 60 % 60}', app.midX,
                  2 * app.boardMargin + app.topTextHeight + 50, size = 50)
    # Draw pieces left sidebar label
    drawLabel('Pieces left', app.midX, 6 * app.boardMargin + app.topTextHeight, 
              size = 20)
    drawLabel(app.piecesLeft, app.midX, 6 * app.boardMargin + app.topTextHeight 
              + 50, size = 50)

# Draw the board creation screen
def drawBoardCreation(app):
    drawLabel('Create your board', app.width / 2, app.boardMargin * 2, 
              size = 50)
    drawBoard(app, app.computer.pieceBoard.grid, atTop=True)
    drawBoard(app, app.player.pieceBoard.grid, atTop=False)
    for button in app.boardCreationButtonList:
        if button.command == 'start':
            if (app.player.piecesPlaced < app.pieces or 
                len(app.player.trainList) > app.maxTrains):
                button.color = 'gray'
            else:
                button.color = 'lime'
                for train in app.player.trainList:
                    if len(train.carList) < 2:
                        print("Gray")
                        button.color = 'gray'
        Button.drawButton(button, app)
    # Draw pieces left sidebar label
    drawLabel('Pieces left', app.midX, 6 * app.boardMargin + app.topTextHeight, 
              size = 20)
    drawLabel(app.pieces - app.player.piecesPlaced, app.midX, 6 * 
              app.boardMargin + app.topTextHeight + 50, size = 50)

# Draw the board
def drawBoard(app, grid, atTop):
    # Draws the black border around the board and the gray background
    if atTop == True:
        drawRect(app.boardMargin, app.boardMargin + app.topTextHeight, 
             app.boardSize, app.boardSize,
            fill='black', opacity = 25)
        drawRect(app.boardMargin, app.boardMargin + app.topTextHeight, 
             app.boardSize, app.boardSize,
            fill=None, border='black', borderWidth=app.cellBorderWidth*2)
    else:
        drawRect(app.boardMargin, 2 * app.boardMargin + app.topTextHeight 
                 + app.boardSize, app.boardSize, app.boardSize,
                fill='black', opacity = 25)
        drawRect(app.boardMargin, 2 * app.boardMargin + app.topTextHeight 
                 + app.boardSize, app.boardSize, app.boardSize,
                fill=None, border='black', borderWidth=app.cellBorderWidth*2)
    # Draws the indiviual cells
    for row in range(app.size):
        for col in range(app.size):
            drawCell(app, grid, row, col, atTop)

# Draws each indiviual cell
def drawCell(app, grid, row, col, atTop):
    cellLeft, cellTop, cellSize = getCellLeftTop(app, row, col, atTop)
    color = getColor(app, grid, row, col, atTop)
    if color == 'red':
        color = None
        drawImage('trainSide.png', cellLeft, cellTop)
    elif color == 'lime':
        drawImage('trainSide.png', cellLeft, cellTop)
        drawX(app, row, col, atTop, 'red')
        color = None
    elif color == 'blue':
        color = None
        drawX(app, row, col, atTop, 'blue')

    drawRect(cellLeft, cellTop, cellSize, cellSize,
             fill=color, border='black',
             borderWidth=app.cellBorderWidth)

def drawX(app, row, col, atTop, color):
    cellLeft, cellTop, cellSize = getCellLeftTop(app, row, col, atTop)
    drawLine(cellLeft + 2, cellTop + 2, cellLeft + cellSize - 2, 
             cellTop + cellSize - 2, fill = color, lineWidth = 5)
    drawLine(cellLeft + 2, cellTop + cellSize - 2, cellLeft + cellSize - 2, 
             cellTop + 2, fill = color, lineWidth = 5)

# Gets what color that cell should be
def getColor(app, grid, row, col, atTop):
    if atTop and app.showSolution and grid[row][col]:
        color = 'red'
        if app.player.guessBoard.grid[row][col]:
            color = 'lime'
    elif atTop and grid[row][col] and app.player.guessBoard.grid[row][col]:
        color = 'lime'
    elif atTop == False and grid[row][col]:
        color = 'red'
        if app.computer.guessBoard.grid[row][col]:
            color = 'lime'
    else:
        color = None
        if atTop and app.player.guessBoard.grid[row][col] == False:
            color = 'blue'
        elif atTop == False and app.computer.guessBoard.grid[row][col] == False:
            color = 'blue'
    return color

# Gets the x and y position for each cell given a row and column
def getCellLeftTop(app, row, col, atTop):
    cellSize = app.boardSize / app.size
    if atTop:
        cellTop = app.boardMargin + (row * cellSize)
    else:
        cellTop = 2 * app.boardMargin + (row * cellSize) + app.boardSize
    # Adds room for the title at the top
    cellTop += app.topTextHeight
    cellLeft = app.boardMargin + (col * cellSize)
    return cellLeft, cellTop, cellSize
