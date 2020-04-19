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
n6 = g.AddNode(Node(6, 750, 500))

g.Connect(1,2, wage=3)
g.Connect(1,4, wage=2)
g.Connect(2,4, wage=5)
g.Connect(3,5, wage=2)
g.Connect(4,5, wage=2)
g.Connect(3,6, wage=2)
print(g.IsCyclic())

print(g.MinSpanningTreeKruskal())
gui.Draw(g,withWages=True)
root.update()
root.mainloop()
