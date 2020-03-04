import math
import random

from helping_funcs import *
from edge import *
from node import *

class Graph:
    def __init__(self, canvas, nodes = [], edges = [], connections = []):
        self.nodes = [n for n in nodes]
        self.edges = [e for e in edges]
        self.connections = [(a,b) for (a,b) in connections]
        self.n = len(nodes) if nodes != None else 0
        self.canvas = canvas
    
    def AddNode(self, node):
        self.nodes.append(node)
        self.n += 1 
    
    def RemoveNode(self, indx):
        new_nodes = [self.nodes[i] for i in range(len(self.nodes)) if i != indx]
        self.nodes = [n for n in new_nodes]
    
    def PrintGraph(self):
        print("Graph has {} nodes and {} edges.".format(Node.count, Edge.count))
        print("Unique connected nodes:")
        for (a,b) in self.connections:
            print("{},{}".format(a.index,b.index))
        
        print("Neighbour list:")
        for node in self.nodes:
            node.PrintNeighbours()
        
        for edge in self.edges:
            print(edge.index)



    def Connect(self, canvas, node1_idx, node2_idx, Arrow = False):
        # check for (x,y) for both 2 nodes that are going to be connected
        for n in self.nodes:
            if n.index == node1_idx:
                x1 = n.x
                y1 = n.y
                a = n
            elif n.index == node2_idx:
                x2 = n.x
                y2 = n.y
                b = n
        
        # prevent from adding already connected nodes
        if (a,b) not in self.connections and (b,a) not in self.connections:
            self.edges.append(Edge(len(self.edges)+1, a, b, Arrow))
            self.connections.append((a, b))      

            
    def Draw(self, canvas):
        for n in self.nodes:
            n.Draw(canvas)

        for e in self.edges:
            e.Draw(canvas)

        
    def NM_to_NL(self, canvas, filename):
        f,rows,cols = GetFileRowsCols(self, filename)

        for i in range(rows):  
            xnext = 400 - 355 *math.cos(i * 2*math.pi / (rows))
            ynext = 450 - 355 *math.sin(i * 2*math.pi / (rows))

            self.AddNode(Node(i+1,xnext,ynext))
    
        for i in range(rows):                   
            line = str(f.readline()).split(" ")
            for j in range(cols):
                if i == j:
                    continue
                elif line[j] == '1' or line[j] == '1\n':
                    self.nodes[j].neighbours.append(i+1)
                    self.Connect(canvas, i+1, j+1)

        f.close()

