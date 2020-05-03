from tkinter import *
from tkinter.ttk import *
from gui import *


root = Tk()
gui = GUI(root)
g = Graph()

n1 = g.AddNode(Node(1, 300, 300))
n2 = g.AddNode(Node(2, 500, 300))
n3 = g.AddNode(Node(3, 500, 500))
n4 = g.AddNode(Node(4, 550, 200))
n5 = g.AddNode(Node(5, 750, 400))
n6 = g.AddNode(Node(6, 250, 400))
n7 = g.AddNode(Node(7, 250, 500))

g.Connect(1,7,arrow=True)

g.Connect(2,1,arrow=True)
g.Connect(2,3,arrow=True)
g.Connect(2,6,arrow=True)
g.Connect(2,7,arrow=True)

g.Connect(3,2,arrow=True)
g.Connect(3,6,arrow=True)

g.Connect(4,3,arrow=True)
g.Connect(4,5,arrow=True)

g.Connect(5,3,arrow=True)

g.Connect(6,5,arrow=True)

g.Connect(7,1,arrow=True)

g.PrintAdjacencyList()
g.KosarajuAlgorithm()
gui.Draw(g,weighted=True)

root.update()
root.mainloop()
