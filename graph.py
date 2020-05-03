import math
import copy

from operator import itemgetter
from helping_funcs import *
from edge import *
from node import *
from collections import *
from tkinter import messagebox


class Graph:
    def __init__(self, nodes=[], edges=[], connections=[]):
        """ 
        Constructor for Graph objects.
        :return: nothing
        """
        Node.count=0
        Edge.count=0
        self.nodes = [n for n in nodes]
        self.edges = [e for e in edges]
        self.connections = [(a, b) for (a, b) in connections]

    def AddNode(self, node):
        """ 
        Adds Node object to the graph. Returns added node
        :return: Node
        """
        self.nodes.append(node)
        return node

    def RemoveNode(self, indx):
        """ IT NEEDS FIXES """
        new_nodes = [self.nodes[i]
                     for i in range(len(self.nodes)) if i != indx]
        self.nodes = [n for n in new_nodes]

    def PrintGraph(self):
        """
        Prints graph info and stats to the console.
        :return: nothing
        """
        print("Graph has {} nodes and {} edges.".format(Node.count, Edge.count))
        print("Unique connected nodes:")
        for (a, b) in self.connections:
            print("{},{}".format(a.index, b.index))

        print(f"\nAll edges : {[e.index for e in self.edges]}")

        print("\nDegree of nodes")

        for node in self.nodes:
            print(f"D of {node.index} = {len(node.neighbours)}")

    def PrintAdjacencyMatrix(self):
        """
        Prints graph represented by Adjacency Matrix form to the console.
        :return: nothing
        """
        print("\nAdjacency Matrix:")
        for node in self.nodes:
            node.PrintNeighboursInVector()

    def PrintAdjacencyList(self):
        """
        Prints graph represented by Adjacency List form to the console.
        :return: nothing
        """
        print("\nAdjacency list:")

        for node in self.nodes:
            node.PrintNeighbours()


    def PrintIncidenceMatrix(self):
        """
        Prints graph represented by Incidence Matrix form to the console.
        :return: nothing
        """
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


    def Connect(self, node1_idx, node2_idx, arrow=False, weight = 0):
        """
        Constructs edge between two nodes of given indexes. If they were succesfully connected
        then it returns True, otherwise returns False.
        :return: bool
        """
        if node1_idx == node2_idx or node1_idx > self.NodesCount() or node2_idx > self.NodesCount():
            return False

        for n in self.nodes:
            if n.index == node1_idx:
                a = n
            elif n.index == node2_idx:
                b = n

        # prevent from adding already connected nodes
        if ((a.index != b.index and (a, b) not in self.connections and (b, a) not in self.connections) or 
            (a.index != b.index and ((a,b) not in self.connections or (b, a) not in self.connections) and arrow)):
            self.edges.append(
                Edge(len(self.edges)+1, a, b, arrow, weight))
            self.connections.append((a, b))
            if arrow:
                a.neighbours.append(b.index)
                return True
            else:
                if b.index not in a.neighbours:
                    a.neighbours.append(b.index)
                if a.index not in b.neighbours:
                    b.neighbours.append(a.index)
                return True
        else:
            return False


    def Disconnect(self, node1_idx, node2_idx):
        """
        Removes edge that at the first end has node with index node1_idx and at second edge has node with index node2_idx.
        :return: None
        """
        for edge in self.edges:
            if (edge.node1.index == node1_idx and edge.node2.index == node2_idx) or (edge.node1.index == node2_idx and edge.node2.index == node1_idx):
                self.DisconnectByEdge(edge) 

    def ConnectByEdge(self, edge, arrow=False):
        """
        Constructs edge between two nodes of given indexes. If they were succesfully connected
        then it returns True, otherwise returns False.
        :return: bool
        """
        return self.Connect(edge.node1.index, edge.node2.index,arrow, edge.weight)

    def DisconnectByEdge(self, edge):
        """
        Removes edge from graph and updates status of all properties.
        :return: nothing
        """
        try:
            self.edges.remove(edge)
            self.connections.remove((edge.node1, edge.node2))
            edge.node1.removeNeighbour(edge.node2.index)
            edge.node2.removeNeighbour(edge.node1.index)
            Edge.count -= 1
        except Exception as exc:
            print("Exception {} occured when trying to disconnect the edge".format(exc))

    def AreConnected(self, node1_idx, node2_idx):
        """
        Checks if two nodes with given indexes are already connected with each other.
        :return: bool
        """
        for n in self.nodes:
            if n.index == node1_idx:
                a = n
            elif n.index == node2_idx:
                b = n

        return ((b.index in a.neighbours) and (a.index in b.neighbours))


    def NodesCount(self):
        """
        Returns count of nodes in graph.
        :return: int
        """
        return len(self.nodes)

    def EdgesCount(self):
        """
        Returns count of edges in graph.
        :return: int
        """
        return len(self.edges)

    # 1_1a
    def FillGraphFromIM(self, filename, canvas, inCircle=False, directedGraph=False):
        """
        Constructs graph from Incidence Matrix.
        :return: nothing
        """
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
                print("[{}][{}] = {}".format(i, j, matrix[i][j]))
                if matrix[i][j] == -1:
                    node2 = i+1
                    print("Node2 = -1")
                    counter += 1
                elif matrix[i][j] == 1 and counter == 0 and not directedGraph:
                    node1 = i+1
                    counter += 1
                elif matrix[i][j] == 1 and counter == 1 and not directedGraph:
                    node2 = i+1
                    counter += 1
                    break
                elif matrix[i][j] == 1 and directedGraph:
                    print("Node1 = 1")
                    node1 = i+1
            if not directedGraph:
                self.Connect(node1, node2)
            else:
                print("Conncting {} to {}".format(node1, node2))
                self.Connect(node1, node2, arrow=True)
            
        return True

    # 1_1b
    def FillGraphFromAL(self, filename, canvas, inCircle=False, directedGraph=False):
        """
        Constructs graph from Adjacency List.
        :return: nothing
        """
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
                    if not directedGraph:
                        self.Connect(i+1, int(vect[j]))
                    else:
                        self.Connect(i+1, int(vect[j]), arrow=True)
                line = f.readline()
                i += 1

    # 1_1c
    def FillGraphFromAM(self, filename, canvas, inCircle=False, directedGraph=False):
        """
        Constructs graph from Adjacency Matrix.
        :return: nothing
        """
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
                    if not directedGraph:
                        self.Connect(i+1, j+1)
                    else:
                        self.Connect(i+1, j+1, arrow=True)

        f.close()
        return True

    # 1_3a
    def FillRandomizeGraphGNL(self, canvas, n_nodes, l_edges,  inCircle=False, directedGraph=False):
        """
        Constructs random graph with given number of nodes and edges.
        :return: nothing
        """
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
            if not directedGraph:
                self.Connect(idx1, idx2)
            else:
                self.Connect(idx1, idx2, arrow=True)


    # 1_3b
    def FillRandomizeGraphGNP(self, canvas, n_nodes, prob,  inCircle=False, directedGraph=False):
        """
        Constructs random graph with given number of nodes and probability
        of that there exists edge between any two nodes. 
        Probability ranges between 0 and 100 [%].
        :return: nothing
        """
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
                    if not directedGraph:
                        self.Connect(node.index, i+1)
                    else:
                        self.Connect(node.index, i+1, arrow=True)


    ############################# PROJECT2 ################################

    def FillFromGraphicSequence(self, filename, canvas, line=1, inCircle=False):
        """
        Constructs random graph from given graphic sequence.
        Returns True if it successfully constructed graph, otherwise False.
        :return: bool
        """
        seq, pls = self.ParseGraphicSequence(filename, line)

        if pls:      
            seq_copy = [[idx, deg] for idx, deg in enumerate(seq)]
        
            adj_list = [[] for _ in range(len(seq))]
            for _ in range(len(seq)):
                seq_copy.sort(reverse=True, key=itemgetter(1))
                i = 0
                j = i + 1
                while seq_copy[i][1] > 0 and j < len(seq_copy):
                    adj_list[seq_copy[i][0]].append(seq_copy[j][0])
                    adj_list[seq_copy[j][0]].append(seq_copy[i][0])
                    seq_copy[i][1] -= 1
                    seq_copy[j][1] -= 1
                    j += 1

            f = open("examples/AL_from_gs.txt", "w")
            ct = 1
            for nbs in adj_list:
                line = ' '.join([str(v+1) for v in nbs]).strip()
                f.write(str(line))
                if ct < len(seq):
                    f.write('\n')
                ct +=1 
                    
            f.close()
            self.FillGraphFromAL("examples/AL_from_gs.txt", canvas,inCircle)
                
            return True
        else:
            return False

    def ParseGraphicSequence(self, filename, line=1):
        """
        Checks if given string from file is a graphic sequence; meaning if it is
        possible to construct graph from it. Returns True if graph can be generated,
        otherwise False.
        :return: bool
        """
        f = open(filename, "r")
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

    def EdgesRandomization(self, count):
        """
        Randomizes [count] times graph's edges. The following statement is true:
        count of edges before = count of edges after randomization.
        Returns False if it cannot randomize, otherwise True.
        :return: bool
        """
        if CanEdgeRandomize(self):
            i = 0
            while i < count:
                Samples = random.sample(self.edges, 2)
                if AreUnique(Samples):
                    a = Samples[0].node1
                    b = Samples[0].node2
                    c = Samples[1].node1
                    d = Samples[1].node2
                    if a.index != c.index and (a, c) not in self.connections and (c, a) not in self.connections:
                        if(self.Connect(d.index, b.index)):
                            self.Connect(a.index, c.index)
                            self.DisconnectByEdge(Samples[0])
                            self.DisconnectByEdge(Samples[1])
                            i += 1
            return True

        else:
            return False

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
            if(CanEdgeRandomize(self)):
                self.EdgesRandomization(10)
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
        SetRandomWeightsOfEdges(self, 1, 10)
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

    def CheckIfConnectionIsABridge(self, node1_idx, node2_idx):
        """
        Check if edge connecting node with index node1_idx and node with index node2_idx is a bridge, that is, checks if number 
        of common connected components after removing the edge increases.
        :return: True of False
        """

        is_bridge = False

        num_of_commmon_components_before_disconecting = len(self.GetCommonComponents())

        self.Disconnect(node1_idx, node2_idx)

        num_of_commmon_components_after_disconecting = len(self.GetCommonComponents())

        if num_of_commmon_components_after_disconecting > num_of_commmon_components_before_disconecting:
            is_bridge = True
        self.Connect(node1_idx, node2_idx)

        return is_bridge

    def ResetGraph(self):
        """
        Sets graph data to origin form.
        :return: Nothing.
        """
        self.nodes = []
        self.edges = []
        self.connections = []
        Node.resetNodeCount()
        Edge.resetEdgesCount()

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
                        self.Disconnect(neighbour, current_node.index)
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

    def IsEveryNodeInTheList(self, list_to_check):
        """
        Checks if every node index is contined in a passed list. 
        :param list_to_check: List to be search for all nodes indexes.
        :return: True or False.
        """
        for node in self.nodes:
            if node.index not in list_to_check:
                return False
        return True

    def FindHamiltonCycle(self):
        """
        If current graph is Hamilton graph, Hamilton Cycle of the graph is found. 
        :return: Hamilton Cycle stored in the list type, or False if there is no Hamilton Cycle of current graph.
        """
        hamilton_cycle = list()
        visited_from = list()
        for node in self.nodes:
            current_node = node
            if current_node.index not in hamilton_cycle:
                hamilton_cycle.append(current_node.index)
                while len(hamilton_cycle) != 0:
                    current_node = self.nodes[hamilton_cycle[-1] - 1]
                    for i, neighbour in enumerate(current_node.neighbours):
                        check = [node_index for node_index in hamilton_cycle]
                        check.append(neighbour)
                        if (neighbour not in hamilton_cycle) and (check not in visited_from):
                            hamilton_cycle.append(neighbour)
                            visited_from.append(check)
                            current_node = self.nodes[neighbour - 1]
                            visited_from.append(hamilton_cycle)
                            break
                        elif self.IsEveryNodeInTheList(hamilton_cycle) and (hamilton_cycle[0] == neighbour):
                            hamilton_cycle.append(neighbour)
                            return hamilton_cycle
                        elif i == len(current_node.neighbours) - 1:
                            hamilton_cycle.pop()
        return None

    # 2_5
    def CheckIfIsHamiltonGraph(self, canvas, filepath, in_circle=False):
        """
        Check if current graph contains Hamilton Cycle. 
        :return: Value returned by FindHamiltonCycle() method.
        """
        if filepath == None:
            num_of_nodes = random.randint(4, 10)
            self.FillRandomizeGraphGNP(canvas, num_of_nodes, 0.5, inCircle=in_circle)
        else: 
            self.FillGraphFromIM(filepath, canvas, inCircle=in_circle)

        return self.FindHamiltonCycle()


    ############################# PROJECT3 ################################

    # 3-2
    def DijsktraInit(self, nodeIdx):
        p = []
        d = []
        for n in self.nodes:
            d.append(float("inf"))
            p.append(None)
        d[nodeIdx-1] = 0
        p[nodeIdx-1] = -1
        return p, d

    def Relaxation(self, node1, node2, d, p):
        w = 0
        for e in self.edges:
            if ( (e.node1 == node1) and (e.node2 == node2) ) or ( (e.node1 == node2) and (e.node2 == node1) ):
                w = e.weight
        if d[node2.index-1] > (d[node1.index-1] + w):
            d[node2.index-1] = d[node1.index-1] + w
            p[node2.index-1] = node1.index - 1

    def DijkstraShortestPaths(self, nodeIdx):
        if nodeIdx > self.NodesCount():
            return "Wrong index"
        S = []
        p, d = self.DijsktraInit(nodeIdx)
        tempD = d.copy()
        u = self.nodes[0]
        while len(S) < len(self.nodes):
            index_min = tempD.index(min(tempD))
            u = self.nodes[index_min]
            S.append(u)
            for v in u.neighbours:
                if self.nodes[v-1] not in S:
                    self.Relaxation(u, self.nodes[v-1], d, p)
            tempD = d.copy()
            for n in S:
                tempD[n.index-1] = float("inf")
        infoString = "START: s = " + str(nodeIdx)
        listOfPaths = []
        for n in range(0, len(self.nodes)):
            shortestPath = []
            infoString += "\nd(" + str(n+1) + ") = " + str(d[n]) + " ==> ["
            counter = 0
            tempS = []
            j = n
            while j > -1:
                tempS.append(j)
                counter += 1
                j = p[j]
            while( counter > 0):
                counter -= 1
                shortestPath.append(tempS[counter]+1)
                infoString += str(tempS[counter]+1) + " - "
            infoString = infoString[:-3] + ']'
            listOfPaths.append(shortestPath)
        return infoString,  d, listOfPaths    
    
    # 3_3
    def DistanceMatrix(self):
        infoString = ""
        distanceMatrix = []
        for idx in range(self.NodesCount()):
            distanceMatrix.append(self.DijkstraShortestPaths(idx + 1)[1])
        
        for i in range(self.NodesCount()):
            for j in range(self.NodesCount()):
                infoString += '{:4}'.format(str(distanceMatrix[i][j])) + "  "
            infoString += "\n"
        return distanceMatrix, infoString

    # 3_4
    def FindCentralVertex(self):
        listAllDistance = [0 for i in range(self.NodesCount())]
        distanceMatrix = self.DistanceMatrix()[0]

        for i in range(self.NodesCount()):
            for j in range(self.NodesCount()):
                listAllDistance[i] += distanceMatrix[i][j]
        
        infoString = ("Central Vertex = {}\n(distance : {})").format(listAllDistance.index(min(listAllDistance)) + 1, min(listAllDistance))
        
        return infoString
        
    def FindMinimaxVertex(self):
        listOfMaxAllDistances = []
        distanceMatrix = self.DistanceMatrix()[0]

        for i in range(self.NodesCount()):
            listOfMaxAllDistances.append(max(distanceMatrix[i]))

        infoString = ("Minimax Vertex = {}\n(distance : {})").format(listOfMaxAllDistances.index(min(listOfMaxAllDistances)) + 1, min(listOfMaxAllDistances))
        
        return infoString

    # 3_5
    def GetEdgeFromIndexes(self, idx1, idx2):
        """
        Gets the Edge object that connects two nodes of given indexes.
        :return: Edge
        """
        try:
            for e in self.edges:
                if (e.node1.index == idx1 and e.node2.index == idx2) or (e.node1.index == idx2 and e.node2.index == idx1):
                    return e
        except Exception:
            print(f"[GetEdgeFromIndexes] There is no connection ({idx1},{idx2}) in this graph.")
    
    def IsGraphConsistent(self):
        visited = [False for _ in range(self.NodesCount())]
        visit_count = 0
        nodes_set = set([])
        nodes_set.add(1)
        visited[0] = True
        while len(nodes_set) > 0:
            node = NodeFromIndex(self, nodes_set.pop())
            visit_count += 1
            for nb in node.neighbours:
                if visited[nb-1]:
                    continue
                visited[nb-1] = True
                nodes_set.add(nb)
            

        return visit_count == self.NodesCount()

    def IsCyclicRec(self, idx, visited, parent): 
        """
        Helper func for checking if graph is cyclic.

        :return: bool
        """
        visited[idx-1] = True
        curr_node = NodeFromIndex(self, idx)
        for nb_idx in curr_node.neighbours:
            if not visited[nb_idx-1]:
                if self.IsCyclicRec(nb_idx, visited, curr_node.index):
                    return True
            elif parent != nb_idx: 
                return True
        return False

    def IsCyclic(self): 
        """
        Method that checks if there exists any cycle in graph.
        :return: bool
        """

        visited = [False for i in range(self.NodesCount())]
        
        for idx in range(1, self.NodesCount()+1): 
            if not visited[idx-1]: 
                if self.IsCyclicRec(idx, visited, -1): 
                    return True
        return False

    def CausesCycleIfAdded(self, edge):
        """
        Checks if adding edge to the current graph would cause cycle.
        :return: bool
        """
        i1 = edge.node1.index
        i2 = edge.node2.index
        self.Connect(i1, i2)
        causes = self.IsCyclic()
        self.Disconnect(i1, i2)
        return causes    
        

    def MinSpanningTreeKruskal(self):
        """
        Generates minimum spanning tree based on Kruskal algorithm.
        Prerequisite to use this function properly is that current graph 
        1) is already constructed (not empty)
        2) is consistent.
        
        :return: Nothing
        """
        nodes = [n for n in self.nodes]
        edges = [e for e in self.edges]
        self.ResetGraph()
        for n in nodes:
            self.AddNode(n)
            n.neighbours = []

        
        edges.sort(key=lambda e: e.weight)
        
        for edge in edges:
            if not self.CausesCycleIfAdded(edge):
                self.ConnectByEdge(edge)
            if len(self.edges) == self.NodesCount()-1:
                break 


