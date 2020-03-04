import tkinter as tk
import math
import random
from tkinter import W

from helping_funcs import *

class Graph:
    def __init__(self, canvas, nodes = [], edges = []):
        self.nodes = [n for n in nodes]
        self.edges = [e for e in edges]
        self.n = len(nodes) if nodes != None else 0
        self.canvas = canvas
    
    def AddNode(self, node):
        self.nodes.append(node)
        self.n += 1 
    
    def RemoveNode(self, indx):
        new_nodes = [self.nodes[i] for i in range(len(self.nodes)) if i != indx]
        self.nodes = [n for n in new_nodes]
    
    def PrintGraph(self):
        print("Lista sąsiedztwa:")
        for node in self.nodes:
            node.PrintNeighbours()
        print("Krawedzie:")
        for edge in self.edges:
            print(edge.index)
        

        
    #todo
    def Connect(self, canvas, node1_idx, node2_idx, Arrow = False):
        #check for (x,y) for both 2 nodes that are going to be connected
        if node1_idx == node2_idx:
            print("Cant connect self to self!")
            return
        elif node1_idx in self.edges or node2_idx in self.edges:
            print("Already connected edges!")
            return
        else:
            for n in self.nodes:
                if n.index == node1_idx:
                    x1 = n.x
                    y1 = n.y
                    a = n
                elif n.index == node2_idx:
                    x2 = n.x
                    y2 = n.y
                    b = n

            self.edges.append(Edge(len(self.edges)+1, a, b, Arrow))      

            
    def Draw(self, canvas):
        for n in self.nodes:
            n.Draw(canvas)

        for e in self.edges:
            e.Draw(canvas)

        
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

        f.close()

class Node:
    def __init__(self, index, x = 0, y = 0, r = 35, neighbours = []):
        self.index = index
        self.x = x
        self.y = y 
        self.r = r
        self.neighbours = [nb for nb in neighbours]


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
        canvas.create_oval(x0, y0, x1, y1)
        canvas.create_text(self.x-5, self.y, anchor=W, font="Arial",text="{}".format(self.index))


class Edge:
    count = 0
    def __init__(self,index, node1, node2, arrow = False):
        self.index = index
        self.node1 = node1
        self.node2 = node2
        self.arrow = arrow
        

    def Draw(self, canvas):
        if self.arrow:
            canvas.create_line(self.node1.x, self.node1.y,self.node2.x, self.node2.y, arrow=tk.LAST)
        else:
            canvas.create_line(self.node1.x, self.node1.y,self.node2.x, self.node2.y)
