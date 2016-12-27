from tkinter import Frame, Label, Button, PhotoImage
from app.model import model
import time

class UI:

    def __init__(self, master, dimension):
        self.master = master
        self.dimension = dimension
        self.model = model.Model(self.dimension)
        self.buttons = []

    def run(self):
        self.master.title('Candy Crush')

        self.board = Frame(self.master)

        for r in range(self.dimension):
            row = []
            for c in range(self.dimension):
                command = lambda p=(r,c): self.model.select(p)
                b = Button(self.board, command=command)
                b.grid(row=r, column=c)
                row.append(b)
            self.buttons.append(row)

        self.score_label = Label(self.master, font=("Arial", 16))

        self.board.pack()
        self.score_label.pack()

        self.model.add_observer(self)

    def update(self):

        for row, r in zip(self.buttons, range(self.dimension)):
            for button, c in zip(row, range(self.dimension)):
                path = self.model.get((r,c))
                image = PhotoImage(file=path)
                button.config(background='white', image=image)
                button.image = image

        self.score_label.config(text=str(self.model.score()))

        p = self.model.selected_first()
        if p != None:
            button = self.buttons[p[0]][p[1]]
            button.config(background='red')

        if self.model.no_moves():
            print("there are no remaining moves - game over")