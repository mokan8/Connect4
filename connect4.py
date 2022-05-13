# connect 4
# original board is 6x7 row x col
# board stores pieces as strings
#from asyncore import ExitNow
#from random import randint
import random
import os
from statistics import mode

# board is a list of strings
board = ['-' for x in range(43)]

# to create new board when game ends


def newBoard():
    global board
    board = ['-' for x in range(43)]

# 1-7 firstrow
#8-14, 15-21, 22-28, 29-35
# 36-42 last row

# gets copy of board so as to not alter original board


def copyBoard():
    tempBoard = board.copy()
    return tempBoard

# prins the board in a psuedo-graphic way


def printBoard(board):
    print(board[36] + board[37] + board[38] +
          board[39] + board[40] + board[41] + board[42])
    print(board[29] + board[30] + board[31] +
          board[32] + board[33] + board[34] + board[35])
    print(board[22] + board[23] + board[24] +
          board[25] + board[26] + board[27] + board[28])
    print(board[15] + board[16] + board[17] +
          board[18] + board[19] + board[20] + board[21])
    print(board[8] + board[9] + board[10] +
          board[11] + board[12] + board[13] + board[14])
    print(board[1] + board[2] + board[3] +
          board[4] + board[5] + board[6] + board[7])

# checks if column is full


def colFull(col):
    if board[col + 35] != '-':
        return False
    else:
        return True

# inserts piece into specified column


def insertPiece(board, piece, col):
    state = True
    while state:
        if board[col] == '-':
            board[col] = piece
            state = False
        else:
            col += 7

# checks if board is full, returns false if board is not full


def isBoardFull(board):
    if board.count('-') > 0:
        return False
    else:
        return True

# checks if computer can insert a piece to get three in a row


def threeCheck(piece):
    for i in range(1, 7):
        favorable = []
        temp = copyBoard()
        insertPiece(temp, 'O', i)
        for i in range(1, 22):
            if temp[i] == temp[i+7] == temp[i+14] == piece:
                favorable.append(i)

            rowCheck = [1, 2, 3, 4, 8, 9, 10, 11, 15, 16, 17, 18,
                        22, 23, 24, 25, 29, 30, 31, 32, 36, 37, 38, 39]
        for i in rowCheck:
            if temp[i] == temp[i+1] == temp[i+2] == piece:
                favorable.append(i)

    # list for right diagonals
        rd = [1, 2, 3, 4, 8, 9, 10, 11, 15, 16, 17, 18]
        for i in rd:
            if temp[i] == temp[i+8] == temp[i+16] == piece:
                favorable.append(i)
    # list for left diagonals
        ld = [7, 6, 5, 4, 14, 13, 12, 11, 21, 20, 19, 18]
        for i in ld:
            if temp[i] == temp[i+6] == temp[i+12] == piece:
                favorable.append(i)
    if len(favorable) > 0:
        return mode(favorable)
    else:
        return 0

# checks for winner


def isWinner(board, piece):
    # column check
    for i in range(1, 22):
        if board[i] == board[i+7] == board[i+14] == board[i+21] == piece:
            return True

    rowCheck = [1, 2, 3, 4, 8, 9, 10, 11, 15, 16, 17, 18,
                22, 23, 24, 25, 29, 30, 31, 32, 36, 37, 38, 39]
    for i in rowCheck:
        if board[i] == board[i+1] == board[i+2] == board[i+3] == piece:
            return True

    # list for right diagonals
    rd = [1, 2, 3, 4, 8, 9, 10, 11, 15, 16, 17, 18]
    for i in rd:
        if board[i] == board[i+8] == board[i+16] == board[i+24] == piece:
            return True
    # list for left diagonals
    ld = [7, 6, 5, 4, 14, 13, 12, 11, 21, 20, 19, 18]
    for i in ld:
        if board[i] == board[i+6] == board[i+12] == board[i+18] == piece:
            return True
    return False


def playerMove():
    run = True
    while run:
        move = input('Select a column to drop an X (1-7)')
        try:
            move = int(move)
            if move > 0 and move < 8:
                if colFull(move):
                    run = False
                    insertPiece(board, 'X', move)
                    if isWinner(board, 'X') == True:
                        print('X wins!')
                        restartGame()
                        return
                else:
                    print('Column occupied')
            else:
                print('Insert valid number')
        except:
            print('Insert valid number')


def restartGame():
    run = True
    while run == True:
        flip = input('Restart gamne?(y/n): ')
        if flip == 'y':
            board = newBoard()
            main()
        if flip == 'n':
            print('Thanks for playing!')
            os._exit(os.EX_OK)
        else:
            print('Enter y or n')

# Random AI


def compMove():
    run = True
    while run == True:
        move = random.randint(1, 7)
        if colFull(move):
            run = False
            insertPiece(board, 'O', move)
            if isWinner(board, 'O') == True:
                print('O wins!')
                restartGame()
        printBoard(board)

# smart AI


def compThink():
    # copy board to check winner??
    # check for winning move
    for i in range(1, 7):
        tempBoard = copyBoard()
        if colFull(i):
            insertPiece(tempBoard, 'O', i)
        if isWinner(tempBoard, 'O'):
            insertPiece(board, 'O', i)
            printBoard(board)
            print('O wins!')
            restartGame()
    # block player win
    for i in range(1, 7):
        tempBoard = copyBoard()
        insertPiece(tempBoard, 'X', i)
        if isWinner(tempBoard, 'X'):
            insertPiece(board, 'O', i)
            printBoard(board)
            return
            # stop loop
            # stop next turn
    # connect3
    if threeCheck('O') != 0:
        insertPiece(board, 'O', threeCheck('O'))
        printBoard(board)
        return

    # random
    else:
        compMove()
        return


def main():
    print('Welcome to Connect-4')
    diff = input('Select diffculty(1:Easy,2:Hard): ')
    try:
        diff = int(diff)
        if diff == 1 or diff == 2:
            level = int(diff)
    except:
        print('Insert 1 for easy, 2 for hard')

    printBoard(board)

    if level == 1:
        while not(isBoardFull(board)):
            playerMove()
            compMove()
    else:
        while not(isBoardFull(board)):
            playerMove()
            compThink()


main()
# two different AIs,
#random(easy), hard
