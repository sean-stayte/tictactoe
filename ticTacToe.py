# Most of this program is from p113 in Automate The Boring Stuff With Python by Al Sweigart
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# I added the if/elif statements that determine whether the game has been won
turn = 'X'
for i in range(9):
    if theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] and theBoard['top-L'] != ' ':
        print(theBoard['top-L'] + ' wins!')
    elif theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R'] and theBoard['mid-L'] != ' ':
        print(theBoard['mid-L'] + ' wins!')
    elif theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R'] and theBoard['low-L'] != ' ':
        print(theBoard['low-L'] + ' wins!')
    elif theBoard['top-L'] == theBoard['mid-L'] == theBoard['low-L'] and theBoard['top-L'] != ' ':
        print(theBoard['top-L'] + ' wins!')
    elif theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M'] and theBoard['top-M'] != ' ':
        print(theBoard['top-M'] + ' wins!')
    elif theBoard['top-R'] == theBoard['mid-R'] == theBoard['low-R'] and theBoard['top-R'] != ' ':
        print(theBoard['top-R'] + ' wins!')
    elif theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] and theBoard['top-L'] != ' ':
        print(theBoard['top-L'] + ' wins!')
    elif theBoard['top-R'] == theBoard['mid-M'] == theBoard['low-L'] and theBoard['top-R'] != ' ':
        print(theBoard['top-L'] + ' wins!')
    else:
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
printBoard(theBoard)

