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

# Used in creating all possible board configurations
def determineChar(index):
    if(index == 0):
        return ' '
    elif(index == 1):
        return 'X'
    else:
        return 'O'

# Checks if a board configuration is valid
def checkValid(board):
    xCount = 0
    oCount = 0
    for i in range(0, len(board), 1):
        if(board[i] == 'X'):
            xCount += 1
        elif(board[i] == 'O'):
            oCount += 1

    if((xCount - oCount) == 1):
        if(checkWinner(board, 'O')):
            return False
        return True
    elif((xCount - oCount) == 0):
        if(checkWinner(board, 'X')):
            return False
        return True
    else:
        return False

# Creates and returns an array of all legal combinations of boards
def initStates():
    states = []

    count = 0
    gameBoard = [' '] * 9

    for i in range(0,3,1):
        gameBoard[0] = determineChar(i)
        for j in range(0,3,1):
            gameBoard[1] = determineChar(j)
            for k in range(0,3,1):
                gameBoard[2] = determineChar(k)
                for l in range(0,3,1):
                    gameBoard[3] = determineChar(l)
                    for m in range(0,3,1):
                        gameBoard[4] = determineChar(m)
                        for n in range(0,3,1):
                            gameBoard[5] = determineChar(n)
                            for o in range(0,3,1):
                                gameBoard[6] = determineChar(o)
                                for p in range(0,3,1):
                                    gameBoard[7] = determineChar(p)
                                    for q in range(0,3,1):
                                        gameBoard[8] = determineChar(q)
                                        if(checkValid(gameBoard)):
                                            states.append(gameBoard[:])
                                            count += 1
    return states

def getStateIndex(board, states):
    for i in range(0, 5478, 1):
        if(board == states[i]):
            return i
    return -1
        

# Randomly choose which computer will go first
def setFirst():
    if(randrange(2) == 0):
        return 'X'
    else:
        return 'O'

#Get the computer's move
def getMove(board, rewards, exp):
    expNum = exp
    possibleMoves = availableMoves(board)
    if(randrange(100) < expNum):
        move = possibleMoves[randrange(len(possibleMoves))]
    else:
        maxReward = -999999
        highIndexes = []
        for index in possibleMoves:
            if rewards[index] > maxReward:
                maxReward = rewards[index]
                highIndexes = [index]
            elif rewards[index] == maxReward:
                highIndexes.append(index)
        move = highIndexes[randrange(len(highIndexes))]
    return move

def getRanMove(board):
    possibleMoves = availableMoves(board)
    move = possibleMoves[randrange(len(possibleMoves))]
    return move

# Returns array of indexes of open spaces
def availableMoves(board):
    available = []
    for i in range(0, len(board), 1):
        if(board[i] == ' '):
            available.append(i)
    return available

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

# Checks to see if there is a winner given a board
def checkWinner(board, char):
    return((board[0] == char and board[1] == char and board[2] == char) or
           (board[3] == char and board[4] == char and board[5] == char) or
           (board[6] == char and board[7] == char and board[8] == char) or
           (board[0] == char and board[3] == char and board[6] == char) or
           (board[1] == char and board[4] == char and board[7] == char) or
           (board[2] == char and board[5] == char and board[8] == char) or
           (board[0] == char and board[4] == char and board[8] == char) or
           (board[2] == char and board[4] == char and board[6] == char))

def determineWinner(state):
    if(checkWinner(state, 'X')):
        return 1
    elif(checkWinner(state, 'O')):
        return 2
    else:
        return 0

