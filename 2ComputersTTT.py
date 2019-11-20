from random import randrange

#==================== FUNCTIONS ====================#
# Draws the current state of the board
def drawBoard(board):
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

# Randomly choose which computer will go first
def setFirst():
    if(randrange(2) == 0):
        return 'X'
    else:
        return 'O'

#Get the computer's move
def getMove(board):
    move = randrange(9)
    while(not legalMove(board, move)):
        move = randrange(9)
    return move

# Check that the intended move is legal
def legalMove(board, move):
    return board[move] == ' '

# Add a move to the board
def makeMove(board, char, move):
    board[move] = char

def changeTurn(char, charTurn):
    if(char == 'X'):
        return 'O'
    else:
        return 'X'

def isBoardFull(board):
    for space in board:
        if(space == ' '):
            return False
    return True

# Checks to see if the player has won
def checkWinner(board, char):
    return((board[0] == char and board[1] == char and board[2] == char) or
           (board[3] == char and board[4] == char and board[5] == char) or
           (board[6] == char and board[7] == char and board[8] == char) or
           (board[0] == char and board[3] == char and board[6] == char) or
           (board[1] == char and board[4] == char and board[7] == char) or
           (board[2] == char and board[5] == char and board[8] == char) or
           (board[0] == char and board[4] == char and board[8] == char) or
           (board[2] == char and board[4] == char and board[6] == char))

def playGame():
    # Set the computers' characters
    comp1Char = 'X'
    comp2Char = 'O'

    # Randomly choose which computer will go first
    #charTurn = setFirst()
    charTurn = 'X'

    gameOver = False
    gameBoard = [' '] * 9
    #drawBoard(gameBoard)
    
    while(not gameOver):
        if(charTurn == comp1Char):
            # Get the index of the computer's intended move
            moveIndex = getMove(gameBoard)

            # Update the board with the player's intended move
            makeMove(gameBoard, comp1Char, moveIndex)
            #drawBoard(gameBoard)

            # Make it the other computer's turn
            charTurn = changeTurn(comp1Char, charTurn)

            # Check if the computer has won the game
            if(checkWinner(gameBoard, comp1Char)):
                return 1
                gameOver = True

        # The computer's turn
        else:
            # Get the index of the computer's intended move
            moveIndex = getMove(gameBoard)

            # Update the board with the player's intended move
            makeMove(gameBoard, comp2Char, moveIndex)
            #drawBoard(gameBoard)

            # Make it the other computer's turn
            charTurn = changeTurn(comp2Char, charTurn)

            # Check if the computer has won the game
            if(checkWinner(gameBoard, comp2Char)):
                return 2
                gameOver = True
                
        if(not gameOver):
            if(isBoardFull(gameBoard)):
                return 0
                gameOver = True


                
#================= INTRO AND SETUP =================#
# Welcome message and ask player for character
print("Welcome to Tic-Tac-Toe!")
print("Clash of the Computers")

c1Wins = 0
c2Wins = 0
ties = 0

numGames = 100000
for i in range(0, numGames, 1):
    result = playGame()
    if(result == 1):
        c1Wins += 1
    elif(result == 2):
        c2Wins += 1
    else:
        ties += 1

print()
print("Computer 1 won the game ", (c1Wins/numGames)*100, "% of the time")
print("Computer 2 won the game ", (c2Wins/numGames)*100, "% of the time")
print("The computers tied ", (ties/numGames)*100, "% of the time")
    
