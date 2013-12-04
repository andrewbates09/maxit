#!/usr/bin/python3

#
# Author  : Andrew M Bates (abates09)
#


''' IMPORTS '''

#import curses # for coloured triangulation
import os
import random


# simple cross platform clear screen
def clearScreen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


# print the basic intro message
def prIntro ():
    clearScreen()
    print('Time to play MAXIT!\n'
          'Basic gameplay is as follows:\n'
          ' - you are player 1\n'
          ' - each player alternates turns\n'
          ' - select element in same row or colum as current position\n'
          ' - value of selected element gets added to player total\n'
          ' - selected element becomes next player position\n'
          ' - game ends once all sections on the grid have been selected\n'
          ' - highest total score wins\n')
    return


# pretty print the game board
def printBoard( mboard, msize ):
    print('MAXIT Board Game\n')

    if (mboard==[]):
        print('-- empty board --\n')
        return

    print('   0 ||', end='')
    for col in range(msize):
        print('%4d |' %(col+1), end='')
    print('\n ------', end='')
    for col in range(msize):
        print('------', end='')
    for row in range(msize):
        if (row >= 0):
            print('\n%4d ||' %(row+1), end='')

        for col in range(msize):
            #form = '%' + str(max(msize)) + 's'
            print('%4s |' %str(mboard[row][col]), end='')
    print('\n')
    return


# print the current player stats
def printStats( mplayers, mcurPlayer, mcurPos):
    print('%s' %mplayers[0][0] + '\'s Score: %s'  %mplayers[1][0])
    print('%s' %mplayers[0][1] + '\'s Score: %s'  %mplayers[1][1])
    print('\nCurrent Player: ' + mplayers[0][mcurPlayer])
    print('Current Position: [%d, ' %(mcurPos[0]) + '%d]' %(mcurPos[1]))
    return


# get board size
def getSize():
    is_legit = 0
    while not is_legit:
        try:
            msize = int (input('Enter board size: ' ))
            if msize > 30:
                print('Don\'t be a twat. Pick a smaller size.')
            elif msize > 0:
                is_legit = 1
        except ValueError:
            print('Please enter board size as a number.')
    return msize


# setup board
def setBoard( size ):
    mboard = [[random.randint(-9,15) for col in range(size)] for row in range(size)]
    return mboard


# check for available moves
def checkMoves( mcurPos, mboard, msize ):
    for row in range(msize):
        for col in range(msize):
            print('- checking [%d, %d]', row, col)
            if row == (mcurPos[0]-1):
                print(' - - testing [%d, %d]', row, col)
                if mboard[row][col] != '-':
                    return 1
            elif col == (mcurPos[1]-1):
                print(' - - testing [%d, %d]', row, col)
                if mboard[row][col] != '-':
                    return 1
    return 0


# computer AI and play
# to later be updated for different levels of difficulty
# level 0: random next move
# level 1: highest possible
# level 2: highest possible mapped out combos
def computerAI( mcurPos, mboard, msize ):
    maxNum = -10
    newPos = [0,0]
    aiMoves = [[],[],[]]

    for row in range(msize):
        for col in range(msize):
            if row == (mcurPos[0]-1):
                if mboard[row][col] != '-':
                    if int(mboard[row][col]) > maxNum:
                        maxNum = mboard[row][col]
                        newPos[0] = row+1
                        newPos[1] = col+1
            elif col == (mcurPos[1]-1):
                if mboard[row][col] != '-':
                    if int(mboard[row][col]) > maxNum:
                        maxNum = mboard[row][col]
                        newPos[0] = row+1
                        newPos[1] = col+1
    print('\nComputer chooses: [%s, ' %newPos[0] + '%d]' %newPos[1])
    beepBoop = input('\n(press enter to continue)\n')
    return newPos


# return player's selected choice
def getMove( mcurPlayer, mcurPos, mboard, msize ):
    is_legit = 0
    newPos = [0,0]
    while not is_legit:
        try:
            if mcurPlayer == 1:
                return computerAI(mcurPos, mboard, msize)
            else:
                newPos[0] = int(input('\nSelect row: '))
                newPos[1] = int(input('Select column: '))
                if newPos[0] == mcurPos[0]:
                    if mboard[newPos[0]-1][newPos[1]-1] != '-':
                        is_legit = 1
                elif newPos[1] == mcurPos[1]:
                    if mboard[newPos[0]-1][newPos[1]-1] != '-':
                        is_legit = 1
        except ValueError:
            print('Hint: new [row, column] must be in same row or column from current.')
    return newPos


# simply update players
def updatePlayer( mcurPlayer ):
    return ( mcurPlayer + 1 ) % 2


# init players
# get board size
# build the board
# start the game
def mainMaxit():

    prIntro()

    # init players, scores, boardsize, board, current player, & position
    players = [['Human', 'Computer'], [0, 0]]
    size = getSize()
    board = setBoard( size )
    curPlayer = random.randint(0,1)
    curPos = [random.randint(1, size), random.randint(1, size)]

    gametime = 1

    while gametime:
        clearScreen()
        printBoard(board, size)
        printStats(players, curPlayer, curPos)
        curPos = getMove(curPlayer, curPos, board, size)
        players[1][curPlayer] += board[curPos[0]-1][curPos[1]-1]
        board[curPos[0]-1][curPos[1]-1] = '-'
        curPlayer = updatePlayer(curPlayer)

        # check for possible moves to do.
        gametime  = checkMoves(curPos, board, size)

    # end game stats
    clearScreen()
    printBoard(board, size)
    printStats(players, curPlayer, curPos)
    finalize = input('\nGAME OVER!\n\n(press enter to continue)')
    return
