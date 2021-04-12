"""
Project #1: A Simple Game: CONNECT 4
"""

from termcolor import colored, cprint

Fields = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]

def drawField(Fields):
    for row in range(13):
        if row%2 == 0:
            practicalRow = int(row/2)
            for column in range(13):
                if column%2 == 0:
                    practicalColumn = int(column/2)
                    color = "white"
                    if Fields[practicalColumn][practicalRow] == "X":
                        color = "red"
                    tile = colored(Fields[practicalColumn][practicalRow],color,attrs=['bold'])
                    if column != 12:
                        print(tile,end="")
                    else:
                        print(tile)
                else:
                    print("│",end="")
        else:
            print("-"*13)
            
    print("\n")
    
    
def updateField(num, player):
    column = Field[num]
    index = ""
    ReversedColumn = column[::-1]
    for row in ReversedColumn:
        if row == "":
            index = ReversedColumn.index(row)
            ReversedColumn[index] = "X" if player == 1 else "O"
            break
    if index == "":
        return False
    column = ReversedColumn[::-1]
    Fields[num] = column
    drawField(Fields)
    return True


def checkIfFourInRow():
    Winner = False
    for column in Fields:
        counter = 0
        length = len(column)
        for i in range(1, length):
            if column[i - 1] != " " and column[i] != " " and column[i-1] == column[i]:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                winner column[i - 1]
                return winner
    return winner

def checkIfFourInColumn(columnMatrix):
    winner = False
    for column in columnMatrix:
        counter = 0
        length = len(column)
        for i in range(1, length):
            if column[i - 1] != " " and column[i] != " " and column[i-1] == column[i]:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                winner column[i - 1]
                return winner
    return winner

def checkIfFourInForwardDiagonal(columnMatrix, player):
    for i in range(0, len(columnMatrix)):
        for j in range(0, len(columnMatrix[i])):
            try:
                if columnMatrix[i][j] == player and columnMatrix[i + 1][j - 1] == player and column:
                    return True
            except IndexError:
                next
    return False


def checkIfFourInBackwardDiagonal(columnMatrix, player):
    for i in range(0, len(columnMatrix)):
        for j in range(0, len(columnMatrix[i])):
            try:
                if columnMatrix[i][j] == player and columnMatrix[i + 1][j + 1] == player and column:
                    return True
            except IndexError:
                next
    return False
    

def IsValidMove(columnNo):
    if columnNo >= 1 and columnNo <= 7:
        return True
    else:
        return False

def createColumnMatrix():
    columnMatrix = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
    for i in range(7):
        for j in range(len(Fields[i])):
            columnMatrix[j][i] = Fields[i][j]

    return columnMatrix

def BeginConnect4():
    player = 1
    NoWin = True
    winner = ""
    while(NoWin):
        AskColumn = colored('Player ' + str(player) + ' turn, Enter the column number:\n', "yellow",attr=['bold'])
        columnNo = input(AskColumn)
        if columnNo:
            columnNo = int(columnNo)
            if isValidMove(columnNo) == False:
                cprint('This is a wrong move. Try again.\n', 'red',attrs=['bold'])
            else:
                updatedFlag = updateField(columnNo - 1, player)
                if updatedFlag:
                    print("")
                    currentPlayer = player
                    tile = "X" if player == 1 else "0"
                    player = 2 if player == 1 else 1
                    winner = checkIfFourInRow()
                    if winner:
                        NoWin = False
                    else:
                        columnMatrix = createColumnMatrix()
                        winner = checkIfFourInColumn(columnMatrix)
                        if winner:
                            NoWin = False
                        elif checkIfFourInBackwardDiagonal(columnMatrix, tile):
                            winner = currentPlayer
                            NoWin = False
                        elif checkIfFourInForwardDiagonal(columnMatrix, tile):
                            winner = currentPlayer
                            NoWin = False
                    else:
                        cprint('This is a wrong move. Try again.\n', 'red', attrs=['bold'])
        else:
            cprint('This is a wrong move. Try again.\n', 'red', attrs=['bold'])

    if winner == "X":
        winner = "1"
    else:
        winner = "2"
    cprint('The WINNER IS PLAYER '+ str(winner), 'blue', attrs=['bold'])

print("Starting Connect 4 Game...!\n")

drawField(Fields)
BeginConnect4()
