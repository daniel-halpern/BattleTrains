from cmu_graphics import *
from player import *
from button import *
from computer import *

# Drawing the start screen
def drawStartScreen(app):
    drawLabel('BattleTrains', app.width / 2, app.boardMargin * 3, size = 79)
    drawLabel('Welcome to BattleTrains!', app.width / 2, app.boardMargin * 5, 
               size = 30)
    drawLabel('Try and destroy all the', app.width / 2, app.boardMargin * 6, 
               size = 30)
    drawLabel("opponent's train cars", app.width / 2, app.boardMargin * 7, 
               size = 30)
    drawLabel("before they get yours!", app.width / 2, app.boardMargin * 8, 
               size = 30)
    for button in app.startButtonList:
        Button.drawButton(button, app)

# Drawing the rules screen
def drawRulesScreen(app):
    topDist = app.boardMargin
    drawLabel('The Rules:', app.width / 2, app.boardMargin * 3, size = 79)
    drawLabel('During set up, you must place', app.width / 2, topDist * 5, 
               size = 30)
    drawLabel('down 10 pieces, known as train', app.width / 2, topDist * 6, 
               size = 30)
    drawLabel('cars, on the bottom grid.', app.width / 2, topDist * 7, 
               size = 30)
    drawLabel('When you place down a train car', app.width / 2, topDist * 9, 
               size = 30)
    drawLabel('that is not connected to any', app.width / 2, topDist * 10, 
               size = 30)
    drawLabel('other train car, it becomes a', app.width / 2, topDist * 11, 
               size = 30)
    drawLabel('train.', app.width / 2, topDist * 12, 
               size = 30)
    drawLabel('In order for a board to be legal,', app.width / 2, topDist * 14, 
               size = 30)
    drawLabel('it must not have more than 5', app.width / 2, topDist * 15, 
               size = 30)
    drawLabel('trains, with each of these trains', app.width / 2, topDist * 16, 
               size = 30)
    drawLabel('being longer than 2 cars and', app.width / 2, topDist * 17, 
               size = 30)
    drawLabel('no train car can touch another', app.width / 2, topDist * 18, 
               size = 30)
    drawLabel('train car that isnt a subsequent', app.width / 2, topDist * 19, 
               size = 30)
    drawLabel('part of that train.', app.width / 2, topDist * 20, 
               size = 30)
    Button.drawButton(app.backButton, app)

# Draw the win / lose screen
def drawWinLoseScreen(app):
    if app.screen == 'win':
        drawLabel('You win!', app.width / 2, app.boardMargin * 2, size = 70)
    else:
        drawLabel('You lose!', app.width / 2, app.boardMargin * 2, size = 70)
    drawBoard(app, app.computer.pieceBoard.grid, atTop=True)
    drawBoard(app, app.player.pieceBoard.grid, atTop=False)
    drawBoard(app, app.player.guessBoard.grid, atTop=True)
    for button in app.winLoseButtonList:
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
                        button.color = 'gray'
        Button.drawButton(button, app)
    # Draw pieces left sidebar label
    drawLabel('Pieces left', app.midX, 6 * app.boardMargin + app.topTextHeight, 
              size = 20)
    drawLabel(app.pieces - app.player.piecesPlaced, app.midX, 6 * 
              app.boardMargin + app.topTextHeight + 50, size = 50)

# Takes a list of trains and places them on a grid
def turnTrainListIntoGrid(trainList, grid, colorGrid):
    trainNum = 0
    for train in trainList:
        for car in train.carList:
            grid[car[0]][car[1]] = True
            colorGrid.grid[car[0]][car[1]] = trainNum
        trainNum += 1
    return grid, colorGrid

# Draw the board
# CITATION: I based this function off of the drawBoard function from the Tetris 
# project
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
        turnTrainListIntoGrid(app.player.trainList, grid, 
                              app.player.pieceBoardColors)
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

# CITATION: I based this function off of the drawCell function from the Tetris 
# project
# Draws each indiviual cell
def drawCell(app, grid, row, col, atTop):
    cellLeft, cellTop, cellSize = getCellLeftTop(app, row, col, atTop)
    color, piece = getColor(app, grid, row, col, atTop)
    if piece == 'train':
        drawImageColored(app, color, cellLeft, cellTop, atTop)
    elif piece == 'hit':
        drawImageColored(app, color, cellLeft, cellTop, atTop)
        drawX(app, row, col, atTop, 'red')
    elif piece == 'miss':
        drawX(app, row, col, atTop, 'blue')
    drawRect(cellLeft, cellTop, cellSize, cellSize,
             fill=None, border='black',
             borderWidth=app.cellBorderWidth)

def drawImageColored(app, color, x, y, atTop):
    if not atTop:
        for train in app.player.trainList:
            if (x,y) in train.carList:
                color = train.color
    if color == 0:
        drawImage('trainSide0.png', x, y)
    elif color == 1:
        drawImage('trainSide1.png', x, y)
    elif color == 2:
        drawImage('trainSide2.png', x, y)
    elif color == 3:
        drawImage('trainSide3.png', x, y)
    elif color == 4:
        drawImage('trainSide4.png', x, y)
    else:
        drawImage('trainSide.png', x, y)

# Draws the red or blue hit / miss
def drawX(app, row, col, atTop, color):
    cellLeft, cellTop, cellSize = getCellLeftTop(app, row, col, atTop)
    drawLine(cellLeft + 2, cellTop + 2, cellLeft + cellSize - 2, 
             cellTop + cellSize - 2, fill = color, lineWidth = 5)
    drawLine(cellLeft + 2, cellTop + cellSize - 2, cellLeft + cellSize - 2, 
             cellTop + 2, fill = color, lineWidth = 5)

# Gets what color that cell should be
def getColor(app, grid, row, col, atTop):
    color = None
    if atTop and app.showSolution and grid[row][col]:
        piece = 'train'
        color = app.computer.pieceBoardColors.grid[row][col]
        if app.player.guessBoard.grid[row][col]:
            piece = 'hit'
    elif atTop and grid[row][col] and app.player.guessBoard.grid[row][col]:
        piece = 'hit'
        color = app.computer.pieceBoardColors.grid[row][col]
    elif atTop == False and grid[row][col]:
        piece = 'train'
        color = app.player.pieceBoardColors.grid[row][col]
        if app.computer.guessBoard.grid[row][col]:
            piece = 'hit'
    else:
        piece = None
        if atTop and app.player.guessBoard.grid[row][col] == False:
            piece = 'miss'
        elif atTop == False and app.computer.guessBoard.grid[row][col] == False:
            piece = 'miss'
    return color, piece

# Gets the x and y position for each cell given a row and column
# CITATION: I based this function off of the getCellLeftTop from the Tetris 
# project
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
