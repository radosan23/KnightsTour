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

    def print_board(self):
        lph = len(str(self.y))
        print(' ' * lph + '-' * (3 + self.x * (self.c_size + 1)))
        for j in range(self.y, 0, -1):
            row = ' '.join(self.matrix[j - 1])
            print(' ' * (lph - len(str(j))) + str(j) + '| ' + row + ' |')
        print(' ' * lph + '-' * (3 + self.x * (self.c_size + 1)))
        print(' ' * (lph + 2) + ' '.join(' ' * (self.c_size - len(str(x))) + str(x) for x in range(1, self.x + 1)))
