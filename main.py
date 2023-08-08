from drawingHelpers import *
from otherHelpers import *
from player import *
from button import *
from computer import *

def onAppStart(app):
    restart(app)

def onStep(app):
    checkForWin(app)
    if app.screen == 'game':
        app.steps += 1
        # Adds a delay between player's guess and computer's guess
        if app.steps == app.unPauseTime and app.paused:
            app.computer.guess(app)
            app.paused = False
            app.yourTurn = True

def onMousePress(app, mouseX, mouseY):
    if app.paused:
        return
    # Start screen buttons
    if app.screen == 'start':
        for button in app.startButtonList:
            checkButtonPressed(app, button, mouseX, mouseY)
    # Board creation screen buttons and grid presses
    elif app.screen == 'boardCreation':
        # Checks if the mouse was clicked in grid area
        if checkGridPressed(app, mouseX, mouseY)[0]:
            # Checks if the player has enough pieces left to place a piece
            if app.player.piecesPlaced <= app.pieces:
                # Checks which grid (top or bottom) was clicked
                if checkGridPressed(app, mouseX, mouseY)[1]:
                    app.player.topBoardPressed(app, mouseX, mouseY, True)
                else:
                    app.player.bottomBoardPressed(app, mouseX, mouseY, False)
        else: # Otherwise checks if the mouse was clicked in a button area
            for button in app.boardCreationButtonList:
                checkButtonPressed(app, button, mouseX, mouseY)
    # Game screen buttons and grid presses
    elif app.screen == 'game':
        # Checks if the mouse was clicked in grid area
        if checkGridPressed(app, mouseX, mouseY)[0]:
            # Checks if the player has enough pieces left to place a piece
            if app.player.piecesPlaced <= app.pieces:
                # Checks which grid (top or bottom) was clicked
                if checkGridPressed(app, mouseX, mouseY)[1]:
                    app.player.topBoardPressed(app, mouseX, mouseY, True)
                else:
                    app.player.bottomBoardPressed(app, mouseX, mouseY, False)
        else: # Otherwise checks if the mouse was clicked in a button area
            for button in app.boardCreationButtonList:
                checkButtonPressed(app, button, mouseX, mouseY)
    # Instructions screen buttons
    elif app.screen == 'rules':
        checkButtonPressed(app, app.backButton, mouseX, mouseY)

def onKeyPress(app, key):
    # Quick randomize board button
    if key == 'r' and app.screen == 'boardCreation':
        app.player.pieceBoard.grid = randomizeBoard(app)
        app.computer.pieceBoard.grid = randomizeBoard(app)
        piecesPlaced = Player.updatePiecesPlacedCount(app.player, app)
        app.player.piecesPlaced = piecesPlaced
    elif key == 's':
        app.showSolution = not app.showSolution
    elif key == 'k':
        app.computer.pieceBoard.grid = randomizeBoard(app)

def redrawAll(app):
    # CITATION: I got this texture from
    """
    <a href="https://www.freepik.com/free-photo/abstract-bright-green-square-
    pixel-tile-mosaic-wall-background-texture_18487439.htm#query=pixel%20texture
    %20grass&position=1&from_view=keyword&track=ais">Image by benzoix</a> on 
    Freepik 
    """
    drawImage('grass.png', 0, 0)
    if app.screen == 'start':
        drawStartScreen(app)
    elif app.screen == 'boardCreation':
        drawBoardCreation(app)
    elif app.screen == 'game':
        drawGameScreen(app)
    elif app.screen == 'rules':
        drawRulesScreen(app)
        

def main():
    runApp(500, 800)

main()