############################# PROJECT4 ################################

    def GetConnectionIndexes(self):
        connectionsWithNodesIndexes = list()
        for (a, b) in self.connections:
            connectionsWithNodesIndexes.append((a.index, b.index))
        return connectionsWithNodesIndexes

    def SaveToALFile(self, filename, targetDict="./examples"):
        with open("{}/{}".format(targetDict, filename), 'w') as targetALFile:
            for node in self.nodes:
                neighbours = str() 
                for neighbour in node.neighbours:
                    neighbours += (str(neighbour) + " ")
                if node == self.nodes[len(self.nodes) - 1]:
                    targetALFile.write("{}".format(neighbours[:-1]))
                else:
                    targetALFile.write("{}\n".format(neighbours[:-1]))

    def SaveToAMFile(self, filename, targetDict="./examples"):
        with open("{}/{}".format(targetDict, filename), 'w') as targetALFile:
            for node in self.nodes:
                nodeNeigboursAdjencyRow = list()
                row = str()
                nodeNeigboursAdjencyRow = node.GetNeighboursInVector()
                for isNeighbour in nodeNeigboursAdjencyRow:
                    row += str(isNeighbour) + " "
                if node == self.nodes[len(self.nodes) - 1]:
                        targetALFile.write("{}".format(row[:-1]))
                else:
                    targetALFile.write("{}\n".format(row[:-1]))
        self.PrintAdjacencyMatrix()


