from app.model import board
from app.model import selector


class Model:

    def __init__(self, dimension):
        self.board = board.Board(dimension)
        self.selector = selector.Selector(self.board)

    def add_observer(self, ui):
        self.observer = ui
        self.observer.update()

    def select(self, p):
        self.selector.select(p)
        self.observer.update()

    def score(self):
        return self.board.score

    def no_moves(self):
        return self.board.has_no_moves()

    def get(self, p):
        return self.board.get(p)

    def selected_first(self):
        return self.selector.selected_first
