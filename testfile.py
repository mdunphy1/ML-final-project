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

def determineChar(index):
    if(index == 0):
        return ' '
    elif(index == 1):
        return 'X'
    else:
        return 'O'

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

def numSpacesFilled(board):
    count = 0
    for i in range(0, len(board), 1):
        if(board[i] == 'X'):
            count += 1
        elif(board[i] == 'O'):
            count += 1
    return count

def checkWinner(board, char):
    return((board[0] == char and board[1] == char and board[2] == char) or
           (board[3] == char and board[4] == char and board[5] == char) or
           (board[6] == char and board[7] == char and board[8] == char) or
           (board[0] == char and board[3] == char and board[6] == char) or
           (board[1] == char and board[4] == char and board[7] == char) or
           (board[2] == char and board[5] == char and board[8] == char) or
           (board[0] == char and board[4] == char and board[8] == char) or
           (board[2] == char and board[4] == char and board[6] == char))


states = []

count = 0
counts = [0] * 10
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
                                        num = numSpacesFilled(gameBoard)
                                        counts[num] += 1

for i in range(0, len(counts), 1):
    print("Number of combinations with ", i, "spaces filled: ", counts[i])
print(count)

drawBoard(states[1000])
'''
for i in range(0, 100, 1):
    drawBoard(states[i])
'''


'''
def drawBoard(board):
    print('   |')
    print(' ' + board[0] + ' | ' + board[1])
    print('   |')
    print('-------')
    print('   |')
    print(' ' + board[2] + ' | ' + board[3])
    print('   |')

def determineChar(index):
    if(index == 0):
        return ' '
    elif(index == 1):
        return 'X'
    else:
        return 'O'

def checkValid(board):
    xCount = 0
    oCount = 0
    for i in range(0, len(board), 1):
        if(board[i] == 'X'):
            xCount += 1
        elif(board[i] == 'O'):
            oCount += 1

    if((xCount - oCount) <= 1 and (xCount - oCount) >= -1):
        return True
    else:
        return False

count = 0
gameBoard = [' '] * 4
for i in range(0,3,1):
    gameBoard[0] = determineChar(i)
    for j in range(0,3,1):
        gameBoard[1] = determineChar(j)
        for k in range(0,3,1):
            gameBoard[2] = determineChar(k)
            for l in range(0,3,1):
                gameBoard[3] = determineChar(l)
                if(checkValid(gameBoard)):
                    count += 1
                    print("Game board #", count)
                    drawBoard(gameBoard)
                else:
                    print()
                    print()
                    print("NOT LEGAL!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    drawBoard(gameBoard)
                    print()
                    print()

print(count)
'''
