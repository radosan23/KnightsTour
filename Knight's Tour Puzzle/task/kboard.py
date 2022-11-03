class Board:
    def __init__(self, xy):
        self.x = xy[0]
        self.y = xy[1]
        self.c_size = len(str(self.x * self.y))
        self.matrix = None
        self.calc_matrix([0, 0])

    @staticmethod
    def check_num(msg, wrong, lim_x=999, lim_y=999):
        while True:
            try:
                num = [int(x) for x in input(msg).split()]
                if len(num) == 2 and 0 < num[0] <= lim_x and 0 < num[1] <= lim_y:
                    return num
                print(wrong)
            except ValueError:
                print(wrong)

    def calc_matrix(self, pos):
        marked = ' ' * (self.c_size - 1) + 'X'
        empty = '_' * self.c_size
        self.matrix = [[marked if [i, j] == pos else empty for i in range(1, self.x + 1)] for j in range(1, self.y + 1)]

    def possible_moves(self, pos):
        space = ' ' * (self.c_size - 1)
        for n in self.get_poss_moves(pos):
            self.matrix[n[1] - 1][n[0] - 1] = space + str(len(self.get_poss_moves(n)) - 1)

    def get_poss_moves(self, pos):
        moves = [[-2, 1], [-2, -1], [2, 1], [2, -1], [-1, 2], [-1, -2], [1, 2], [1, -2]]
        poss_moves = []
        for n in moves:
            move = [sum(x) for x in zip(pos, n)]
            if 0 < move[0] <= self.x and 0 < move[1] <= self.y:
                poss_moves.append(move)
        return poss_moves

    def print_board(self):
        lph = len(str(self.y))
        print(' ' * lph + '-' * (3 + self.x * (self.c_size + 1)))
        for j in range(self.y, 0, -1):
            row = ' '.join(self.matrix[j - 1])
            print(' ' * (lph - len(str(j))) + str(j) + '| ' + row + ' |')
        print(' ' * lph + '-' * (3 + self.x * (self.c_size + 1)))
        print(' ' * (lph + 2) + ' '.join(' ' * (self.c_size - len(str(x))) + str(x) for x in range(1, self.x + 1)))
