from tkinter import *
from tkinter.ttk import *
from gui import *


root = Tk()
gui = GUI(root)
g = Graph(directed=True)

# newGraph = g.FordFulkersonAlgorithm()
# gui.Draw(newGraph,isNetwork=True, isCapacity=True, isFlow=True, numberOfLayers=2)

#Projekt 6-1##########
g.FillGraphFromAL("examples/AL_directed_PR.txt",gui.canvas,inCircle=True,directedGraph=True)
g.PageRankV1(1)
g.PageRankV2()
root.update()
root.mainloop()
