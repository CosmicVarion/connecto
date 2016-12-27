import sys
import os
from tkinter import Tk

def main(args):
    sys.path.append(os.getcwd())
    from app.view import ui
    root = Tk()
    if len(args) == 1:
        candy_crush = ui.UI(root, 5)
    else:
        candy_crush = ui.UI(root, int(args[1]))
    candy_crush.run()
    root.mainloop()

if __name__ == '__main__': main(sys.argv)
