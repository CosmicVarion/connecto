class Selector:

    def __init__(self, board):
        self.board = board
        self.clear_selections()

    def select(self, p):
        if self.selected_first == None:
            self.selected_first = p
        else:
            self.selected_second = p
            if (self.adjacent(self.selected_first, self.selected_second)):
                self.board.game_exchange(self.selected_first, self.selected_second)
            else:
                print("invalid move - the tiles are not adjacent")
            self.clear_selections()

    def adjacent(self, p, q):
        return abs(p[0] - q[0]) + abs(p[1] - q[1]) == 1

    def clear_selections(self):
        self.selected_first = None
        self.selected_second = None