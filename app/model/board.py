from random import randint
import os

class Board:

    IMAGES = 5

    def __init__(self, dimension):
        self.dimension = dimension
        self.score = 0
        self.match_points = None
        self.image_paths()
        self.setup_board()

    def image_paths(self):
        self.image_paths = []
        for i in range(self.IMAGES):
            path = os.getcwd() + "/Images/Tile-"+str(i)+".gif"
            self.image_paths.append(path)

    def setup_board(self):
        self.board = []
        for r in range(self.dimension):
            row = []
            for c in range(self.dimension):
                row.append("")
            self.board.append(row)

        while self.invalid_configuration():
            for r in range(self.dimension):
                for c in range(self.dimension):
                    self.board[r][c] = self.image_paths[randint(0, self.IMAGES - 1)]

    def invalid_configuration(self):
        return self.has_no_moves() or self.has_matches()

    def has_no_moves(self):
        # horizontal
        for r in range(self.dimension):
            for c in range(self.dimension - 1):
                if self.valid_exchange((r,c), (r,c+1)):
                    return False
        # vertical
        for c in range(self.dimension):
            for r in range(self.dimension - 1):
                if self.valid_exchange((r,c), (r+1,c)):
                    return False
        return True

    def valid_exchange(self, p, q):
        self.exchange(p, q)
        ret_val = False
        if self.has_matches():
            ret_val = True
        self.exchange(p, q)
        return ret_val

    def has_matches(self):
        return len(self.matches()) > 0

    def matches(self):
        master = set()
        # horizontal
        for row, r in zip(self.board, range(self.dimension)):
            match = set()
            len_match = 1
            for c in range(self.dimension-1):
                if row[c] is row[c+1]:
                    len_match = len_match + 1
                    match.add((r,c))
                    match.add((r,c+1))
                else:
                    if len_match >= 3:
                        master = master.union(match)
                    match = set()
                    len_match = 1
            if len_match >= 3:
                master = master.union(match)

        #vertical
        for c in range(self.dimension):
            col = [row[c] for row in self.board]
            match = set()
            len_match = 1
            for r in range(self.dimension-1):
                if col[r] is col[r+1]:
                    len_match = len_match + 1
                    match.add((r, c))
                    match.add((r+1, c))
                else:
                    if len_match >= 3:
                        master = master.union(match)
                    match = set()
                    len_match = 1
            if len_match >= 3:
                master = master.union(match)

        return master

    def exchange(self, p, q):
        path_p = self.board[p[0]][p[1]]
        path_q = self.board[q[0]][q[1]]

        self.board[p[0]][p[1]] = path_q
        self.board[q[0]][q[1]] = path_p

    def game_exchange(self, p, q):
        self.exchange(p, q)
        matches = self.matches()
        length = len(matches)
        if length == 0:
            self.exchange(p, q)
            print("invalid move attempted")
        else:
            print("valid move!")
            self.score = self.score + length
            self.remove_matches(matches)

    def remove_matches(self, matches):
        for p in matches:
            self.board[p[0]][p[1]] = ""

        for c in range(self.dimension):
            for r in range(self.dimension):
                if self.board[r][c] is "":
                    temp_r = r
                    while temp_r > 0:
                        if self.board[temp_r-1][c] is not "":
                            self.exchange((temp_r,c),(temp_r-1,c))
                        temp_r = temp_r - 1

        for c in range(self.dimension):
            for r in range(self.dimension):
                p = self.board[r][c]
                if p is "":
                    self.board[r][c] = self.image_paths[randint(0, self.IMAGES - 1)]

        points = self.matches()
        if len(points) > 0:
            self.remove_matches(points)

    def get(self, p):
        return self.board[p[0]][p[1]]
