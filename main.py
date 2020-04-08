from tkinter import *
from tkinter.ttk import *
from gui import *


def main():
    root = Tk()
    gui = GUI(root)
    
    g = Graph()
    g.FillGraphFromLogicSequence("logic_seq.txt", gui.canvas,1, True)
    gui.Draw(g)

    root.update()
    root.mainloop()


if __name__ == '__main__':
    main()
