from kboard import Board


def main():
    size = Board.check_num('Enter your board dimensions: ', 'Invalid dimensions!')
    board = Board(size)
    position = Board.check_num("Enter the knight's starting position: ", 'Invalid position!', board.x, board.y)
    board.calc_matrix(position)
    board.possible_moves(position)
    print('Here are the possible moves:')
    board.print_board()


if __name__ == '__main__':
    main()
