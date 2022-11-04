from kboard import Board


def main():
    size = Board.check_num('Enter your board dimensions: ', 'Invalid dimensions!')
    board = Board(size)
    position = Board.check_num("Enter the knight's starting position: ", 'Invalid position!', board.x, board.y)
    board.calc_matrix()
    board.make_move(position)
    board.print_board()
    visited_count = 1
    end = board.check_end_cond(position, visited_count)
    while not end:
        position = board.check_move('Enter your next move: ', 'Invalid move!', board.x, board.y, position)
        board.calc_matrix()
        board.make_move(position)
        board.print_board()
        visited_count += 1
        end = board.check_end_cond(position, visited_count)


if __name__ == '__main__':
    main()
