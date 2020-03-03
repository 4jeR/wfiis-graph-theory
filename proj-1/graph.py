import tkinter as tk
import math
import random
from tkinter import W

from helping_funcs import *

class Graph:
    def __init__(self, canvas, nodes = []):
        self.nodes = [n for n in nodes]
        self.n = len(nodes) if nodes != None else 0
        self.canvas = canvas
    
    # bez rysowania, 
    def AddNode(self, node):
        self.nodes.append(node)
        self.n += 1 
    
    # bez rysowania 
    def RemoveNode(self, indx):
        new_nodes = [self.nodes[i] for i in range(len(self.nodes)) if i != indx]
        self.nodes = [n for n in new_nodes]
    
    #do testow do konsoli
    def PrintGraph(self):
        i = 0
        for node in self.nodes:
            node.Print(i)
            i += 1
        print("Size of graph: {}.".format(self.n))
        
    #todo
    def Connect(self, canvas, node1_idx, node2_idx, Arrow = False):
        #check for (x,y) for both 2 nodes that are going to be connected
        for n in self.nodes:
            if n.index == node1_idx:
                x1 = n.x
                y1 = n.y

            elif n.index == node2_idx:
                x2 = n.x
                y2 = n.y

        if Arrow:
            canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)
        else:
            canvas.create_line(x1, y1, x2, y2)
            
    # dla kazdego Node woła jego metode Draw
    def Draw(self, canvas):
        for n in self.nodes:
            n.Draw(canvas)


    def NM_to_NL(self, canvas, filename):
        f,rows,cols = GetFileRowsCols(self, filename)

        for i in range(rows):  
            self.AddNode(Node(i+1, 500 + 355 * math.sin(i) , 400 + 355 * math.cos(i)))
    
        for i in range(rows):                   
            line = str(f.readline()).split(" ")
            for j in range(cols):
                if i == j:
                    continue
                elif line[j] == '1' or line[j] == '1\n':
                    self.nodes[j].neighbours.append(i+1)
                    self.Connect(canvas, i+1, j+1)



# klasa reprezentujaca wierzcholek, 
class Node:
    def __init__(self, index, x = 0, y = 0, r = 35, neighbours = []):
        self.index = index
        self.x = x
        self.y = y 
        self.r = r
        self.neighbours = [nb for nb in neighbours]


    #do testow wypisywania na konsole
    def Print(self):
        print("{}: {}".format(self.index, [n for n in self.neighbours]))

    def Move(self, dx, dy):
        self.x += dx
        self.y += dy

    # metoda ktora rysuje obecny wierzcholek na glownym canvasie
    def Draw(self, canvas): #center coordinates, radius
        x0 = self.x - self.r
        y0 = self.y - self.r
        x1 = self.x + self.r
        y1 = self.y + self.r
        canvas.create_oval(x0, y0, x1, y1)
        canvas.create_text(self.x-5, self.y, anchor=W, font="Arial",text="{}".format(self.index))
        self.Print()


        