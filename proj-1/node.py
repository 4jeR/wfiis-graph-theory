import tkinter as tk
from tkinter import W

class Node:
    count = 0
    def __init__(self, index, x = 0, y = 0, r = 35, neighbours = []):
        self.index = index
        self.x = x
        self.y = y 
        self.r = r
        self.neighbours = [nb for nb in neighbours]
        Node.count += 1
        


    def PrintNeighbours(self):
        print("{}: {}".format(self.index, [n for n in self.neighbours]))

    def Move(self, dx, dy):
        self.x += dx
        self.y += dy

    def Draw(self, canvas): #center coordinates, radius
        x0 = self.x - self.r
        y0 = self.y - self.r
        x1 = self.x + self.r
        y1 = self.y + self.r
        canvas.create_oval(x0, y0, x1, y1, width=3, outline='green',fill='yellow')
        canvas.create_text(self.x-15, self.y, anchor=W,font=("Arial", 16), text=f'{self.index}',fill ='blue')
