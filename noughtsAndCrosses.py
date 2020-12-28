# clearBoard which sets all locations on the board to the BLANK character.
# printBoard which prints the board to the screen in the format shown.
# canMakeMove which takes a board and a location and returns whether a move can be made there.
# makeMove which adds a piece (NOUGHT or CROSS) to the board in the specified location.
# isBoardFull which indicates whether the board is full.
# winner which returns the piece which has won or BLANK if no-one has yet won.
col1 = [' ', ' ', ' ']
col2 = [' ', ' ', ' ']
col3 = [' ', ' ', ' ']
counter = 1
def clearBoard():
    col1 = [' ', ' ', ' ']
    col2 = [' ', ' ', ' ']
    col3 = [' ', ' ', ' ']
def printBoard(col1, col2,col3):
    print('------------', '|', col1[2], '|', col2[2], '|', col3[2], '|', '\n', '------------',
         '|', col1[1], '|', col2[2], '|', col3[2], '|', '\n',
          '------------', '|', col1[0], '|', col2[0], '|', col3[0], '|', '------------')

def canMakeMove(row, column, symbol):
    if(column == 1):
        if (row.isdigit and row<=3 and row>0):
            if (col1[row]==' '):
                col1[row]==symbol
    elif (column == 2):
        if (row.isdigit and row <= 3 and row > 0):
            if (col2[row] == ' '):
                 col2[row] == symbol
    elif (column == 3):
        if (row.isdigit and row <= 3 and row > 0):
            if (col3[row] == ' '):
                 col3[row] == symbol

def makeMove():

def isBoardFull(col1, col2, col3):
    while

finished = 1

canMakeMove()

