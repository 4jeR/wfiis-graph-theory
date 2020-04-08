import math

from helping_funcs import *
from edge import *
from node import *


class Graph:
    def __init__(self, nodes=[], edges=[], connections=[]):
        Node.count = 0
        Edge.count = 0
        self.nodes = [n for n in nodes]
        self.edges = [e for e in edges]
        self.connections = [(a, b) for (a, b) in connections]

    # this does exactly what you think it does
    def AddNode(self, node):
        self.nodes.append(node)

    # this does exactly what you think it does
    def RemoveNode(self, indx):
        new_nodes = [self.nodes[i]
                     for i in range(len(self.nodes)) if i != indx]
        self.nodes = [n for n in new_nodes]

    # HELP
    def PrintGraph(self):
        print("Graph has {} nodes and {} edges.".format(Node.count, Edge.count))
        print("Unique connected nodes:")
        for (a, b) in self.connections:
            print("{},{}".format(a.index, b.index))

        for edge in self.edges:
            print(edge.index)

    # prints neighbour Matrix to the console
    def PrintNeighbourMatrix(self):
        print("\nMacierz sasiedztwa:")
        for node in self.nodes:
            node.PrintNeighboursInVector()

    # prints neighbour list to the console

    def PrintNeighbourList(self):
        print("\nLista sasiedztwa:")
        for node in self.nodes:
            node.PrintNeighbours()

    # prints incidence Matrix to the console
    def PrintIncidenceMatrix(self):
        print("\nMacierz incydencji:")
        Matrix = [[0 for i in range(len(self.edges))]
                  for y in range(len(self.nodes))]
        for edge in self.edges:
            Matrix[edge.node1.index-1][edge.index-1] = 1
            Matrix[edge.node2.index-1][edge.index-1] = 1
        for row in Matrix:
            for val in row:
                print(val, " ", end='')
            print()

    # connects two [Node] objects together
    def Connect(self, node1_idx, node2_idx, Arrow=False):
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

        if a.index != b.index and (a, b) not in self.connections and (b, a) not in self.connections:
            self.edges.append(
                Edge(len(self.edges)+1, a, b, Arrow))
            self.connections.append((a, b))
            if b.index not in a.neighbours:
                a.neighbours.append(b.index)
            if a.index not in b.neighbours:
                b.neighbours.append(a.index)
            return True
        else:
            return False
    
    def DisConnect(self,edge):
        try:            
            self.edges.remove(edge)
            self.connections.remove((edge.node1,edge.node2))
            Edge.count-=1
        except:
            print("Graph doesn't have the Edge")

    def NodesCount(self):
        return len(self.nodes)

    def EdgesCount(self):
        return len(self.edges)

    # 1_1a
    def FillGraphFromIM(self, filename, canvas, inCircle=False):
        matrix, rows, cols = FileToMatrix(filename)
        # put vertexes on the circle
        if inCircle:
            for i in range(rows):
                xnext = canvas.winfo_width()/2.0 - 255 * math.cos(i * 2*math.pi / (rows))
                ynext = canvas.winfo_height()/2.0 - 255 * math.sin(i * 2*math.pi / (rows))
                self.AddNode(Node(i+1, xnext, ynext))
        else:
            for i in range(rows):
                xx = random.randint(30, canvas.winfo_width() - 30)
                yy = random.randint(30, canvas.winfo_height() - 30)
                self.AddNode(Node(i+1, xx, yy, 20))
        # find neighbours
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    for k in range(rows):
                        if i != k and matrix[k][j] == 1:
                            self.nodes[i].neighbours.append(k+1)
                            break
                        else:
                            continue

        # find edges
        for j in range(cols):
            counter = 0
            for i in range(rows):
                if matrix[i][j] == 1 and counter == 0:
                    node1 = i+1
                    counter += 1
                elif matrix[i][j] == 1 and counter == 1:
                    node2 = i+1
                    counter += 1
                    break
            self.Connect(node1, node2)

    # 1_1b
    def FillGraphFromNL(self, filename, canvas, inCircle=False):
        vert_count = 0
        with open(filename, 'r') as f:
            for line in f:
                vert_count += 1

        # put nodes
        if inCircle:
            for i in range(vert_count):
                xnext = canvas.winfo_width()/2.0 - 255 * math.cos(i * 2*math.pi / (vert_count))
                ynext = canvas.winfo_height()/2.0 - 255 * math.sin(i * 2*math.pi / (vert_count))
                self.AddNode(Node(i+1, xnext, ynext))
        else:
            for i in range(vert_count):
                xx = random.randint(30, canvas.winfo_width() - 30)
                yy = random.randint(30, canvas.winfo_height() - 30)
                self.AddNode(Node(i+1, xx, yy, 20))

        # find neighbour and connect
        with open(filename, 'r') as f:
            line = f.readline()
            i = 0
            while line:
                line = line.rstrip('\n')
                vect = line.split(" ")
                for j in range(len(vect)):
                    self.Connect(i+1, int(vect[j]))
                line = f.readline()
                i += 1

    # 1_1c
    def FillGraphFromNM(self, filename, canvas, inCircle=False):
        f, rows, cols = GetFileRowsCols(self, filename)

        if inCircle:
            for i in range(rows):
                xnext = canvas.winfo_width()/2.0 - 255 * math.cos(i * 2*math.pi / (rows))
                ynext = canvas.winfo_height()/2.0 - 255 * math.sin(i * 2*math.pi / (rows))
                self.AddNode(Node(i+1, xnext, ynext))
        else:
            for i in range(rows):
                xx = random.randint(30, canvas.winfo_width() - 30)
                yy = random.randint(30, canvas.winfo_height() - 30)
                self.AddNode(Node(i+1, xx, yy, 20))

        for i in range(rows):
            line = str(f.readline()).split(" ")
            for j in range(cols):
                if i == j:
                    continue
                elif line[j] == '1' or line[j] == '1\n':
                    self.Connect(i+1, j+1)

        f.close()

    # 1_3a
    def FillRandomizeGraphGNL(self, canvas, n_nodes, l_edges):
        for i in range(n_nodes):
            xx = random.randint(30, canvas.winfo_width() - 30)
            yy = random.randint(30, canvas.winfo_height() - 30)
            self.AddNode(Node(i+1, xx, yy, 20))

        while self.EdgesCount() < l_edges:
            idx1 = random.randint(1, n_nodes)
            idx2 = random.randint(1, n_nodes)
            self.Connect(idx1, idx2)


                

    # 1_3b
    def FillRandomizeGraphGNP(self, canvas, n_nodes, prob):
        for i in range(n_nodes):
            xx = random.randint(30, canvas.winfo_width() - 30)
            yy = random.randint(30, canvas.winfo_height() - 30)
            self.AddNode(Node(i+1, xx, yy, 20))

        for node in self.nodes:
            for i in range(n_nodes):
                rand_prob = random.uniform(0, 1)
                if rand_prob <= prob:
                    self.Connect(node.index, i+1)
    
    def EdgesRandomization(self,count):
        i = 0 
        while i < count:
            Samples = random.sample(self.edges,2)
            if AreUnique(Samples):
                a = Samples[0].node1.index
                b = Samples[0].node2.index
                c = Samples[1].node1.index
                d = Samples[1].node2.index
                if self.Connect(a,c):
                    if(self.Connect(d,b)):
                        self.DisConnect(Samples[0])
                        self.DisConnect(Samples[1])
                        i+=1
                    else:
                        self.DisConnect(Samples[0])
                        i+=1
                elif self.Connect(b,c):
                    if(self.Connect(d,a)):
                        self.DisConnect(Samples[0])
                        self.DisConnect(Samples[1])
                        i+=1
                    else:
                        self.DisConnect(Samples[0])
                        i+=1
                else:
                    i+=1




    ########## PROJECT 2 PARTS ##########

    def FillGraphFromLogicSequence(self, filename, canvas, line =1, inCircle=False):
        seq, pls = self.ParseLogicSequence(filename, line)
        
        if pls:
            # construct nodes
            if inCircle:
                for i in range(len(seq)):
                    xnext = 600 - 255 * math.cos(i * 2*math.pi / (len(seq)))
                    ynext = 400 - 255 * math.sin(i * 2*math.pi / (len(seq)))
                    self.AddNode(Node(i+1, xnext, ynext))
            else:
                for i in range(len(seq)):
                    xx = random.randint(100, 1100)
                    yy = random.randint(150, 650)
                    self.AddNode(Node(i+1, xx, yy, 35))

            # make connections based on sequence
            idx = 1
            while sum(seq) > 0:
                for i in range(1, seq[idx-1]+1):
                    self.Connect(idx, idx + i)
                    seq[idx-1] -= 1
                    seq[idx+i-1] -= 1
                idx += 1

        else:
            print("Couldn't construct graph from this sequence.")

                    
               
                
                    




    def ParseLogicSequence(self, filename, line = 1):
        f = open(filename,"r")
        seq = list()
        for i in range(line):
            seq = list(map(int, f.readline().split(" ")))
        
        seq_result = seq.copy()
        seq.sort(reverse=True)



        
        while(True):
            if int(True) not in seq:
                f.close()
                return seq_result, True
            if seq[0] < 0 or seq[0] >= len(seq) or sum(1 for el in seq if el < 0) > 0:
                f.close()
                return seq_result, False
            for i in range(1, seq[0] + 1):
                seq[i] -= 1
            seq[0] = 0
            seq.sort(reverse=True)

        
