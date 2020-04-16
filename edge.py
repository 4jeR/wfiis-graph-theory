import tkinter as tk
from tkinter import W
import random


class Edge:
    count = 0

    def __init__(self, index, node1, node2, wage = 0, arrow=False):
        self.index = index
        self.node1 = node1
        self.node2 = node2
        self.arrow = arrow
        self.wage = wage
        Edge.count += 1

    def Draw(self, canvas, wages = False):
        s = (str)(self.wage)
        if self.arrow:
            canvas.create_line(
                self.node1.x, self.node1.y, self.node2.x, self.node2.y, dash=(10, 20), arrow=tk.LAST)
            if wages:
                canvas.create_text( ( self.node1.x + self.node2.x )/2, ( self.node1.y + self.node2.y )/2, fill="darkblue",font="Times 20 italic bold",
                    text=s )
        else:
            canvas.create_line(
                self.node1.x, self.node1.y, self.node2.x, self.node2.y, dash=(11, 2))
            if wages:
                canvas.create_text( ( self.node1.x + self.node2.x )/2, ( self.node1.y + self.node2.y )/2, fill="darkblue",font="Times 20 italic bold",
                    text=s )