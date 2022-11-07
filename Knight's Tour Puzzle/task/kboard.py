class Board:
    def __init__(self, xy):
        self.x = xy[0]
        self.y = xy[1]
        self.c_size = len(str(self.x * self.y))
        self.matrix = None
        self.visited = []
        self.calc_matrix()

    @staticmethod
    def check_num(msg, wrong, lim_x=999, lim_y=999):
        while True:
            try:
                num = [int(x) for x in input(msg).split()]
                if len(num) == 2 and 0 < num[0] <= lim_x and 0 < num[1] <= lim_y:
                    return num
                print(wrong, end='')
            except ValueError:
                print(wrong, end='')

    def check_move(self, msg, wrong, lim_x, lim_y, pos):
        while True:
            move = self.check_num(msg, wrong, lim_x, lim_y)
            if move in self.get_poss_moves(pos):
                return move
            else:
                print(wrong, end='')

    def calc_matrix(self):
        vis = ' ' * (self.c_size - 1) + '*'
        empty = '_' * self.c_size
        self.matrix = [[vis if ([i, j] in self.visited) else empty
                        for i in range(1, self.x + 1)] for j in range(1, self.y + 1)]

    def make_move(self, pos, symbol='X'):
        space = ' ' * (self.c_size - len(symbol))
        self.matrix[pos[1] - 1][pos[0] - 1] = space + symbol
        self.visited.append(pos)

    def get_poss_moves(self, pos):
        moves = [[-2, 1], [-2, -1], [2, 1], [2, -1], [-1, 2], [-1, -2], [1, 2], [1, -2]]
        poss_moves = []
        for n in moves:
            move = [sum(x) for x in zip(pos, n)]
            if 0 < move[0] <= self.x and 0 < move[1] <= self.y and move not in self.visited:
                poss_moves.append(move)
        return poss_moves

    def show_poss_moves(self, pos):
        space = ' ' * (self.c_size - 1)
        for n in self.get_poss_moves(pos):
            self.matrix[n[1] - 1][n[0] - 1] = space + str(len(self.get_poss_moves(n)))

    def find_solution(self, pos, count=1):
        self.make_move(pos, str(count))
        end, win = self.check_end_cond(pos)
        if win:
            return True
        else:
            for move in sorted(self.get_poss_moves(pos), key=lambda x: len(self.get_poss_moves(x))):
                if self.find_solution(move, count + 1):
                    return True
            self.visited.remove(pos)
        return False

    def print_board(self):
        lph = len(str(self.y))
        print(' ' * lph + '-' * (3 + self.x * (self.c_size + 1)))
        for j in range(self.y, 0, -1):
            row = ' '.join(self.matrix[j - 1])
            print(' ' * (lph - len(str(j))) + str(j) + '| ' + row + ' |')
        print(' ' * lph + '-' * (3 + self.x * (self.c_size + 1)))
        print(' ' * (lph + 2) +
              ' '.join(' ' * (self.c_size - len(str(x))) + str(x) for x in range(1, self.x + 1)) + '\n')

    def check_end_cond(self, pos):
        if len(self.visited) == self.x * self.y:
            return True, True
        elif not self.get_poss_moves(pos):
            return True, False
        else:
            return False, False