def playGame(states, rewards, exp, two):
    # Set the computers' characters
    comp1Char = 'X'
    comp2Char = 'O'

    # Set X to go first
    charTurn = 'X'

    gameOver = False
    gameBoard = [' '] * 9
    usedStates = [0]
    moves = []

    returnArr = []
    
    while(not gameOver):
        if(charTurn == comp1Char):
            # Get the index of the computer's intended move
            moveIndex = getMove(gameBoard, rewards[getStateIndex(gameBoard, states)], exp)
            moves.append(moveIndex)

            # Update the board with the player's intended move
            makeMove(gameBoard, comp1Char, moveIndex)
            #drawBoard(gameBoard)
            #print("State index: ", getStateIndex(gameBoard, states))
            usedStates.append(getStateIndex(gameBoard, states))

            # Make it the other computer's turn
            charTurn = changeTurn(comp1Char, charTurn)

            # Check if the computer has won the game
            if(checkWinner(gameBoard, comp1Char)):
                returnArr.append(usedStates)
                returnArr.append(moves)
                return returnArr
                gameOver = True

        # The computer's turn
        else:
            # Get the index of the computer's intended move
            if(two):
                moveIndex = getMove(gameBoard, rewards[getStateIndex(gameBoard, states)], exp)
            else:
                moveIndex = getRanMove(gameBoard)
            moves.append(moveIndex)

            # Update the board with the player's intended move
            makeMove(gameBoard, comp2Char, moveIndex)
            #drawBoard(gameBoard)
            #print("State index: ", getStateIndex(gameBoard, states))
            usedStates.append(getStateIndex(gameBoard, states))

            # Make it the other computer's turn
            charTurn = changeTurn(comp2Char, charTurn)

            # Check if the computer has won the game
            if(checkWinner(gameBoard, comp2Char)):
                returnArr.append(usedStates)
                returnArr.append(moves)
                return returnArr
                gameOver = True
        
        if(not gameOver):
            if(isBoardFull(gameBoard)):
                returnArr.append(usedStates)
                returnArr.append(moves)
                return returnArr
                gameOver = True

def updateRewards(rewards, indexes, moves, winner):
    for moveNum in range(0, len(moves), 1):
        if(moveNum % 2 == 0):
            if(winner == 1):
                rewards[indexes[moveNum]][moves[moveNum]] += 1
            elif(winner == 2):
                rewards[indexes[moveNum]][moves[moveNum]] -= 1
            else:
                rewards[indexes[moveNum]][moves[moveNum]] += .1
        else:
            if(winner == 1):
                rewards[indexes[moveNum]][moves[moveNum]] -= 1
            elif(winner == 2):
                rewards[indexes[moveNum]][moves[moveNum]] += 1
            else:
                rewards[indexes[moveNum]][moves[moveNum]] += .1
        
                
#================= INTRO AND SETUP =================#
# Welcome message and ask player for character
print("Welcome to Tic-Tac-Toe!")
print("Clash of the Computers")

states = initStates()
rewards = [[0] * 9 for i in range(5478)]

c1Wins = 0
c2Wins = 0
ties = 0

numGames = 50000
for i in range(0, numGames, 1):
    if(i % 1000 == 0):
        print(i, "games played so far")
    twoArrs = playGame(states, rewards, 30, True)
    gameIndexes = twoArrs[0]
    moves = twoArrs[1]

    endIndex = gameIndexes[len(gameIndexes)-1]
    winner = determineWinner(states[endIndex])

    updateRewards(rewards, gameIndexes, moves, winner)
    
    if(winner == 1):
        c1Wins += 1
    elif(winner == 2):
        c2Wins += 1
    else:
        ties += 1
print()
print(rewards[0])
print("Computer 1 won the game ", (c1Wins/numGames)*100, "% of the time")
print("Computer 2 won the game ", (c2Wins/numGames)*100, "% of the time")
print("The computers tied ", (ties/numGames)*100, "% of the time")
print()

'''
numGames2 = 1
for i in range(0, numGames2, 1):
    twoArrs = playGame(states, rewards, 0, True)
    gameIndexes = twoArrs[0]
    moves = twoArrs[1]

    print("Game number: ", i)
    print(gameIndexes)
    print(moves)
    print()

    for index in gameIndexes:
        drawBoard(states[index])
        print(rewards[index])
        print()
'''   
