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

# Sets the computer's character depending on what the player has chosen
def setCompChar(playerChar):
    if(playerChar == 'X'):
        return 'O'
    else:
        return 'X'

# Randomly choose if the user or computer will go first
# Return True if player goes first, False if computer does
def setPlayerOrder():
    if(randrange(2) == 0):
        print("The Computer has been randomly chosen to go first!")
        return False
    else:
        print("You have been randomly chosen to go first!")
        return True

# Get the player's move
def getPlayerMove(board):
    print("Where would you like to make a move? (1-9)")
    move = input()
    while((move not in '1 2 3 4 5 6 7 8 9'.split()) or not legalMove(board, int(move)-1)):
        print("That is not a valid option. Please enter a number from 1 - 9")
        move = input()
    return int(move) - 1

#Get the computer's move
def getCompMove(board):
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
           
    
#================= INTRO AND SETUP =================#
# Welcome message and ask player for character
print("Welcome to Tic-Tac-Toe!")
print("Would you like to play as X or O?")
playerChar = input()

# Make sure that the user inputs either an x or an o
while(playerChar.lower() != 'x' and playerChar.lower() != 'o'):
    print("That is not a valid option. Please enter 'X' or 'O'.")
    playerChar = input()
playerChar = playerChar.upper()
print("You will be playing as: " + playerChar)

# Set the computer's character
compChar = setCompChar(playerChar)

# Randomly choose if the user or computer will go first
playerTurn = setPlayerOrder()

#==================== GAME LOOP ====================#
# Board Variables and Instantiation
gameOver = False
gameBoard = [' '] * 9
drawBoard(gameBoard)

# The game will loop until there is a winner
while(not gameOver):
    if(playerTurn):
        # Get the index of the player's intended move
        moveIndex = getPlayerMove(gameBoard)

        # Update the board with the player's intended move
        makeMove(gameBoard, playerChar, moveIndex)
        drawBoard(gameBoard)

        # Make it the computer's turn
        playerTurn = False

        #Check to see if the player has won the game
        if(checkWinner(gameBoard, playerChar)):
            print("You Win!")
            gameOver = True

    # The computer's turn
    else:
        print("The computer will now make their move")
        # Get the index of the computer's intended move
        moveIndex = getCompMove(gameBoard)

        # Update the board with the player's intended move
        makeMove(gameBoard, compChar, moveIndex)
        drawBoard(gameBoard)

        # Make it the player's turn
        playerTurn = True

        # Check if the computer has won the game
        if(checkWinner(gameBoard, compChar)):
            print("The Computer Wins!")
            gameOver = True
            
    if(not gameOver):
        if(isBoardFull(gameBoard)):
            print("There are no more possible moves!")
            print("You have tied.")
            gameOver = True













    
    
