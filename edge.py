import tkinter as tk
from tkinter import W
import random
import math

class Edge:
    count = 0

    def __init__(self, index, node1, node2, arrow=False, weight = 0):
        self.index = index
        self.node1 = node1
        self.node2 = node2
        self.arrow = arrow
        self.weight = weight
        Edge.count += 1

    def resetEdgesCount():
        Edge.count = 0

    def Draw(self, canvas, wages = False):
        s = (str)(self.weight)
        if self.arrow:
            xLength = abs(self.node1.x - self.node2.x)
            yLength = abs(self.node1.y - self.node2.y)
            edgeLength = abs(math.sqrt(xLength**2 + yLength**2))
            cutXLineRate = xLength / edgeLength 
            cutYLineRate = yLength / edgeLength
            cutLineBy = 7
            canvas.create_line(
                self.node1.x, self.node1.y, (self.node2.x - ((self.node2.r / 2) + cutLineBy * cutXLineRate)) if (self.node2.x > self.node1.x) else (self.node2.x + ((self.node2.r / 2) + cutLineBy * cutXLineRate)),
                (self.node2.y - ((self.node2.r / 2) + cutLineBy * cutYLineRate)) if (self.node2.y > self.node1.y) else (self.node2.y + ((self.node2.r / 2) + cutLineBy * cutYLineRate)), arrow=tk.LAST, dash=(11, 2))
            if wages:
                separateWagesBy = 1.5
                separateYWageBy = separateWagesBy / abs((cutXLineRate - 1.1)  )
                separateXWageBy = separateWagesBy / abs((cutYLineRate - 1.1))
                canvas.create_text( (((( self.node1.x + self.node2.x ) / 2) - separateXWageBy) if self.node1.x < self.node2.x else ((( self.node1.x + self.node2.x ) / 2) + separateXWageBy)), 
                    (((( self.node1.y + self.node2.y ) / 2) - separateYWageBy) if self.node1.y < self.node2.y else ((( self.node1.y + self.node2.y ) / 2) + separateYWageBy)), fill="darkblue",font="Times 20 italic bold", text=s )
        else:
            canvas.create_line(
                self.node1.x, self.node1.y, self.node2.x, self.node2.y, dash=(11, 2))
            if wages:
                canvas.create_text( ( self.node1.x + self.node2.x ) / 2, ( self.node1.y + self.node2.y ) / 2, fill="darkblue",font="Times 20 italic bold",
                    text=s )