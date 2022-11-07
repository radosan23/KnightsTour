from kboard import Board


def play(board, pos):
    while True:
        board.calc_matrix()
        board.make_move(pos)
        board.show_poss_moves(pos)
        board.print_board()
        end, win = board.check_end_cond(pos)
        if end:
            break
        pos = board.check_move('Enter your next move: ', 'Invalid move! ', board.x, board.y, pos)
    if win:
        print('What a great tour! Congratulations!')
    else:
        print('No more possible moves!')
        print(f'Your knight visited {len(board.visited)} squares!')


def main():
    size = Board.check_num('Enter your board dimensions: ', 'Invalid dimensions!')
    board = Board(size)
    solution = Board(size)
    position = Board.check_num("Enter the knight's starting position: ", 'Invalid position!', board.x, board.y)
    is_solution = solution.find_solution(position)
    while True:
        menu = input('Do you want to try the puzzle? (y/n): ')
        if menu == 'y' or menu == 'n':
            break
        else:
            print('Invalid input!')
    if not is_solution:
        print('No solution exists!')
    elif menu == 'y':
        play(board, position)
    else:
        print("\nHere's the solution!")
        solution.print_board()


if __name__ == '__main__':
    main()
