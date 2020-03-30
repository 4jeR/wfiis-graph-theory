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
        self.canvas = canvas
    
    # this does exactly what you think it does
    def AddNode(self, node):
        self.nodes.append(node)
    
    # this does exactly what you think it does
    def RemoveNode(self, indx):
        new_nodes = [self.nodes[i] for i in range(len(self.nodes)) if i != indx]
        self.nodes = [n for n in new_nodes]
    
    # for console test printing
    def PrintGraph(self):
        print("Graph has {} nodes and {} edges.".format(Node.count, Edge.count))
        print("Unique connected nodes:")
        for (a,b) in self.connections:
            print("{},{}".format(a.index,b.index))
        
        for edge in self.edges:
            print(edge.index)
        
        
    # prints neighbour list to the console
    def PrintNeighbourList(self):
        print("Neighbour list:")
        for node in self.nodes:
            node.PrintNeighbours()

    # connects two [Node] objects together
    def Connect(self, canvas, node1_idx, node2_idx, Arrow = False):
        # check for (x,y) for both 2 nodes that are going to be connected
        if node1_idx == node2_idx:
            return False

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
        return True
            
    def Draw(self, canvas, trace = False):
        if trace:
            self.DrawCircleTrace(self)
        for e in self.edges:
            e.Draw(canvas)
        for n in self.nodes:
            n.Draw(canvas)

    def NodesCount(self):
        return len(self.nodes)

    def EdgesCount(self):
        return len(self.edges)

        
    def DrawCircleTrace(self, canvas):
        xmin = min([n.x for n in self.nodes])
        ymin = min([n.y for n in self.nodes])
        xmax = max([n.x for n in self.nodes])
        ymax = max([n.y for n in self.nodes])

        self.canvas.create_oval(xmin, ymin, xmax, ymax, dash=(15,20), outline ='red',width=2)


        print("MINs: \nx->{},\ny->{}".format(xmin, ymin))
        print("MAXs: \nx->{},\ny->{}".format(xmax, ymax))

        return
        
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


    def NL_to_NM(self, canvas, filename):
        pass




    def IM_to_NL(self, canvas, filename):
        pass
    
    def NL_to_IM(self, canvas, filename):
        pass




    def NM_to_IM(self, canvas, filename):
        pass

    def IM_to_NM(self, canvas, filename):
        pass
    
   
    @staticmethod
    def RandomizeGraphGNL(canvas, n_nodes, l_edges):
        if l_edges > (n_nodes *(n_nodes-1) / 2):
            print("Enter correct number of nodes and edges. Returning empty graph.")
            return Graph(canvas)

        result_graph = Graph(canvas)
        for i in range(n_nodes):
            xx = random.randint(40, 1160)
            yy = random.randint(40, 860)
            result_graph.AddNode(Node(i+1,xx,yy,35))

        while result_graph.EdgesCount() < l_edges:
            idx1 = random.randint(1, n_nodes)
            idx2 = random.randint(1, n_nodes)
            result_graph.Connect(canvas, idx1, idx2)    

        return result_graph
    