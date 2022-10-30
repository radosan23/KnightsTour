def check_pos(pos):
    try:
        pos = [int(x) for x in pos.split()]
        pos = [x for x in pos if 0 < x < 9]
        if len(pos) == 2:
            return pos
        print('Invalid dimensions!')
    except ValueError:
        print('Invalid dimensions!')


def calc_matrix(pos):
    b = [['X' if [i, j] == pos else '_' for i in range(1, 9)] for j in range(1, 9)]
    return b


def print_board(b):
    print(' ' + '-' * 19)
    for i in range(8, 0, -1):
        row = ''
        for j in range(1, 9):
            row += b[i-1][j-1] + ' '
        print(str(i) + '| ' + row + '|')
    print(' ' + '-' * 19)
    print(' ' * 3 + '1 2 3 4 5 6 7 8')


position = check_pos(input("Enter the knight's starting position: "))
if position is not None:
    board = calc_matrix(position)
    print_board(board)
