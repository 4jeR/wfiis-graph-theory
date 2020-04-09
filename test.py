from tkinter import *
from tkinter.ttk import *
from gui import *


root = Tk()
gui = GUI(root)
g = Graph()
g.FillComponents("examples/FCC_neighbour_matrix.txt", gui.canvas, True)
root.update()
root.mainloop()