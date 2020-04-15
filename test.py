from tkinter import *
from tkinter.ttk import *
from gui import *


root = Tk()
gui = GUI(root)
g = Graph()
g.FillFromGraphicSequence("examples/GS_ex1.txt", gui.canvas)
gui.Draw(g)
root.update()
root.mainloop()
