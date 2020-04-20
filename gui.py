from tkinter import *
from tkinter.ttk import *
from graph import *
from tkinter import filedialog
from tkinter import messagebox
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

    def Draw(self, graph, inCircle=False, color="#aaa", weighted=False):
        self.ClearCanvas()
        if inCircle:
            self.DrawCircleTrace(graph)
        for e in graph.edges:
            e.Draw(self.canvas, weighted)
        for n in graph.nodes:
            n.Draw(self.canvas, color)

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
            title="Informacja", message=info)

    def SelectEuleranGraph(self, num_of_nodes=0):
        """
        Invokes function that generates random Euler Graph and then finds Euler Circuit of that graph.

        :param num_of_nodes: Number of nodes of a graph to be randomly generated.
        :return: None
        """
        g = Graph()
        is_checked = bool(self.checkP2.get())
        euler_circuit = g.GetEulersCycleFromRandomEulerGraph(
            self.canvas, num_of_nodes, in_circle=is_checked)
        self.Draw(g, inCircle=is_checked)
        messagebox.showinfo(
            title="Informacja", message="[SelectEuleranGraph] Found Euler Cycle : {}".format(euler_circuit))

    def SelectKReguralGraph(self, n, k):
        g = Graph()
        isChecked = bool(self.checkP2.get())
        if (g.FillKReguralGraph(self.canvas, n, k, isChecked)):
            self.Draw(g)
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
        g.PrintGraph()
        self.Draw(g)

        if hamilton_cycle:
            messagebox.showinfo(title="Informacja", message="[SelectEuleranGraph]  Found hamilton cycle: {}".format(hamilton_cycle))
        else:
            messagebox.showinfo(title="Informacja", message="[SelectEuleranGraph]  Given graph is not Hamilton graph: {}".format(hamilton_cycle))

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
        # TO DO
        # check is connected graph
        self.graph.ResetGraph()
        isCheckedCircle = bool(self.checkP3.get())
        isWeighted = bool(self.checkP3weighted.get())
        if(fromFile == True):  # fromFile True for generate graph from file
            filepath = filedialog.askopenfilename(initialdir='examples', filetypes=(
                ("Text files", "IM_*.txt"), ("all files", "*.*")))
            self.graph.FillGraphFromIM(filepath, self.canvas, isCheckedCircle)
            
            self.Draw(self.graph, inCircle=isCheckedCircle,
                      weighted=isWeighted)
        else:       # fromFile False for generate random graph
            if(l > (n * (n-1) / 2)):
                messagebox.showerror(
                    title="Błąd", message="[SelectBasicGraph] Invalid arguments' values.")
            else:
                self.graph.FillRandomizeGraphGNL(
                    self.canvas, n, l, isCheckedCircle)
                self.Draw(self.graph, inCircle=isCheckedCircle,
                          weighted=isWeighted)

    def SelectAddWeights(self):
        isCheckedCircle = bool(self.checkP3.get())
        isWeighted = bool(self.checkP3weighted.get())
        SetRandomWagesOfEdges(self.graph, 1, 10)
        self.Draw(self.graph, inCircle=isCheckedCircle,
                  weighted=isWeighted)

    def SelectTheShortestPath(self, numOfVertex=1):
        pass
        ######################
        # TO DO
        #
        # NEW_FUNCTION(numOfVertex)
        # numOfVertex -> number of vertex which we are looking for the shortest path
        #
        # NEW_FUNCTION should
        #   return string == info
        #   e.g.
        # "START : s = 1
        # 2 d (1) = 0 == > [1]
        # 3 d (2) = 3 == > [1 - 2]
        # 4 d (3) = 2 == > [1 - 3]
        # 5 d (4) = 5 == > [1 - 2 - 4]
        # 6 d (5) = 7 == > [1 - 2 - 5]
        # 7 d (6) = 10 == > [1 - 2 - 5 - 8 - 6]
        # 8 d (7) = 8 == > [1 - 2 - 4 - 7]
        # 9 d (8) = 9 == > [1 - 2 - 5 - 8]
        # 10 d (9) = 12 == > [1 - 2 - 5 - 8 - 6 - 9]
        # 11 d (10) = 13 == > [1 - 2 - 4 - 7 - 10]
        # 12 d (11) = 14 == > [1 - 2 - 5 - 8 - 6 - 9 - 11]
        # 13 d (12) = 17 == > [1 - 2 - 5 - 8 - 6 - 9 - 11 - 12]"
        #
        ######################

        # info = self.graph.NEW_FUNCTION(numOfVertex)
        # messagebox.showinfo(
        #        title="Informacja", message=info)

    def SelectDistanceMatrix(self):
        pass
        ######################
        # TO DO
        #
        # NEW_FUNCTION()
        #
        # NEW_FUNCTION should
        #   return string == info
        #   e.g.
        # "0 3 2 5 7 10 8 9 12 13 14 17
        # 2 3 0 5 2 4 7 5 6 9 10 11 14
        # 3 2 5 0 7 6 9 7 8 11 12 13 16
        # 4 5 2 7 0 4 7 3 6 9 8 11 13
        # 5 7 4 6 4 0 3 1 2 5 6 7 10
        # 6 10 7 9 7 3 0 4 1 2 6 4 7
        # 7 8 5 7 3 1 4 0 3 6 5 8 10
        # 8 9 6 8 6 2 1 3 0 3 5 5 8
        # 9 12 9 11 9 5 2 6 3 0 8 2 5
        # 10 13 10 12 8 6 6 5 5 8 0 8 5
        # 11 14 11 13 11 7 4 8 5 2 8 0 3
        # 12 17 14 16 13 10 7 10 8 5 5 3 0"
        #
        ######################

        # info = self.graph.NEW_FUNCTION()
        # messagebox.showinfo(
        #        title="Informacja", message=info)

    def SelectFindCentralVertex(self):
        pass
        ######################
        # TO DO
        #
        # NEW_FUNCTION()
        #
        # NEW_FUNCTION should
        #   return string == info
        #   e.g.
        # "Centrum = 5 ( suma odleglosci : 55)"
        #
        ######################

        # info = self.graph.NEW_FUNCTION()
        # messagebox.showinfo(
        #        title="Informacja", message=info)

    def SelectFindMinimaxVertex(self):
        pass
        ######################
        # TO DO
        #
        # NEW_FUNCTION()
        #
        # NEW_FUNCTION should
        #   return string == info
        #   e.g.
        # "Centrum minimax = 8 ( odleglosc od najdalszego : 9)"
        #
        ######################

        # info = self.graph.NEW_FUNCTION()
        # messagebox.showinfo(
        #        title="Informacja", message=info)

    def SelectFindMinSpanningTree(self):
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

        # check if generate graph draw with wages
        self.checkP3weighted = IntVar()
        checkShowWages3 = Checkbutton(
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
            menuProj3, text="Find central vertex", command=lambda: self.SelectFindCentralVertex)
        button4b = Button(
            menuProj3, text="Find minimax vertex", command=lambda: self.SelectFindMinimaxVertex)

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
        checkShowWages3.grid(column=3, row=1, sticky="nsew", padx=10, pady=5)

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
