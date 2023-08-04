from helpers import *
from player import *
from button import *

def onAppStart(app):
    restart(app)

def onStep(app):
    pass

def onMousePress(app, mouseX, mouseY):
    # Start screen buttons
    if app.screen == 'start':
        for button in app.startButtonList:
            checkButtonPressed(app, button, mouseX, mouseY)
    # Board creation screen buttons and grid presses
    elif app.screen == 'boardCreation':
        # Checks if the mouse was clicked in grid area
        if checkGridPressed(app, mouseX, mouseY)[0]:
            if checkGridPressed(app, mouseX, mouseY)[1] == True:
                app.player.topBoardPressed(app, mouseX, mouseY, True)
            else:
                app.player.bottomBoardPressed(app, mouseX, mouseY, False)
        else: # Otherwise checks if the mouse was clicked in a button area
            for button in app.boardCreationButtonList:
                checkButtonPressed(app, button, mouseX, mouseY)

def onMouseRelease(app, mouseX, mouseY):
    pass

def redrawAll(app):
    if app.screen == 'start':
        drawStartScreen(app)
    elif app.screen == 'boardCreation':
        drawBoardCreation(app)
    elif app.screen == 'game':
        drawLabel('BattleTrains', app.width / 2, app.boardMargin * 2, size = 69)

def main():
    runApp(500, 800)

main()
