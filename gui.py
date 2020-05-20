from tkinter import *
from tkinter.ttk import *
from graph import *
from tkinter import (filedialog, simpledialog, messagebox)
import tkinter as tk


class GUI:
    def __init__(self, root):
        root.title("WARTOWNICY: wfiis-graph-theory")
        root.geometry("1400x900")
        root.minsize(1400, 900)

        self.graph = Graph()  # since project 3

        self.canvas = Canvas(root, width=1200, height=800, bg="white")
        self.AddTabs(root)
        self.AddProject1Widgets(root)
        self.AddProject2Widgets(root)
        self.AddProject3Widgets(root)
        self.AddProject4Widgets(root)
        self.AddProject5Widgets(root)
        self.allTabs.pack(expand=1, fill='both')
        self.canvas.pack(fill=X, padx=10, pady=10)

    def AddTabs(self, root):
        self.allTabs = Notebook(root)
        self.tab1 = Frame(self.allTabs)
        self.tab2 = Frame(self.allTabs)
        self.tab3 = Frame(self.allTabs)
        self.tab4 = Frame(self.allTabs)
        self.tab5 = Frame(self.allTabs)
        self.tab6 = Frame(self.allTabs)

        self.allTabs.add(self.tab1, text="Project 1")
        self.allTabs.add(self.tab2, text="Project 2")
        self.allTabs.add(self.tab3, text="Project 3")
        self.allTabs.add(self.tab4, text="Project 4")
        self.allTabs.add(self.tab5, text="Project 5")
        self.allTabs.add(self.tab6, text="Project 6")

    def ClearCanvas(self):
        self.canvas.delete("all")

    def Draw(self, graph, inCircle=False, color="#aaa", weighted=False, isNetwork=False,  isCapacity=False, isFlow=False, numberOfLayers=-1):
        self.ClearCanvas()
        if isNetwork:
            self.DrawLayersRectangle(numberOfLayers)
        if inCircle:
            self.DrawCircleTrace(graph)
        for e in graph.edges:
            e.Draw(self.canvas, weighted, isCapacity, isFlow)
        for n in graph.nodes:
            n.Draw(self.canvas, color, numberOfLayers)

    def DrawLayersRectangle(self, number):
        width = self.canvas.winfo_width()/(number + 2)
        height = self.canvas.winfo_height()
        for i in range(1, number + 2):
            self.canvas.create_line(width*i, 0, width*i, height,  dash=(15, 20), width = 1)

    def DrawCircleTrace(self, graph):
        xmin = min([n.x for n in graph.nodes])
        ymin = min([n.y for n in graph.nodes])
        xmax = max([n.x for n in graph.nodes])
        ymax = max([n.y for n in graph.nodes])

        self.canvas.create_oval(xmin, ymin, xmax, ymax,
                                dash=(15, 20), outline='red', width=2)

    #################### PROJECT 1 ##########################

    def SelectIM(self):
        filepath = filedialog.askopenfilename(initialdir='examples', filetypes=(
            ("Text files", "IM_*.txt"), ("all files", "*.*")))
        isChecked = bool(self.checkP1.get())
        g = Graph()
        g.FillGraphFromIM(filepath, self.canvas, isChecked)
        self.Draw(g, isChecked)

        g.PrintAdjacencyList()
        g.PrintAdjacencyMatrix()

    def SelectAL(self):
        filepath = filedialog.askopenfilename(initialdir='examples', filetypes=(
            ("Text files", "AL_*.txt"), ("all files", "*.*")))
        isChecked = bool(self.checkP1.get())
        g = Graph()
        g.FillGraphFromAL(filepath, self.canvas, isChecked)
        self.Draw(g, isChecked)

        g.PrintAdjacencyMatrix()
        g.PrintIncidenceMatrix()

    def SelectAM(self):
        filepath = filedialog.askopenfilename(initialdir='examples', filetypes=(
            ("Text files", "AM_*.txt"), ("all files", "*.*")))
        isChecked = bool(self.checkP1.get())
        g = Graph()
        g.FillGraphFromAM(filepath, self.canvas, isChecked)
        self.Draw(g, isChecked)

        g.PrintIncidenceMatrix()
        g.PrintAdjacencyList()

    def SelectRandomGraphNL(self, n, l):
        g = Graph()
        isChecked = bool(self.checkP1.get())
        if(l > (n * (n-1) / 2)):
            messagebox.showerror(
                title="Błąd", message="[SelectRandomGraphNL] Invalid arguments' values.")
        else:
            g.FillRandomizeGraphGNL(self.canvas, n, l, isChecked)
            self.Draw(g, isChecked)

    def SelectRandomGraphNP(self, n, p):
        g = Graph()
        isChecked = bool(self.checkP1.get())
        g.FillRandomizeGraphGNP(self.canvas, n, p, isChecked)
        self.Draw(g, isChecked)

    def AddProject1Widgets(self, root):
        menuProj1 = Frame(self.tab1, width=1200, height=30)

        # check if generate graph in circle
        self.checkP1 = IntVar()
        checkInCircle = Checkbutton(
            menuProj1, text="In circle", variable=self.checkP1)

        # 1
        label1 = Label(menuProj1, text='Task 1 / Task 2',
                       foreground="red")
        buttonIM = Button(
            menuProj1, text="Generate graph - incident matrix", command=self.SelectIM)
        buttonNL = Button(
            menuProj1, text="Generate graph - adjacency list", command=self.SelectAL)
        buttonNM = Button(
            menuProj1, text="Generate graph - adjacency matrix", command=self.SelectAM)

        # 3
        label3 = Label(menuProj1, text='Task 3',  foreground="red")
        labelToValues = Label(
            menuProj1, text='Select: ')
        labelToValuesA = Label(
            menuProj1, text='n - nodes')
        labelToValuesB = Label(
            menuProj1, text='l - edges')
        labelToValuesC = Label(
            menuProj1, text='p - odds of any two nodes to be connected [%]')

        labelN = Label(menuProj1, text='n: ')
        N = Spinbox(menuProj1, from_=0, to=200, width=8, state="readonly")

        labelLP = Label(menuProj1, text='l/p: ')
        LP = Spinbox(menuProj1, from_=0, to=100, width=8, state="readonly")

        buttonRandomGraphNL = Button(
            menuProj1, text="Generate graph - random G(n,l)", command=lambda: self.SelectRandomGraphNL(int(N.get()), int(LP.get())))

        buttonRandomGraphNP = Button(
            menuProj1, text="Generate graph - random G(n,p)", command=lambda: self.SelectRandomGraphNP(int(N.get()), float(int(LP.get()))/100.0))

        label1.grid(column=0, row=0, padx=10, pady=5)
        checkInCircle.grid(column=3, row=0, padx=10, pady=5)

        buttonIM.grid(column=0, row=1, sticky="nsew", padx=10, pady=5)
        buttonNL.grid(column=1, row=1, sticky="nsew", padx=10, pady=5)
        buttonNM.grid(column=2, row=1, sticky="nsew", padx=10, pady=5)

        label3.grid(column=0, row=2, padx=10, pady=5)

        labelToValues.grid(column=0, row=3, sticky="nsew")
        labelToValuesA.grid(column=0, row=4, sticky="nsew")
        labelToValuesB.grid(column=0, row=5, sticky="nsew")
        labelToValuesC.grid(column=0, row=6, sticky="nsew")

        labelN.grid(column=1, row=3, sticky="nse", padx=10, pady=5)
        N.grid(column=2, row=3, sticky="nsew", padx=10, pady=5)

        labelLP.grid(column=1, row=4, sticky="nse", padx=10, pady=5)
        LP.grid(column=2, row=4, sticky="nsew", padx=10, pady=5)

        buttonRandomGraphNL.grid(
            column=2, row=5, sticky="nsew", padx=10, pady=5)
        buttonRandomGraphNP.grid(
            column=2, row=6, sticky="nsew", padx=10, pady=5)

        menuProj1.pack(fill=Y)

    #################### POJECT 2 #########################

    def SelectGraphicSeq(self):
        filepath = filedialog.askopenfilename(initialdir='examples', filetypes=(
            ("Text files", "GS*.txt"), ("all files", "*.*")))

        g = Graph()
        isChecked = bool(self.checkP2.get())

        if g.FillFromGraphicSequence(filepath, self.canvas, inCircle=isChecked):
            self.Draw(g, isChecked)
        else:
            messagebox.showerror(
                title="Błąd", message="[SelectGraphicSeq] Given sequence is not graphic sequence.")

    def SelectRandomGraphGraphicSeq(self, num):
        filepath = filedialog.askopenfilename(initialdir='examples', filetypes=(
            ("Text files", "GS*.txt"), ("all files", "*.*")))
        g = Graph()
        isChecked = bool(self.checkP2.get())
        if(g.FillFromGraphicSequence(filepath, self.canvas, inCircle=isChecked)):
            if(g.EdgesRandomization(num)):
                self.Draw(g, isChecked)
            else:
                messagebox.showerror(
                    title="Błąd", message="[SelectRandomGraphGraphicSeq] This Graph cannot be randomized.")
        else:
            messagebox.showerror(
                title="Błąd", message="[SelectRandomGraphGraphicSeq] Given sequence is not graphic sequence.")

    def SelectFindConnectedComponent(self):
        # filepath first letters should by FCC == Find Connected Component
        filepath = filedialog.askopenfilename(initialdir='examples', filetypes=(
            ("Text files", "FCC_*.txt"), ("all files", "*.*")))
        isChecked = bool(self.checkP2.get())
        g = Graph()
        self.ClearCanvas()
        info = g.FillComponents(
            filepath, self.canvas, isChecked)  # info is string type
        self.Draw(g, isChecked)
        messagebox.showinfo(
            title="Info", message=info)

    def SelectEuleranGraph(self, num_of_nodes=0):
        """
        Invokes function that generates random Euler Graph and then finds Euler Circuit of that graph.

        :param num_of_nodes: Number of nodes of a graph to be randomly generated.
        :return: None
        """
        g = Graph()
        is_checked = bool(self.checkP2.get())
        if num_of_nodes != 0 and num_of_nodes < 3 :
            messagebox.showinfo(
                title="Info", message="[SelectEuleranGraph] Euler Graph must have at least 3 nodes")
            return

        euler_circuit = g.GetEulersCycleFromRandomEulerGraph(
            self.canvas, num_of_nodes, in_circle=is_checked)
        self.Draw(g, inCircle=is_checked)
        messagebox.showinfo(
            title="Info", message="[SelectEuleranGraph] Found Euler Cycle : {}".format(euler_circuit))

    def SelectKReguralGraph(self, n, k):
        g = Graph()
        isChecked = bool(self.checkP2.get())
        if (g.FillKReguralGraph(self.canvas, n, k, isChecked)):
            self.Draw(g, inCircle=isChecked)
        else:
            messagebox.showerror(
                title="Error",
                message="[SelectKReguralGraph] Couldn't make {}-regular graph from given values.".format(k))

    def SelectCheckHamiltonGraph(self, tof):
        """
        Checks if graph is Hamilton graph, if that's true, hamilton cycle is printed.

        :param tof: Value determinig if graph is loaded from incidence matrix.
        :return: None
        """
        g = Graph()
        filepath = None
        if(tof):
            filepath = filedialog.askopenfilename(filetypes=(
                ("Text files", "IM_*.txt"), ("all files", "*.*")))
        else:
            filepath = None
        is_checked = bool(self.checkP2.get())    

        hamilton_cycle = g.CheckIfIsHamiltonGraph(self.canvas, filepath, in_circle=is_checked)
        self.Draw(g, inCircle=is_checked)

        if hamilton_cycle:
            messagebox.showinfo(title="Info", message="[SelectEuleranGraph]  Found hamilton cycle: {}".format(hamilton_cycle))
        else:
            messagebox.showinfo(title="Info", message="[SelectEuleranGraph]  Given graph is not Hamilton graph: {}".format(hamilton_cycle))

    def AddProject2Widgets(self, root):
        menuProj2 = Frame(self.tab2, width=1200, height=30)

        # check if generate graph in circle
        self.checkP2 = IntVar()
        checkInCircle2 = Checkbutton(
            menuProj2, text="In circle", variable=self.checkP2)

        # 1
        label1 = Label(menuProj2, text='Task 1',
                       foreground="red")
        button1 = Button(
            menuProj2, text="Generate graph - from graphic sequence", command=lambda: self.SelectGraphicSeq())

        # 2
        label2 = Label(menuProj2, text='Task 2', foreground="red")
        label2a = Label(menuProj2, text='How many randomizations')
        spinbox2a = Spinbox(menuProj2, from_=0, to=100,
                            width=8, state="readonly")
        button2 = Button(
            menuProj2, text="Generate graph - randomize connections", command=lambda: self.SelectRandomGraphGraphicSeq(int(spinbox2a.get())))

        # 3
        label3 = Label(menuProj2, text='Task 3', foreground="red")
        button3 = Button(
            menuProj2, text="Generate graph - find the longest common component", command=self.SelectFindConnectedComponent)

        # 4
        label4 = Label(menuProj2, text='Task 4', foreground="red")
        label4a = Label(
            menuProj2, text='Nodes (n=0 -> random quantity)')
        spinbox4a = Spinbox(menuProj2, from_=0, to=100,
                            width=8, state="readonly")
        button4 = Button(
            menuProj2, text="Generate graph - Euleran graph", command=lambda: self.SelectEuleranGraph(int(spinbox4a.get())))

        # 5
        label5 = Label(menuProj2, text='Task 5', foreground="red")
        label5a = Label(
            menuProj2, text='1 - nodes, 2 - degree of a node')
        spinbox5b = Spinbox(menuProj2, from_=0, to=100,
                            width=8, state="readonly")
        spinbox5c = Spinbox(menuProj2, from_=0, to=100,
                            width=8, state="readonly")
        button5 = Button(
            menuProj2, text="Generate graph - random k-regular", command=lambda: self.SelectKReguralGraph(int(spinbox5b.get()), int(spinbox5c.get())))

        # 6
        label6 = Label(menuProj2, text='Task 6', foreground="red")
        button6a = Button(
            menuProj2, text="Check if graph is Hamiltonian - from file", command=lambda: self.SelectCheckHamiltonGraph(True))
        button6b = Button(
            menuProj2, text="Check if graph is Hamiltonian - random graph", command=lambda: self.SelectCheckHamiltonGraph(False))

        label1.grid(column=0, row=0)
        checkInCircle2.grid(column=3, row=0)
        button1.grid(column=0, row=1, sticky="nsew", padx=10, pady=5)
        label2.grid(column=0, row=2)
        label2a.grid(column=0, row=3)
        spinbox2a.grid(column=0, row=4, sticky="nsew", padx=10, pady=5)
        button2.grid(column=0, row=5, sticky="nsew", padx=10, pady=5)

        label3.grid(column=1, row=0)
        button3.grid(column=1, row=1, sticky="nsew", padx=10, pady=5)
        label4.grid(column=1, row=2)
        label4a.grid(column=1, row=3, padx=10, pady=5)
        spinbox4a.grid(column=1, row=4, sticky="nsew", padx=10, pady=5)
        button4.grid(column=1, row=5, sticky="nsew", padx=10, pady=5)

        label5.grid(column=2, row=0)
        label5a.grid(column=2, row=1)
        spinbox5b.grid(column=2, row=2, sticky="nsew", padx=10, pady=5)
        spinbox5c.grid(column=2, row=3, sticky="nsew", padx=10, pady=5)
        button5.grid(column=2, row=4, sticky="nsew", padx=10, pady=5)
        label6.grid(column=2, row=5)
        button6a.grid(column=2, row=6, sticky="nsew", padx=10, pady=5)
        button6b.grid(column=2, row=7, sticky="nsew", padx=10, pady=5)

        menuProj2.pack(fill=Y)

    #################### POJECT 3 #########################

    def SelectBasicGraph(self, fromFile, n=0, l=0):
        # check is connected graph
        isCheckedCircle = bool(self.checkP3.get())
        if(fromFile == True):  # fromFile True for generate graph from file
            filepath = filedialog.askopenfilename(initialdir='examples', filetypes=(
                ("Text files", "IM_*.txt"), ("all files", "*.*")))
            self.graph.FillGraphFromIM(filepath, self.canvas, isCheckedCircle)

        else:       # fromFile False for generate random graph
            if(l > (n * (n-1) / 2)):
                messagebox.showerror(
                    title="Błąd", message="[SelectBasicGraph] Invalid arguments' values.")
            else:
                self.graph.FillRandomizeGraphGNL( self.canvas, n, l, isCheckedCircle)
                
        if not self.graph.IsGraphConsistent():
            self.graph.ResetGraph()
            self.ClearCanvas()
            messagebox.showerror(
                title="Error", message="[SelectBasicGraph] Graph is not connected.")
        else:
            isWeighted = bool(self.checkP3weighted.get())
            self.Draw(self.graph, inCircle=isCheckedCircle,   weighted=isWeighted)

    def SelectAddWeights(self):
        isCheckedCircle = bool(self.checkP3.get())
        isWeighted = bool(self.checkP3weighted.get())
        SetRandomWeightsOfEdges(self.graph, 1, 10)
        self.graph.PrintEdgesWithWeights()
        self.Draw(self.graph, inCircle=isCheckedCircle,
                  weighted=isWeighted)

    def SelectTheShortestPath(self, numOfVertex=1):
        info = self.graph.DijkstraShortestPaths(numOfVertex)[0]
        messagebox.showinfo( title="Info", message=info)

    def SelectDistanceMatrix(self):
        info = self.graph.DistanceMatrix()[1]
        messagebox.showinfo( title="Info", message=info)

    def SelectFindCentralVertex(self):
        info = self.graph.FindCentralVertex()
        messagebox.showinfo( title="Info", message=info)

    def SelectFindMinimaxVertex(self):
        info = self.graph.FindMinimaxVertex()
        messagebox.showinfo(title="Info", message=info)

    def SelectFindMinSpanningTree(self):
        if not self.graph.IsGraphConsistent():
            messagebox.showerror(
                title="Error", message="[SelectFindMinSpanningTree] Graph is not consistent - cannot find minimum spanning tree.")
        else:
            isCheckedCircle = bool(self.checkP3.get())
            isWeighted = bool(self.checkP3weighted.get())

            self.ClearCanvas()
            self.graph.MinSpanningTreeKruskal()
            self.Draw(self.graph, inCircle=isCheckedCircle, weighted=isWeighted)
            messagebox.showinfo(
                title="Info", message="[SelectFindMinSpanningTree] Minimum spanning tree has been drawn.")

    def AddProject3Widgets(self, root):
        menuProj3 = Frame(self.tab3, width=1200, height=30)

        # check if generate graph in circle
        self.checkP3 = IntVar()
        checkInCircle3 = Checkbutton(
            menuProj3, text="In circle", variable=self.checkP3)

        # check if generate graph draw with Weights
        self.checkP3weighted = IntVar()
        checkShowWeights3 = Checkbutton(
            menuProj3, text="Weighted graph", variable=self.checkP3weighted)

        # 0
        label0a = Label(menuProj3, text='- vertices')
        label0b = Label(menuProj3, text='- edges')
        spinbox0a = Spinbox(menuProj3, from_=0, to=100,
                            width=35, state="readonly")
        spinbox0b = Spinbox(menuProj3, from_=0, to=100,
                            width=35, state="readonly")
        button0a = tk.Button(
            menuProj3, width=35, text='Generate graph from file', command=lambda: self.SelectBasicGraph(True), bg="red", fg="white")

        button0b = tk.Button(
            menuProj3, width=35,  text="Generate random graph", command=lambda: self.SelectBasicGraph(False, int(spinbox0a.get()), int(spinbox0b.get())), bg="red", fg="white")

        # 1
        label1 = Label(menuProj3, text='Task 1', foreground="red")
        button1 = Button(
            menuProj3, text="Randomize graph's weights", command=lambda: self.SelectAddWeights())

        # 2
        label2 = Label(menuProj3, text='Task 2', foreground="red")
        spinbox2 = Spinbox(menuProj3, from_=1, to=100,
                           width=8, state="readonly")
        button2 = Button(
            menuProj3, text="Find the shortest path (choose vertex first)", command=lambda: self.SelectTheShortestPath(int(spinbox2.get())))

        # 3
        label3 = Label(menuProj3, text='Task 3', foreground="red")
        button3 = Button(
            menuProj3, text="Generate Distance Matrix", command=self.SelectDistanceMatrix)

        # 4
        label4 = Label(menuProj3, text='Task 4', foreground="red")
        button4a = Button(
            menuProj3, text="Find central vertex", command=self.SelectFindCentralVertex)
        button4b = Button(
            menuProj3, text="Find minimax vertex", command=self.SelectFindMinimaxVertex)

        # 5
        label5 = Label(menuProj3, text='Task 5', foreground="red")
        button5 = Button(
            menuProj3, text="Find minimum spanning tree", command=self.SelectFindMinSpanningTree)

        # row 0
        spinbox0a.grid(column=0, row=0, sticky="nsew", padx=10, pady=5)
        label0a.grid(column=1, row=0, sticky="w")
        button0a.grid(column=2, row=0, sticky="nsew", padx=10, pady=5)
        checkInCircle3.grid(column=3, row=0, sticky="nsew", padx=10, pady=5)

        # row 1
        spinbox0b.grid(column=0, row=1, sticky="nsew", padx=10, pady=5)
        label0b.grid(column=1, row=1, sticky="w")
        button0b.grid(column=2, row=1, sticky="nsew", padx=10, pady=5)
        checkShowWeights3.grid(column=3, row=1, sticky="nsew", padx=10, pady=5)

        # row 2
        label1.grid(column=0, row=2)
        label2.grid(column=1, row=2)
        label3.grid(column=2, row=2)

        # row 3
        button1.grid(column=0, row=3, sticky="nsew", padx=10, pady=5)
        spinbox2.grid(column=1, row=3, sticky="nsew", padx=10, pady=5)
        button3.grid(column=2, row=3, sticky="nsew", padx=10, pady=5)

        # row 4
        label4.grid(column=0, row=4)
        button2.grid(column=1, row=4, sticky="nsew", padx=10, pady=5)
        label5.grid(column=2, row=4)

        # row 5
        button4a.grid(column=0, row=5, sticky="nsew", padx=10, pady=5)
        button5.grid(column=2, row=5, sticky="nsew", padx=10, pady=5)

        # row 6
        button4b.grid(column=0, row=6, sticky="nsew", padx=10, pady=5)

        menuProj3.pack(fill=Y)

    #################### POJECT 4 #########################
    
    def SelectBasicDigraph(self, n=0, propability=0):
        isCheckedCircle = bool(self.checkP4.get())
        propability = propability / 100
        self.graph = Graph(directed=True)
        self.graph.ResetGraph()
        self.graph.FillRandomizeGraphGNP(self.canvas, n, propability, inCircle=isCheckedCircle, directedGraph=True)
        # TO DO 
        # FUNCTION TO CREATE RANDOM DIGRAPH
        # # DRAW
        isWeighted = bool(self.checkP4weighted.get())
        self.Draw(self.graph, inCircle=isCheckedCircle, weighted=isWeighted)

    def SaveDAMToFile(self):
        targetDAMFile = simpledialog.askstring("File name", "Enter filename", initialvalue="AM_directed_graph.txt")
        self.graph.SaveToAMFile(targetDAMFile)

    def SelectDAM(self):
        filepath = filedialog.askopenfilename(initialdir='examples', filetypes=(
            ("Text files", "AM_*.txt"), ("all files", "*.*")))
        isChecked = bool(self.checkP4.get())
        isWeighted = bool(self.checkP4weighted.get())
        self.graph = Graph()
        self.graph.FillGraphFromAM(filepath, self.canvas, isChecked, directedGraph=True)
        self.Draw(self.graph, inCircle=isChecked, weighted=isWeighted)

        self.graph.PrintIncidenceMatrix()
        self.graph.PrintAdjacencyList()

    def SelectDIM(self):
        filepath = filedialog.askopenfilename(initialdir='examples', filetypes=(
            ("Text files", "IM_*.txt"), ("all files", "*.*")))

        isChecked = bool(self.checkP4.get())
        isWeighted = bool(self.checkP4weighted.get())
        self.graph = Graph(directed=True)
        self.graph.FillGraphFromIM(filepath, self.canvas, isChecked, directedGraph=True)
        self.Draw(self.graph, inCircle=isChecked, weighted=isWeighted)

        self.graph.PrintAdjacencyList()
        self.graph.PrintAdjacencyMatrix()

    def SaveDIMToFile(self):
        targetDIMFile = simpledialog.askstring("File name", "Enter filename", initialvalue="IM_directed_graph.txt")
        self.graph.SaveToIMFile(targetDIMFile)

    def SelectDAL(self):
        filepath = filedialog.askopenfilename(initialdir='examples', filetypes=(
            ("Text files", "AL_*.txt"), ("all files", "*.*")))
        isChecked = bool(self.checkP4.get())
        isWeighted = bool(self.checkP4weighted.get())
        self.graph = Graph()
        self.graph.FillGraphFromAL(filepath, self.canvas, isChecked, directedGraph=True)
        self.Draw(self.graph, inCircle=isChecked, weighted=isWeighted)

        self.graph.PrintAdjacencyMatrix()
        self.graph.PrintIncidenceMatrix()

    def SaveDALToFile(self):
        targetALFileName = simpledialog.askstring("File name", "Enter filename", initialvalue="AL_directed_graph.txt")
        self.graph.SaveToALFile(targetALFileName)

    def SelectFindCommonComponentDigraph(self):
        isChecked = bool(self.checkP4.get())
        isWeighted = bool(self.checkP4weighted.get())
        self.ClearCanvas()
        info = self.graph.KosarajuAlgorithm()[0]  # info is string type
        self.Draw( self.graph, isChecked, weighted=isWeighted)
        messagebox.showinfo(title="Info", message=info)

    def SelectAddWeightsDigraph(self):
        if(self.graph.KosarajuAlgorithm()[1] == 1):  
            isChecked = bool(self.checkP4.get())
            isWeighted = bool(self.checkP4weighted.get())
            SetRandomWeightsOfEdges(self.graph, -2, 10)
            self.graph.PrintEdgesWithWeights()
            self.ClearCanvas()
            self.Draw( self.graph, isChecked, weighted=isWeighted)
        else:
            messagebox.showerror(title="Error", message="[SelectAddWeightsDigraph] Digrahp is not strongly connected, impossible to add weights")

    def SelectTheShortestPathDigraph(self, numOfVertex = 1):
        negativeCycle, iStr, weights, paths = self.graph.BellmanFordAlgorithm(numOfVertex)
        if( negativeCycle ):
            messagebox.showerror(title="Error", message="Graph doesnt have negative cycle\n" + iStr)
        else:
            messagebox.showerror(title="Error", message="Graph does have negative cycle")

    def SelectDistanceMatrixDigraph(self):
        info = self.graph.JohnsonAlgorithm()
        messagebox.showinfo(title="Info", message=info)


    def AddProject4Widgets(self, root):
        menuProj4 = Frame(self.tab4, width=1200, height=30)

        # check if generate graph in circle
        self.checkP4 = IntVar()
        checkInCircle4 = Checkbutton(
            menuProj4, text="In circle", variable=self.checkP4)

        # check if generate graph draw with Weights
        self.checkP4weighted = IntVar()
        checkShowWeights4 = Checkbutton(
            menuProj4, text="Weighted graph", variable=self.checkP4weighted)

        # 1
        label1a = Label(menuProj4, text='- vertices',width=35)
        label1b = Label(menuProj4, text='- propability (%)',width=35)
        spinbox1a = Spinbox(menuProj4, from_=0, to=100,
                            width=35, state="readonly")
        spinbox1b = Spinbox(menuProj4, from_=0, to=100,
                            width=35, state="readonly")

        buttonIM = Button(
            menuProj4, text="Generate digraph - incident matrix", command=self.SelectDIM)
        buttonNL = Button(
            menuProj4, text="Generate digraph - adjacency list", command=self.SelectDAL)
        buttonNM = Button(
            menuProj4, text="Generate digraph - adjacency matrix", command=self.SelectDAM)        

        buttonToIM = Button(
            menuProj4, text="Save digraph - incident matrix", command=self.SaveDIMToFile)
        buttonToNL = Button(
            menuProj4, text="Save digraph - adjacency list", command=self.SaveDALToFile)
        buttonToNM = Button(
            menuProj4, text="Save digraph - adjacency matrix", command=self.SaveDAMToFile)

        button1 = tk.Button(
            menuProj4, width=35,  text="Generate random digraph", command=lambda: self.SelectBasicDigraph(int(spinbox1a.get()), int(spinbox1b.get())), bg="red", fg="white")

        # 2
        label2 = Label(menuProj4, text='Task 2', foreground="red")
        button2 = Button(
            menuProj4, text="Find common components", command=lambda: self.SelectFindCommonComponentDigraph())

        # 3
        label3 = Label(menuProj4, text='Task 3', foreground="red")
        button3a = Button(
            menuProj4, text="Randomize graph's weights", command=lambda: self.SelectAddWeightsDigraph())
        spinbox3 = Spinbox(menuProj4, from_=1, to=100,
                           width=8, state="readonly")
        button3b = Button(
            menuProj4, text="Find the shortest path (choose vertex first)", command=lambda: self.SelectTheShortestPathDigraph(int(spinbox3.get())))

        # 4
        label4 = Label(menuProj4, text='Task 4', foreground="red")
        button4 = Button(
            menuProj4, text="Generate Distance Matrix", command=self.SelectDistanceMatrixDigraph)

        # row 0
        spinbox1a.grid(column=0, row=0, sticky="nsew", padx=10, pady=5)
        label1a.grid(column=1, row=0, sticky="w")
        checkInCircle4.grid(column=3, row=0, sticky="nsew", padx=10, pady=5)

        # row 1
        spinbox1b.grid(column=0, row=1, sticky="nsew", padx=10, pady=5)
        label1b.grid(column=1, row=1, sticky="w")
        button1.grid(column=2, row=1, sticky="nsew", padx=10, pady=5)
        checkShowWeights4.grid(column=3, row=1, sticky="nsew", padx=10, pady=5)

        # row 2
        label2.grid(column=0, row=2)
        label3.grid(column=1, row=2)
        label4.grid(column=2, row=2)

        # row 3
        button2.grid(column=0, row=3, sticky="nsew", padx=10, pady=5)
        button3a.grid(column=1, row=3, sticky="nsew", padx=10, pady=5)
        button4.grid(column=2, row=3, sticky="nsew", padx=10, pady=5)

        buttonIM.grid(column=3, row=2, sticky="nsew", padx=10, pady=5)
        buttonNL.grid(column=3, row=3, sticky="nsew", padx=10, pady=5)
        buttonNM.grid(column=3, row=4, sticky="nsew", padx=10, pady=5)

        buttonToIM.grid(column=4, row=2, sticky="nsew", padx=10, pady=5)
        buttonToNL.grid(column=4, row=3, sticky="nsew", padx=10, pady=5)
        buttonToNM.grid(column=4, row=4, sticky="nsew", padx=10, pady=5)

        spinbox3.grid(column=1, row=4, sticky="nsew", padx=10, pady=5)
        button3b.grid(column=1, row=5, padx=10, pady=5)

        menuProj4.pack(fill=Y)

    #################### POJECT 5 #########################
    
    def SelectBasicFlowNetowrk(self, numberOfLayers=2):
        isCapacity= bool(self.checkP5capacity.get())
        isFlow= bool(self.checkP5flow.get())

        self.ClearCanvas()
        self.graph = Graph(directed=True, isNetwork=True)
        if(self.graph.FillFlowNetwork(self.canvas, numberOfLayers)):
            self.Draw(self.graph, isNetwork=True, isCapacity=isCapacity, isFlow=isFlow, numberOfLayers=numberOfLayers)
        

    def SelectFindMaximumFlow(self):
        isCapacity = bool(self.checkP5capacity.get())
        isFlow= bool(self.checkP5flow.get())

        self.ClearCanvas()
        residualNet = self.graph.FordFulkersonAlgorithm()
        numberOfLayers = GetNumberOfLayers(self.graph) - 1
        self.Draw(residualNet, isNetwork=True, isCapacity=isCapacity, isFlow=isFlow, numberOfLayers=numberOfLayers)


    def AddProject5Widgets(self, root):
        menuProj5 = Frame(self.tab5, width=1200, height=30)

        self.checkP5capacity = IntVar()
        checkShowCapacity5 = Checkbutton(
            menuProj5, text="Capacity on graph", variable=self.checkP5capacity)

        self.checkP5flow= IntVar()
        checkShowFlow5 = Checkbutton(
            menuProj5, text="Flow on graph", variable=self.checkP5flow)

        # 1
        label1 = Label(menuProj5, text='Task 1', foreground="red")
        label1a = Label(menuProj5, text='- number of layers',width=35)
        spinbox1a = Spinbox(menuProj5, from_=2, to=100, state="readonly")
        button1 = tk.Button(
            menuProj5, width=35,  text="Generate flow network", command=lambda: self.SelectBasicFlowNetowrk(int(spinbox1a.get())))

        # 2
        label2 = Label(menuProj5, text='Task 2', foreground="red")
        button2 = Button(
            menuProj5, width=35, text="Find maximum flow", command=lambda: self.SelectFindMaximumFlow())

        # row 0
        label1.grid(column=0, row=0, padx=10, pady=5)
        label2.grid(column=2, row=0, padx=10, pady=5)

        # row 1
        spinbox1a.grid(column=0, row=1, sticky="nsew", padx=10, pady=5)
        label1a.grid(column=1, row=1, sticky="w")
        button2.grid(column=2, row=1, sticky="nsew", padx=10, pady=5)
        checkShowCapacity5.grid(column=3, row=1, sticky="nsew", padx=10, pady=5)

        # row 2
        button1.grid(column=0, row=2, sticky="nsew", padx=10, pady=5)
        checkShowFlow5.grid(column=3, row=2, sticky="nsew", padx=10, pady=5)

        menuProj5.pack(fill=Y)
