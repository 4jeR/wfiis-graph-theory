import math
import copy

from operator import itemgetter
from helping_funcs import *
from edge import *
from node import *
from collections import *


class Graph:
    def __init__(self, nodes=[], edges=[], connections=[]):
        Node.count=0
        Edge.count=0
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

        print("\nAll edges : {}".format([e.index for e in self.edges]))

        print("\nDegree of nodes".format())

        for node in self.nodes:
            print("D of {} = {}".format(node.index, len(node.neighbours)))

    # prints neighbour Matrix to the console
    def PrintAdjacencyMatrix(self):
        print("\nAdjacency Matrix:")
        for node in self.nodes:
            node.PrintNeighboursInVector()

    # prints neighbour list to the console

    def PrintAdjacencyList(self):
        print("\nAdjacency list:")
        for node in self.nodes:
            node.PrintNeighbours()

    # prints incidence Matrix to the console
    def PrintIncidenceMatrix(self):
        print("\nIncident matrix:")
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
        
        if node1_idx == node2_idx or node1_idx > self.NodesCount() or node2_idx > self.NodesCount():
            return False

        for n in self.nodes:
            if n.index == node1_idx:
                a = n
            elif n.index == node2_idx:
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

    def Disconnect(self, edge):
        try:
            self.edges.remove(edge)
            self.connections.remove((edge.node1, edge.node2))
            edge.node1.removeNeighbour(edge.node2.index)
            edge.node2.removeNeighbour(edge.node1.index)
            Edge.count -= 1
        except Exception as exc:
            print("Exception {} occured when trying to disconnect the edge".format(exc))

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
                self.AddNode(Node(i+1, xx, yy))
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
    def FillGraphFromAL(self, filename, canvas, inCircle=False):
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
                self.AddNode(Node(i+1, xx, yy))

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
    def FillGraphFromAM(self, filename, canvas, inCircle=False):
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
                self.AddNode(Node(i+1, xx, yy))

        for i in range(rows):
            line = str(f.readline()).split(" ")
            for j in range(cols):
                if i == j:
                    continue
                elif line[j] == '1' or line[j] == '1\n':
                    self.Connect(i+1, j+1)

        f.close()

    # 1_3a
    def FillRandomizeGraphGNL(self, canvas, n_nodes, l_edges,  inCircle=False):
        if inCircle:
            for i in range(n_nodes):
                xnext = canvas.winfo_width()/2.0 - 255 * math.cos(i * 2*math.pi / (n_nodes))
                ynext = canvas.winfo_height()/2.0 - 255 * math.sin(i * 2*math.pi / (n_nodes))
                self.AddNode(Node(i+1, xnext, ynext))
        else:
            for i in range(n_nodes):
                xx = random.randint(30, canvas.winfo_width() - 30)
                yy = random.randint(30, canvas.winfo_height() - 30)
                self.AddNode(Node(i+1, xx, yy))

        while self.EdgesCount() < l_edges:
            idx1 = random.randint(1, n_nodes)
            idx2 = random.randint(1, n_nodes)
            self.Connect(idx1, idx2)

    # 1_3b
    def FillRandomizeGraphGNP(self, canvas, n_nodes, prob,  inCircle=False):
        if inCircle:
            for i in range(n_nodes):
                xnext = canvas.winfo_width()/2.0 - 255 * math.cos(i * 2*math.pi / (n_nodes))
                ynext = canvas.winfo_height()/2.0 - 255 * math.sin(i * 2*math.pi / (n_nodes))
                self.AddNode(Node(i+1, xnext, ynext))
        else:
            for i in range(n_nodes):
                xx = random.randint(30, canvas.winfo_width() - 30)
                yy = random.randint(30, canvas.winfo_height() - 30)
                self.AddNode(Node(i+1, xx, yy))

        for node in self.nodes:
            for i in range(n_nodes):
                rand_prob = random.uniform(0, 1)
                if rand_prob <= prob:
                    self.Connect(node.index, i+1)

    ########## PROJECT 2 PARTS ##########

    def FillFromGraphicSequence(self, filename, canvas, line=1, inCircle=False):
        seq, pls = self.ParseGraphicSequence(filename, line)

        if pls:
            # construct nodes
            if inCircle:
                for i in range(len(seq)):
                    xnext = canvas.winfo_width()/2.0 - 255 * math.cos(i * 2*math.pi / (len(seq)))
                    ynext = canvas.winfo_height()/2.0 - 255 * math.sin(i * 2*math.pi / (len(seq)))
                    self.AddNode(Node(i+1, xnext, ynext))
            else:
                for i in range(len(seq)):
                    xx = random.randint(30, canvas.winfo_width() - 30)
                    yy = random.randint(30, canvas.winfo_height() - 30)
                    self.AddNode(Node(i+1, xx, yy))

            # make connections based on sequence
            seq_copy = seq.copy()
            
            # seq_copy.sort(reverse=True)
            idx = 1
            while sum(seq_copy.values()) > 0:
                print("suma = {}, idx = {}".format(sum(seq_copy.values()), idx))
                list_idx = [idx]
                while seq_copy[idx-1] > 0:
                    rand_idx = RandomizeIndex(idx, len(seq_copy), list_idx, seq_copy)
                    list_idx.append(rand_idx)
                    if self.Connect(idx, rand_idx):
                        seq_copy[idx-1] -= 1
                        seq_copy[rand_idx-1] -= 1
                idx += 1
                if idx + 1 >= len(seq_copy):
                    if True not in seq_copy:
                        break
                    else:
                        seq_copy = seq.copy()
                        idx = 1
                
            return True
        else:
            print("[FillFromGraphicSequence] Couldn't construct graph from this sequence.")
            return False

    def ParseGraphicSequence(self, filename, line=1):
        f = open(filename, "r")
        seq = list()
        for i in range(line):
            seq = list(map(int, f.readline().split(" ")))

        seq.sort(reverse=True)
        seq_result = dict(enumerate(seq.copy()))
        print(seq_result)


        while(True):
            if sum(seq) <= 0:
                f.close()
                return seq_result, True
            if seq[0] < 0 or seq[0] >= len(seq) or sum(1 for el in seq if el < 0) > 0:
                f.close()
                return seq_result, False
            for i in range(1, seq[0] + 1):
                seq[i] -= 1
            seq[0] = 0
            seq.sort(reverse=True)

    def EdgesRandomization(self, count):
        if Node.count*(Node.count-1)/2 == Edge.count:
            return False
        else:
            i = 0
            while i < count:
                Samples = random.sample(self.edges, 2)
                if AreUnique(Samples):
                    a = Samples[0].node1.index
                    b = Samples[0].node2.index
                    c = Samples[1].node1.index
                    d = Samples[1].node2.index
                    if self.Connect(a, c):
                        if(self.Connect(d, b)):
                            self.Disconnect(Samples[0])
                            self.Disconnect(Samples[1])
                            i += 1
                        else:
                            self.Disconnect(Samples[0])
                            i += 1
                    elif self.Connect(b, c):
                        if(self.Connect(d, a)):
                            self.Disconnect(Samples[0])
                            self.Disconnect(Samples[1])
                            i += 1
                        else:
                            self.Disconnect(Samples[0])
                            i += 1
                    else:
                        i += 1
            return True

    # 2_5
    def FillKReguralGraph(self, canvas, n_nodes, degree, inCircle=False):
        if (n_nodes * degree) % 2 != 0:
            return False

        if not 0 <= degree < n_nodes:
            return False

        seq = [degree for d in range(n_nodes)]
        filename = "examples/GS_ex3.txt"
        with open(filename, "w") as f:
            f.write(' '.join([str(x) for x in seq]))
        f.close()

        if (self.FillFromGraphicSequence(filename, canvas, 1, inCircle)):
            return True
        else:
            return False
    
    # 2_3
    def CommonComponentsToString(self, canvas, comp):
        ComponentsList = ""
        for i in range(0, len(comp)):
            if (comp[i] != 0):
                ComponentsList += "\n"
                nr = comp[i]
                ComponentsList += "" + (str)(nr) + ") "
                randomColor = "#"+("%06x" % random.randint(500000, 16777215))
                for i in range(len(comp)):
                    if comp[i] == nr:
                        self.nodes[i].color = randomColor
                        ComponentsList += (str)(self.nodes[i].index) + " "
                        comp[i] = 0
        tab = ComponentsList.split("\n")
        longest_string = max(tab, key=len)

        return ComponentsList + "\nThe longest common component has numer " + longest_string[0]

    def Components_R(self, nr, n, comp):
        for nb in n.neighbours:
            if comp[nb-1] == -1:
                comp[nb-1] = nr
                self.Components_R(nr, NodeFromIndex(self, nb), comp)
            else:
                continue

    def FillComponents(self, filename, canvas, inCircle=True):
        self.FillGraphFromAM(filename, canvas, inCircle)
        nr = 0
        comp = []
        for i in range(len(self.nodes)):
            comp.append(-1)
        for n in self.nodes:
            if comp[n.index-1] == -1:
                nr += 1
                comp[n.index-1] = nr
                self.Components_R(nr, n, comp)
        return self.CommonComponentsToString(canvas, comp)

    def GetCommonComponents(self):
        """
        Gets common components of current graph.
        :return: List of common componets of the graph.
        """
        nr = 0
        comp = []
        for i in range(len(self.nodes)):
            comp.append(-1)
        for n in self.nodes:
            if comp[n.index-1] == -1:
                nr += 1
                comp[n.index-1] = nr
                self.Components_R(nr, n, comp)
        return self.GenerateCommonComponents(comp)

    def GenerateCommonComponents(self, comp):
        """
        Creates list of a common components of currently generated graph.
        :param comp: Found components.
        :return: List of common componets of the graph.
        """
        ComponentsList = ""
        for i in range(0, len(comp)):
            if (comp[i] != 0):
                ComponentsList += "\n"
                nr = comp[i]
                ComponentsList += "" + (str)(nr) + ") "
                for i in range(len(comp)):
                    if comp[i] == nr:
                        ComponentsList += (str)(self.nodes[i].index) + " "
                        comp[i] = 0
        return ComponentsList.split("\n")

    def DisconnectByIndexes(self, node1_i, node2_i):
        """
        Removes edge that at the first end has node with index node1_i and at second edge has node with index node2_i.
        :return: None
        """
        for edge in self.edges:
            if (edge.node1.index == node1_i and edge.node2.index == node2_i) or (edge.node1.index == node2_i and edge.node2.index == node1_i):
                self.Disconnect(edge) 

    def CheckIfConnectionIsABridge(self, node1_i, node2_i):
        """
        Check if edge connecting node with index node1_i and node with index node2_i is a bridge, that is, checks if number 
        of common connected components after removing the edge increases.
        :return: True of False
        """

        is_bridge = False;

        num_of_commmon_components_before_disconecting = len(self.GetCommonComponents())

        self.DisconnectByIndexes(node1_i, node2_i)

        num_of_commmon_components_after_disconecting = len(self.GetCommonComponents())

        if num_of_commmon_components_after_disconecting > num_of_commmon_components_before_disconecting:
            is_bridge = True
        self.Connect(node1_i, node2_i)

        return is_bridge

    def ResetGraph(self):
        """
        Sets graph data to origin form.
        :return: Nothing.
        """
        self.nodes = []
        self.edges = []
        self.connections = []

    def IsEulerGraph(self):
        """
        Checks if this Graph is euler graph, that is, if every node degree is even number.
        :return: True of False.
        """

        for node in self.nodes:
            if ((len(node.neighbours) % 2) == 1) or (len(node.neighbours) == 0):
                return False
        return True

    def FindEulerCycle(self):
        """
        If current graph is Eulers graph, Euler Cycle of the graph is found.

        :return: String containing euler cycle found in randomly generated graph, e.g:
                 [1 - 2 - 3 - 1 - 4 - 2 - 5 - 1 - 7 - 4 - 3 - 6 - 2 - 8 - 1], where numbers are the nodes labels.
        """

        if self.IsEulerGraph():
            nodes_copy = [n for n in self.nodes]
            edges_copy = [e for e in self.edges]
            connections_copy = [(a, b) for (a, b) in self.connections]
            euler_cycle = list()

            starting_node_index = random.randint(1, len(self.nodes))
            starting_node = self.nodes[starting_node_index - 1]
            euler_cycle.append(starting_node.index)

            current_node = starting_node

            self.PrintGraph()

            while len(self.connections) != 0:
                for i, neighbour in enumerate(current_node.neighbours):
                    if (not self.CheckIfConnectionIsABridge(neighbour, current_node.index)) or (i == (len(current_node.neighbours) - 1)):
                        euler_cycle.append(neighbour)
                        self.DisconnectByIndexes(neighbour, current_node.index)
                        current_node = self.nodes[neighbour - 1]
                        break

            self.nodes = [n for n in nodes_copy]
            self.edges = [e for e in edges_copy]
            self.connections = [(a, b) for (a, b) in connections_copy]

        euler_cycle_readable_format = "["
        for node in euler_cycle:
            euler_cycle_readable_format += " {} -".format(node)
        euler_cycle_readable_format = euler_cycle_readable_format[:-1]     
        euler_cycle_readable_format += "]"

        return euler_cycle_readable_format


    # 2_4
    def GetEulersCycleFromRandomEulerGraph(self, canvas, num_of_nodes=0, in_circle=False):
        """
        Generates random Euler Graph, then finds Eulers Cycle of the graph.

        :param num_of_nodes: Number of nodes of a graph to be randomly generated.
        :param canvas: Canvas on which the graph is drawn.
        :param in_circle: Tells if nodes coordinates should eventually create a circle shape
        :return: String containing euler cycle found in randomly generated graph, e.g:
                 [1 - 2 - 3 - 1 - 4 - 2 - 5 - 1 - 7 - 4 - 3 - 6 - 2 - 8 - 1], where numbers are the nodes labels.
        """

        if num_of_nodes == 0:
            num_of_nodes = random.randint(5, 15)

        while True:
            self.ResetGraph()
            self.FillRandomizeGraphGNP(canvas, num_of_nodes, 0.5, inCircle=in_circle)
            if self.IsEulerGraph():
                break

        return self.FindEulerCycle()


        def checkIfIsHamiltonGraph(self, canvas, filepath, in_circle=False):

            if filepath == None:
                self.FillRandomizeGraphGNP(canvas, 0, 0.5, inCircle=in_circle)








