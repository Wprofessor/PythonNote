theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(Board):
    print(Board['top-L'] + '|' + Board['top-M'] + '|' + Board['top-R'])
    print('-+-+-')
    print(Board['mid-L'] + '|' + Board['mid-M'] + '|' + Board['mid-R'])
    print('-+-+-')
    print(Board['low-L'] + '|' + Board['low-M'] + '|' + Board['low-R'])


turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for' + turn + '. Move on witch space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
