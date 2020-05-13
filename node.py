import random
import tkinter as tk
from tkinter import W


class Node:
    count = 0

    def __init__(self, index, x=0, y=0, r=20, neighbours=[], color = "#"+("%06x" % random.randint(500000, 16777215)), inLayer = -1):
        self.index = index
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.neighbours = [nb for nb in neighbours]
        self.inLayer = inLayer
        Node.count += 1

    def removeNeighbour(self, neighbour):
        self.neighbours.remove(neighbour)

    def resetNodeCount():
        Node.count = 0

    def PrintNeighbours(self, connections=None):
        if connections != None:
            print("{}: {}".format(self.index, [n for n in self.neighbours if ((self.index, n) in connections)]))
        else: 
            print("{}: {}".format(self.index, [n for n in self.neighbours]))

    def PrintNeighboursInVector(self):
        vect = []
        for i in range(0, self.count):
            vect.append(0)

        for i in range(len(self.neighbours)):
            vect[int(self.neighbours[i])-1] = 1
        print(*vect)

    def GetNeighboursInVector(self):
        vect = []
        for i in range(0, self.count):
            vect.append(0)

        for i in range(len(self.neighbours)):
            vect[int(self.neighbours[i])-1] = 1
        return vect

    def Move(self, dx, dy):
        self.x += dx
        self.y += dy

    def Draw(self, canvas, color, maxLayer = -1):  # center coordinates, radius
        x0 = self.x - self.r
        y0 = self.y - self.r
        x1 = self.x + self.r
        y1 = self.y + self.r
        if self.inLayer == 0:
            canvas.create_oval(x0, y0, x1, y1, width=5,
                           outline='red', fill=self.color)
            canvas.create_text(self.x-9, self.y, anchor=W,
                           font=("Arial", 16), text=f'S', fill='red')    
        elif (self.inLayer > 0) and (self.inLayer == (maxLayer+1)):
            canvas.create_oval(x0, y0, x1, y1, width=5,
                            outline='red', fill=self.color)
            canvas.create_text(self.x-9, self.y, anchor=W,
                            font=("Arial", 16), text=f'T', fill='red')
        else:
            canvas.create_oval(x0, y0, x1, y1, width=3,
                           outline='green', fill=self.color)
            canvas.create_text(self.x-9, self.y, anchor=W,
                           font=("Arial", 16), text=f'{self.index}', fill='black')

    def Degree(self):
        return len(self.neighbours)
