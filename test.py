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

g.Connect(1,2,arrow=True,weight=6)
g.Connect(1,3,arrow=True,weight=3)
g.Connect(1,5,arrow=True,weight=-1)

g.Connect(2,1,arrow=True,weight=10)
g.Connect(2,3,arrow=True,weight=-5)
g.Connect(2,4,arrow=True,weight=-4)
g.Connect(2,5,arrow=True,weight=4)
g.Connect(2,7,arrow=True,weight=4)



g.Connect(3,6,arrow=True,weight=2)

g.Connect(4,2,arrow=True,weight=5)
g.Connect(4,7,arrow=True,weight=9)

g.Connect(5,7,arrow=True,weight=-4)

g.Connect(6,2,arrow=True,weight=9)

g.Connect(7,6,arrow=True,weight=4)



print(g.JohnsonAlgorithm())


root.update()
root.mainloop()
