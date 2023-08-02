from helpers import *
from Player import *

def onAppStart(app):
    restart(app)

def onStep(app):
    pass

def onMousePress(app):
    pass

def onMouseRelease(app):
    pass

def redrawAll(app):
    if app.screen == 'start':
        drawStartScreen(app)
    elif app.screen == 'game' or app.screen == 'boardCreation':
        drawLabel('BattleTrains', app.width / 2, app.boardMargin * 2, size = 69)
        drawBoard(app, app.player.guessBoard.grid, atTop=True)
        drawBoard(app, app.player.pieceBoard.grid, atTop=False)

def main():
    runApp(500, 800)

main()
