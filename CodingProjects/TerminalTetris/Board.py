import time
import os
import random
from Pieces import PIECES

BOARD_WIDTH = 10
BOARD_HEIGHT = 20

board = []
stdscr = None
score = 0

currentPiece = {
    "type": random.choice(list(PIECES.keys())),
    "rotation": 0,
    "x": 4,
    "y": 0
}

# Create the width and height of the board
for i in range(BOARD_HEIGHT):
    row = [0] * BOARD_WIDTH
    board.append(row)

for i in range(BOARD_WIDTH):
    board[19][i] = 1


def displayBoard(curses):
    '''Render the board and pieces.'''
    global stdscr
    stdscr = curses

    blockLocation = [] # Holds location of the current piece

    for offsetX, offsetY in PIECES[currentPiece["type"]][currentPiece["rotation"]]:

        blockX = currentPiece["x"] + offsetX
        blockY = currentPiece["y"] + offsetY

        blockLocation.append((blockX, blockY))

    stdscr.clear()

    for y in range(len(board)):
        rowString = ""
        for x in range(len(board[y])):
            if (x, y) in blockLocation:
                rowString += "#"
            elif board[y][x] == 1:
                rowString += "#"
            else:
                rowString += "."
        stdscr.addstr(y, 20, rowString)

    displayScore()
    stdscr.refresh()
        
def displayScore():
    global score
    stdscr.addstr(2, 50, "TOTAL SCORE: " + str(score))

def pieceDown():
    '''Move the piece down 1 unit.'''
    if isValidPosition(currentPiece["x"], currentPiece["y"] + 1):
        currentPiece["y"] += 1
    else:
        placePiece(currentPiece)

def pieceLeft():
    '''Move the piece left 1 unit'''
    if isValidPosition(currentPiece["x"] - 1, currentPiece["y"]):
        currentPiece["x"] += -1
    
def pieceRight():
    '''Move the piece right 1 unit'''
    if isValidPosition(currentPiece["x"] + 1, currentPiece["y"]):
        currentPiece["x"] += 1

def pieceRotate():
    '''Rotate the piece.'''
    nextRotation = (currentPiece["rotation"] + 1) % len(PIECES[currentPiece["type"]])

    if isValidPosition(currentPiece["x"], currentPiece["y"], nextRotation):
        currentPiece["rotation"] = nextRotation

def isValidPosition(newX, newY, newRotation=None):
    shape = PIECES[currentPiece["type"]][currentPiece["rotation"]] if newRotation is None else PIECES[currentPiece["type"]][newRotation]

    for offsetX, offsetY in shape:
        blockX = newX + offsetX
        blockY = newY + offsetY

        if not (0 <= blockX < BOARD_WIDTH and 0 <= blockY < BOARD_HEIGHT):
            return False

        if board[blockY][blockX] == 1:
            return False

    return True
        
def placePiece(piece):
    '''Place the current piece onto the grid.'''
    blockLocation = [] # Holds location of the current piece

    for offsetX, offsetY in PIECES[piece["type"]][piece["rotation"]]:

        blockX = piece["x"] + offsetX
        blockY = piece["y"] + offsetY

        blockLocation.append((blockX, blockY))

    for x, y in blockLocation:
        board[y][x] = 1 # Turns it into the object shape

    lineCheck()
    createPiece()

def createPiece():
    '''Create a new piece. Pass a parameter if you want a specific one.'''
    global currentPiece
    currentPiece = {
        "type": random.choice(list(PIECES.keys())),
        "rotation": 0,
        "x": 4,
        "y": 0
}
    
    if isValidPosition(currentPiece["x"], currentPiece["y"]) == False:
        gameOver()

def gameOver():
        '''End the game.'''
        for _ in range(3):
            stdscr.clear()
            stdscr.addstr("--GAME OVER--")
            stdscr.refresh()
            time.sleep(1)

            stdscr.clear()
            displayBoard(stdscr)
            stdscr.refresh()
            time.sleep(1)
        
        os._exit(1)

def lineCheck():
    '''Check if a line has been completed.'''
    newBoard = []
    clearedLines = 0
    global score

    for row in board:
        if 0 in row:
            newBoard.append(row)
        else:
            clearedLines += 1

        
    for _ in range(clearedLines):
        newBoard.insert(0, [0] * BOARD_WIDTH)

    match clearedLines:
        case 0:
            score += 0
        case 1: 
            score += 100
        case 2:
            score += 300
        case 3:
            score += 500
        case _: # 4+
            score += 800

    board[:] = newBoard