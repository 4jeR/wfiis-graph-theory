from tkinter import *
from tkinter.ttk import *
from gui import *


root = Tk()
gui = GUI(root)
g = Graph()
# g.FillKReguralGraph(gui.canvas, 5, 2)
root.update()
root.mainloop()
