
import tkinter as tk
from tkinter import W

class Edge:
    count = 0
    def __init__(self, canvas,index, node1, node2, arrow = False):
        self.canvas = canvas
        self.index = index
        self.node1 = node1
        self.node2 = node2
        self.arrow = arrow
        Edge.count += 1

    def Draw(self):
        if self.arrow:
            self.canvas.create_line(self.node1.x, self.node1.y,self.node2.x, self.node2.y, dash=(10,20),arrow=tk.LAST)
        else:
            self.canvas.create_line(self.node1.x, self.node1.y,self.node2.x, self.node2.y,dash=(11,2))
