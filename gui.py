from tkinter import *
from tkinter.ttk import *
from graph import *
from tkinter import filedialog
from tkinter import messagebox


class GUI:
    def __init__(self, root):
        root.title("WARTOWNICY: wfiis-graph-theory")
        root.geometry("1400x900")
        root.minsize(1400, 900)

        self.canvas = Canvas(root, width=1200, height=800, bg="white")
        self.AddTabs(root)
        self.AddProject1Widgets(root)
        self.AddProject2Widgets(root)

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

    def Draw(self, graph, inCircle=False, color="#aaa"):
        self.ClearCanvas()
        if inCircle:
            self.DrawCircleTrace(graph)
        for e in graph.edges:
            e.Draw(self.canvas)
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
        g.PrintAdjacencyMatrix()

    def SelectAM(self):
        filepath = filedialog.askopenfilename(initialdir='examples', filetypes=(
            ("Text files", "AM_*.txt"), ("all files", "*.*")))
        isChecked = bool(self.checkP1.get())
        g = Graph()
        g.FillGraphFromAM(filepath, self.canvas, isChecked)
        self.Draw(g, isChecked)

        g.PrintAdjacencyMatrix()
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
        # filepath first letters should by LS == Logical Sequence
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
        g = Graph()
        if(tof):
            filepath = filedialog.askopenfilename(initialdir='examples', filetypes=(
                ("Text files", "HG_*.txt"), ("all files", "*.*")))
        else:
            filepath = None
        is_checked = bool(self.checkP2.get())
        g.CheckIfIsHamiltonGraph(self.canvas, filepath, in_circle=is_checked)
        ######################
        # TO DO
        #
        # in class Graph
        #
        # NEW_FUNCTION(tof, filepath ......)
        # tof -> boolean; if True check from file ; if False genetare random sequence and check
        # filepath -> name of path with example sequence; "HG_*.txt" or empty string
        #
        # NEW_FUNCTION should
        #   return info
        #   e.g.
        #       1) if graph is hamilton's graph
        #          "Podany graf: [sekwencja logiczna OR adjacency matrix OR ...]
        #           Jest grafem hamiltonowskim
        #           Cykl Hamiltona :[1 - 2 - 3 - 7 - 4 - 6 - 8 - 5 - 1]"
        #
        #       2) if graph is not hamilton's graph
        #          "Podany graf: [sekwencja logiczna OR adjacency matrix OR ...]
        #           Nie jest grafem hamiltonowskim"
        #
        ######################

        # info = g.NEW_FUNCTION(tof, filepath ..)
        # messagebox.showinfo(
        #        title="Informacja", message=info)

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
