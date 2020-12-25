boardOne = ['###@@@###', '###@@@###', '@@@@@@@@@', '@@@@-@@@@', '@@@@@@@@@', '###@@@###', '###@@@###']

boardTwo = ['#-@@-#', '-@@@@-', '@@@@@@', '@@@@@@', '-@@@@-', '#-@@-#']

boardThree = ['###-@-###', '##-@@@-##', "#-@@-@@-#", "-@@@@@@@-"]

boardFour = ['-----', '-@@@-', '--@--', '--@--', '-----']


directionNames = {
    1: "Up",
    2: "Down",
    3: "Left",
    4: "Right",
}

boards = (boardOne, boardTwo, boardThree, boardFour)

def readValidInt(prompt, minChoice, maxChoice):
        print(prompt)
        while True:
            choice = input()
            try:
                int(choice)
                if(int(choice) > maxChoice) or (int(choice) < minChoice):
                    print("Please choose a integer between " + str(minChoice) + ' and ' + str(maxChoice))
                    choice = input()
                else:
                    return choice
            except ValueError:
                print("Please choose a integer between " + str(minChoice) + ' and ' + str(maxChoice))
        




def main():
    print("WELCOME TO CS300 PEG SOLITAIRE! \n ===============================")
    boardType = readValidInt("Board Style Menu: \n 1) Cross \n 2) Circle \n 3) Triangle \n 4) Simple T", 1, 4)
    initialBoard = boards[(int(boardType) - 1)]
    boardHeight = len(initialBoard)
    boardWidth = len(initialBoard[1])
    
    def createBoard(boardInput): #intializes board depending on type selected by user
        for i in range(len(boardInput)):
            print(boardInput[i])
    
    def displayBoard(currentBoard):
        boardDisplay = currentBoard
        #side grid numbers
        for i in range(boardHeight):
            boardDisplay[i] = str(i + 1) + " " + currentBoard[i]

        #top grid numbers
        width = []
        for int in range(boardWidth):
            width.append(str(int + 1))
        topGrid = "  " + "".join(width)
        boardDisplay.insert(0,topGrid)
        
        return boardDisplay
    def isValidMove(currentBoard, row, column, direction):    
            if direction == 1:
                if (row-2>0):
                    if currentBoard[row-2][column] == "-":
                        if currentBoard[row-1][column] == "@":
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            elif direction == 2:
                if (row+2 < len(currentBoard)):
                    if currentBoard[row+2][column] == "-":
                        if currentBoard[row+1][column] == "@":
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            elif direction == 3:
                if (column - 2 > 1):
                    if currentBoard[row][column-2] == "-":
                        if currentBoard[row][column - 1] == "@":
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            elif direction == 4:
                if (column + 2 < len(currentBoard[1])):
                    if currentBoard[row][column+2] == "-":
                        if currentBoard[row][column+1] == "@":
                            return True
                        else: 
                            return False
                    else:
                        return False
                else:
                    return False

    def readValidMove(currentBoard):
        rowChoice = int(readValidInt("Select a row to move from:", 1, boardHeight)) 
        columnChoice = int(readValidInt("Select a column to move from:",1,boardWidth)) + 1
        directionChoice = int(readValidInt("Select a direction to move from: \n 1) Up \n 2) Down \n 3) Left \n 4) Right", 1,4))

        while True:
            #validating if peg exists in chosen spot
            if currentBoard[rowChoice][columnChoice] == "@":
                if isValidMove(currentBoard, rowChoice, columnChoice, directionChoice) == True:
                    break
                else:
                    print("Moving a peg from row " + str(rowChoice) + " and column " + str(columnChoice-1) + " in the direction of " + directionNames[directionChoice] + " is not a valid move. Please enter a valid move.")
                    createBoard(currentBoard)
                    rowChoice = int(readValidInt("Select a row to move from:", 1, boardHeight))
                    columnChoice = int(readValidInt("Select a column to move from:",1,boardWidth)) + 1
                    directionChoice = int(readValidInt("Select a direction to move from: \n 1) Up \n 2) Down \n 3) Left \n 4) Right", 1,4))
            else:
                print("Moving a peg from row " + str(rowChoice) + " and column " + str(columnChoice-1) + " in the direction of " + directionNames[directionChoice] + " is not a valid move. Please enter a valid move.")
                createBoard(currentBoard)
                rowChoice = int(readValidInt("Select a row to move from:", 1, boardHeight))
                columnChoice = int(readValidInt("Sel1ect a column to move from:",1,boardWidth)) + 1
                directionChoice = int(readValidInt("Select a direction to move from: \n 1) Up \n 2) Down \n 3) Left \n 4) Right", 1,4))

        moveChoice = [rowChoice, columnChoice, directionChoice]
        return moveChoice

    
    def performMove(currentBoard, row, column, direction):
        def moveUp(currentBoard, row, column):
            tempRowFrom = list(currentBoard[row])
            tempRowBetween = list(currentBoard[row-1])
            tempRowTo = list(currentBoard[row-2])
            tempRowFrom[column] = "-"
            tempRowBetween[column] = "-"
            tempRowTo[column] = "@"
            tempRowTo = "".join(tempRowTo)
            tempRowBetween = "".join(tempRowBetween)
            tempRowFrom = "".join(tempRowFrom)
            currentBoard[row] = tempRowFrom
            currentBoard[row-1] = tempRowBetween
            currentBoard[row-2] = tempRowTo
        def moveDown(currentBoard, row, column):
            tempRowFrom = list(currentBoard[row])
            tempRowTo = list(currentBoard[row+2])
            tempRowBetween = list(currentBoard[row+1])
            tempRowFrom[column] = "-"
            tempRowBetween[column] = "-"
            tempRowTo[column] = "@"
            tempRowTo = "".join(tempRowTo)
            tempRowFrom = "".join(tempRowFrom)
            tempRowBetween = "".join(tempRowBetween)
            currentBoard[row] = tempRowFrom
            currentBoard[row+1] = tempRowBetween
            currentBoard[row+2] = tempRowTo
        def moveLeft(currentBoard, row, column):
            tempRow = list(currentBoard[row])
            tempRow[column] = "-"
            tempRow[column - 1] = "-"
            tempRow[column - 2] = "@"
            tempRow = "".join(tempRow)
            currentBoard[row] = tempRow
        def moveRight(currentBoard, row, column):
            tempRow = list(currentBoard[row])
            tempRow[column] = "-"
            tempRow[column + 1] = "-"
            tempRow[column + 2] = "@"
            tempRow = "".join(tempRow)
            currentBoard[row] = tempRow
        if direction == 1:
            moveUp(currentBoard, row, column)
        elif direction == 2:
            moveDown(currentBoard, row, column)
        elif direction == 3:
            moveLeft(currentBoard, row, column)
        elif direction == 4:
            moveRight(currentBoard, row, column)
    def countPegsRemaining(currentBoard):
        pegCount = 0
        for row in range(len(currentBoard)):
            tempCountRow = list(currentBoard[row])
            for char in range(len(tempCountRow)):
                if tempCountRow[char] == "@":
                    pegCount += 1
        return pegCount



    def checkMovesAvailable(currentBoard):
        movesAvailable = 0
        for row in range(len(currentBoard)):
            tempCountRow = list(currentBoard[row])
            for char in range(len(tempCountRow)):
                if tempCountRow[char] == "@":
                    for dimensions in range(4):
                        if isValidMove(currentBoard, row, char, dimensions) == True:
                            movesAvailable += 1
        return movesAvailable

    xBoard = displayBoard(initialBoard)
    while True:
        createBoard(xBoard)
        moves = readValidMove(xBoard)
        performMove(xBoard, moves[0], moves[1], moves[2])
        pegsRemaining = countPegsRemaining(xBoard)
        movesPossible = checkMovesAvailable(xBoard)
        if pegsRemaining == 1:
            print("Congratulations! You beat the game")
            break
        elif pegsRemaining > 1 and movesPossible == 0:
            print("You have no available moves. You lost")
            break
        else:
            print("You have " + str(pegsRemaining) + " pegs remaining and " + str(movesPossible) + " moves possible")


main()


