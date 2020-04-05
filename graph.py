import math
import random

from helping_funcs import *
from edge import *
from node import *

class Graph:
    def __init__(self, canvas, nodes = [], edges = [], connections = []):
        self.canvas = canvas
        self.nodes = [n for n in nodes]
        self.edges = [e for e in edges]
        self.connections = [(a,b) for (a,b) in connections]
    
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
    
    # prints neighbour Matrix to the console
    def PrintNeighbourMatrix(self):
        for node in self.nodes:
            node.PrintNeighboursInVector()
        
        
    # prints neighbour list to the console
    def PrintNeighbourList(self):
        print("Neighbour list:")
        for node in self.nodes:
            node.PrintNeighbours()

    def PrintIncidenceMatrix(self):
        Matrix = [[0 for i in range(len(self.edges))] for y in range(len(self.nodes))] 
        for edge in self.edges:
            Matrix[edge.node1.index-1][edge.index-1]=1
            Matrix[edge.node2.index-1][edge.index-1]=1
        for row in Matrix:
            for val in row:
                print(val," ",end='')
            print()
        

    # connects two [Node] objects together
    def Connect(self, node1_idx, node2_idx, Arrow = False):
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
            self.edges.append(Edge(self.canvas, len(self.edges)+1, a, b, Arrow))
            self.connections.append((a, b))      
        return True
            
    def Draw(self, trace = False):
        if trace:
            self.DrawCircleTrace(self)
        for e in self.edges:
            e.Draw()
        for n in self.nodes:
            n.Draw()

    def NodesCount(self):
        return len(self.nodes)

    def EdgesCount(self):
        return len(self.edges)

        
    def DrawCircleTrace(self):
        xmin = min([n.x for n in self.nodes])
        ymin = min([n.y for n in self.nodes])
        xmax = max([n.x for n in self.nodes])
        ymax = max([n.y for n in self.nodes])

        self.canvas.create_oval(xmin, ymin, xmax, ymax, dash=(15,20), outline ='red',width=2)
        
    def FillGraphFromIM(self,filename, inCircle = False):
        matrix,rows,cols = FileToMatrix(filename) 
        #put vertexes on the circle
        if inCircle:
            for i in range(rows):  
                xnext = 400 - 255 *math.cos(i * 2*math.pi / (rows))
                ynext = 350 - 255 *math.sin(i * 2*math.pi / (rows))
                self.AddNode(Node(self.canvas,i+1,xnext,ynext))
            self.DrawCircleTrace()
        else:
            for i in range(rows):
                xx = random.randint(40, 1160)
                yy = random.randint(40, 860)
                self.AddNode(Node(self.canvas, i+1,xx,yy,35))
        #find neighbours
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    for k in range(rows):
                        if i!=k and matrix[k][j] == 1:
                            self.nodes[i].neighbours.append(k+1)
                            break
                        else:
                            continue
                
        #find edges
        for j in range(cols):
            counter = 0
            for i in range(rows):
                if matrix[i][j]== 1 and counter == 0:
                    node1 = i+1
                    counter+=1
                elif matrix[i][j]== 1 and counter ==1:
                    node2 = i+1
                    counter+=1
                    break
            self.Connect(node1,node2)
                
    def FillGraphFromNL(self,filename, inCircle = False):
        vert_count = 0
        with open(filename, 'r') as f:
            for line in f:
                vert_count += 1

        # put nodes
        if inCircle:
            for i in range(vert_count):  
                xnext = 400 - 255 *math.cos(i * 2*math.pi / (vert_count))
                ynext = 350 - 255 *math.sin(i * 2*math.pi / (vert_count))
                self.AddNode(Node(self.canvas,i+1,xnext,ynext))
            self.DrawCircleTrace()
        else:
            for i in range(vert_count):
                xx = random.randint(40, 1160)
                yy = random.randint(40, 860)
                self.AddNode(Node(self.canvas, i+1,xx,yy,35))

       
        

        #find neighbour and connect
        with open(filename, 'r') as f:
            line = f.readline()
            i = 0
            while line:
                line= line.rstrip('\n')
                vect = line.split(" ")
                for j in range(len(vect)):
                    self.nodes[i].neighbours.append(vect[j])
                    self.Connect(i+1,int(vect[j]))
                line = f.readline()
                i+=1
        
    def FillGraphFromNM(self, filename, inCircle = False):
        f,rows,cols = GetFileRowsCols(self, filename)

        if inCircle:
            for i in range(rows):  
                xnext = 400 - 255 *math.cos(i * 2*math.pi / (rows))
                ynext = 350 - 255 *math.sin(i * 2*math.pi / (rows))
                self.AddNode(Node(self.canvas,i+1,xnext,ynext))
            self.DrawCircleTrace()
        else:
            for i in range(rows):
                xx = random.randint(40, 1160)
                yy = random.randint(40, 860)
                self.AddNode(Node(self.canvas, i+1,xx,yy,35))
        
        for i in range(rows):                   
            line = str(f.readline()).split(" ")
            for j in range(cols):
                if i == j:
                    continue
                elif line[j] == '1' or line[j] == '1\n':
                    self.nodes[j].neighbours.append(i+1)
                    self.Connect(i+1, j+1)

        f.close()  

    # 1_1  
    def NM_to_NL(self, filename, inCircle = False):
        self.FillGraphFromNM(filename, inCircle)
        self.PrintNeighbourList()

    def NL_to_NM(self, filename, inCircle = False):
        self.FillGraphFromNL(filename, inCircle)
        self.PrintNeighbourMatrix()
        
    def IM_to_NL(self, filename, inCircle = False):
        self.FillGraphFromIM(filename, inCircle)
        self.PrintNeighbourList()
        
    def NL_to_IM(self, filename, inCircle = False):
        self.FillGraphFromNL(filename, inCircle)
        self.PrintIncidenceMatrix()

    def NM_to_IM(self, filename, inCircle = False):
        self.FillGraphFromNM(filename, inCircle)
        self.PrintIncidenceMatrix()

    def IM_to_NM(self, filename, inCircle = False):
        self.FillGraphFromIM(filename, inCircle)
        self.PrintNeighbourMatrix()

    
    # 1_3a
    @staticmethod
    def RandomizeGraphGNL(canvas, n_nodes, l_edges):
        if l_edges > (n_nodes *(n_nodes-1) / 2):
            print("Enter correct number of nodes and edges. Returning empty graph.")
            return Graph(canvas)

        result_graph = Graph(canvas)
        for i in range(n_nodes):
            xx = random.randint(40, 1160)
            yy = random.randint(40, 860)
            result_graph.AddNode(Node(canvas,i+1,xx,yy,35))

        while result_graph.EdgesCount() < l_edges:
            idx1 = random.randint(1, n_nodes)
            idx2 = random.randint(1, n_nodes)
            result_graph.Connect(canvas, idx1, idx2)    

        return result_graph

    # 1_3b
    @staticmethod
    def RandomizeGraphGNP(canvas, n_nodes, prob):
        result_graph = Graph(canvas)
        for i in range(n_nodes):
            xx = random.randint(40, 1160)
            yy = random.randint(40, 860)
            result_graph.AddNode(Node(canvas, i+1,xx,yy,35))

        for node in result_graph.nodes:
            for i in range(n_nodes):
                rand_prob = random.uniform(0, 1)
                if rand_prob <= prob:                   
                    result_graph.Connect(node.index, i+1)  

        return result_graph
    