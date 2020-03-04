
import tkinter as tk
from tkinter import W

class Edge:
    count = 0
    def __init__(self,index, node1, node2, arrow = False):
        self.index = index
        self.node1 = node1
        self.node2 = node2
        self.arrow = arrow
        Edge.count += 1

    def Draw(self, canvas):
        if self.arrow:
            canvas.create_line(self.node1.x, self.node1.y,self.node2.x, self.node2.y, dash=(10,20),arrow=tk.LAST)
        else:
            canvas.create_line(self.node1.x, self.node1.y,self.node2.x, self.node2.y,dash=(11,2))
