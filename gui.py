from tkinter import *
from tkinter.ttk import *
from graph import *
from tkinter import filedialog
from tkinter import messagebox


class GUI:
    def __init__(self, root):
        root.title("WARTOWNICY: Grafy - projekty!")
        root.geometry("1400x900")
        root.minsize(1400, 900)

        self.canvas = Canvas(root, width=1200, height=800, bg="white")
        self.addTabs(root)
        self.addProject1Widgets(root)
        self.addProject2Widgets(root)

        self.allTabs.pack(expand=1, fill='both')
        self.canvas.pack(fill=X, padx=10, pady=10)

    def addTabs(self, root):
        self.allTabs = Notebook(root)
        self.tab1 = Frame(self.allTabs)
        self.tab2 = Frame(self.allTabs)
        self.tab3 = Frame(self.allTabs)
        self.tab4 = Frame(self.allTabs)
        self.tab5 = Frame(self.allTabs)
        self.tab6 = Frame(self.allTabs)

        self.allTabs.add(self.tab1, text="Projekt 1")
        self.allTabs.add(self.tab2, text="Projekt 2")
        self.allTabs.add(self.tab3, text="Projekt 3")
        self.allTabs.add(self.tab4, text="Projekt 4")
        self.allTabs.add(self.tab5, text="Projekt 5")
        self.allTabs.add(self.tab6, text="Projekt 6")

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

    def selectIM(self):
        filepath = filedialog.askopenfilename(filetypes=(
            ("Text files", "IM_*.txt"), ("all files", "*.*")))
        isChecked = bool(self.checkP1.get())
        g = Graph()
        g.FillGraphFromIM(filepath, self.canvas, isChecked)
        self.Draw(g, isChecked)

        g.PrintNeighbourList()
        g.PrintNeighbourMatrix()

    def selectNL(self):
        filepath = filedialog.askopenfilename(filetypes=(
            ("Text files", "NL_*.txt"), ("all files", "*.*")))
        isChecked = bool(self.checkP1.get())
        g = Graph()
        g.FillGraphFromNL(filepath, self.canvas, isChecked)
        self.Draw(g, isChecked)

        g.PrintIncidenceMatrix()
        g.PrintNeighbourMatrix()

    def selectNM(self):
        filepath = filedialog.askopenfilename(filetypes=(
            ("Text files", "NM_*.txt"), ("all files", "*.*")))
        isChecked = bool(self.checkP1.get())
        g = Graph()
        g.FillGraphFromNM(filepath, self.canvas, isChecked)
        self.Draw(g, isChecked)

        g.PrintIncidenceMatrix()
        g.PrintNeighbourList()

    def selectRandomGraphNL(self, n, l):
        g = Graph()
        isChecked = bool(self.checkP1.get())
        if(l > (n * (n-1) / 2)):
            messagebox.showerror(
                title="Błąd", message="[selectRandomGraphNL] Złe wartości argumentów")
        else:
            g.FillRandomizeGraphGNL(self.canvas, n, l, isChecked)
            self.Draw(g, isChecked)

    def selectRandomGraphNP(self, n, p):
        g = Graph()
        isChecked = bool(self.checkP1.get())
        g.FillRandomizeGraphGNP(self.canvas, n, p, isChecked)
        self.Draw(g, isChecked)

    def addProject1Widgets(self, root):
        menuProj1 = Frame(self.tab1, width=1200, height=30)

        # check if generate graph in circle
        self.checkP1 = IntVar()
        checkInCircle = Checkbutton(
            menuProj1, text="Generuj graf kołowy", variable=self.checkP1)

        # 1
        label1 = Label(menuProj1, text='Zadanie 1 / Zadanie 2',
                       foreground="red")
        buttonIM = Button(
            menuProj1, text="Generuj graf - macierz incydencji", command=self.selectIM)
        buttonNL = Button(
            menuProj1, text="Generuj graf - liste sąsiedztwa", command=self.selectNL)
        buttonNM = Button(
            menuProj1, text="Generuj graf - macierz sąsiedztwa", command=self.selectNM)

        # # 2
        # label2 = Label(menuProj1, text='Zadanie 2', foreground="red")
        # buttonCircleGraphNM = Button(
        #     menuProj1, text="Graf Macierz sąsiedztwa - równomiernie rozłożone wierzchołki", command=lambda: self.selectNM(True))
        # buttonCircleGraphIM = Button(
        #     menuProj1, text="Graf Macierz incydencji - równomiernie rozłożone wierzchołki", command=lambda: self.selectIM(True))
        # buttonCircleGraphNL = Button(
        #     menuProj1, text="Graf Lista sąsiedztw - równomiernie rozłożone wierzchołki", command=lambda: self.selectNL(True))

        # 3
        label3 = Label(menuProj1, text='Zadanie 3',  foreground="red")
        labelToValues = Label(
            menuProj1, text='Podaj: ')
        labelToValuesA = Label(
            menuProj1, text='n - liczba węzłów oraz')
        labelToValuesB = Label(
            menuProj1, text='l - liczba krawędzi')
        labelToValuesC = Label(
            menuProj1, text='p - prawdopodobieństwo połączenia (wart. %)')

        labelN = Label(menuProj1, text='n: ')
        N = Spinbox(menuProj1, from_=0, to=200, width=8, state="readonly")

        labelLP = Label(menuProj1, text='l/p: ')
        LP = Spinbox(menuProj1, from_=0, to=100, width=8, state="readonly")

        buttonRandomGraphNL = Button(
            menuProj1, text="Generuj graf - losowy G(n,l)", command=lambda: self.selectRandomGraphNL(int(N.get()), int(LP.get())))

        buttonRandomGraphNP = Button(
            menuProj1, text="Generuj graf - losowy G(n,p)", command=lambda: self.selectRandomGraphNP(int(N.get()), float(int(LP.get()))/100.0))

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

    def selectLogicSeq(self):
        # filepath first letters should by LS == Logical Sequence
        filepath = filedialog.askopenfilename(filetypes=(
            ("Text files", "LS_*.txt"), ("all files", "*.*")))
        g = Graph()
        isChecked = bool(self.checkP2.get())

        if g.FillFromLogicSequence(filepath, self.canvas, inCircle=isChecked):
            self.Draw(g, isChecked)
        else:
            messagebox.showerror(
                title="Błąd", message="Podana sekwencja nie jest ciągiem graficznym!")

    def selectRandomGraphLogicalSeq(self, num):
        # filepath first letters should by RLS == Random Logical Sequence
        filepath = filedialog.askopenfilename(filetypes=(
            ("Text files", "RLS_*.txt"), ("all files", "*.*")))
        g = Graph()
        if(g.FillFromLogicSequence(filepath, self.canvas)):
            if(g.EdgesRandomization(num)):
                self.Draw(g)
            else:
                messagebox.showerror(
                    title="Błąd", message="This Graph cannot be randomized")
        else:
            messagebox.showerror(
                title="Błąd", message="Podana sekwencja nie jest ciągiem graficznym!")

    def selectFindConnectedComponent(self):
        # filepath first letters should by FCC == Find Connected Component
        filepath = filedialog.askopenfilename(filetypes=(
            ("Text files", "FCC_*.txt"), ("all files", "*.*")))
        g = Graph()
        self.ClearCanvas()
        info = g.FillComponentsAndDraw(
            filepath, self.canvas, True)  # info is string type
        messagebox.showinfo(
            title="Informacja", message=info)

    def selectEulerGraph(self, num):
        g = Graph()

        ######################
        # TO DO
        #
        # in class Graph
        #
        # NEW_FUNCTION(canvas, num ......)
        # self.canvas -> current canvas.winfo_width()/canvas.winfo_height()
        # num -> number of nodes
        #
        # NEW_FUNCTION should
        #   return string
        #      e.g.
        #       "[1 - 2 - 3 - 1 - 4 - 2 - 5 - 1 - 7 - 4 - 3 - 6 - 2 - 8 - 1]"
        #   if num = 0 -> draw numbers od nodes
        #   fill graph
        #
        ######################

        # info = g.NEW_FUNCTION(self.canvas, num ...)
        # self.Draw(g)
        # messagebox.showinfo(title="Informacja", message=info)

    def selectKReguralGraph(self, n, k):
        g = Graph()
        isChecked = bool(self.checkP2.get())
        if (g.FillKReguralGraph(self.canvas, n, k, isChecked)):
            self.Draw(g)
        else:
            messagebox.showerror(
                title="Błąd", message="Podane wartości nie pozwalają na stworzenie grafu {}-regularnego!".format(k))

    def selectCheckHamiltonGraph(self, tof):
        g = Graph()
        if(tof):
            filepath = filedialog.askopenfilename(filetypes=(
                ("Text files", "HG_*.txt"), ("all files", "*.*")))
        else:
            filepath = ""

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
        #          "Podany graf: [sekwencja logiczna OR macierz sąsiedztwa OR ...]
        #           Jest grafem hamiltonowskim
        #           Cykl Hamiltona :[1 - 2 - 3 - 7 - 4 - 6 - 8 - 5 - 1]"
        #
        #       2) if graph is not hamilton's graph
        #          "Podany graf: [sekwencja logiczna OR macierz sąsiedztwa OR ...]
        #           Nie jest grafem hamiltonowskim"
        #
        ######################

        # info = g.NEW_FUNCTION(tof, filepath ..)
        # messagebox.showinfo(
        #        title="Informacja", message=info)

    def addProject2Widgets(self, root):
        menuProj2 = Frame(self.tab2, width=1200, height=30)

        # check if generate graph in circle
        self.checkP2 = IntVar()
        checkInCircle2 = Checkbutton(
            menuProj2, text="Generuj graf kołowy", variable=self.checkP2)

        # 1
        label1 = Label(menuProj2, text='Zadanie 1',
                       foreground="red")
        button1 = Button(
            menuProj2, text="Generuj graf - z ciągu graficznego", command=lambda: self.selectLogicSeq())

        # 2
        label2 = Label(menuProj2, text='Zadanie 2', foreground="red")
        label2a = Label(menuProj2, text='Liczba żadanych randomizacji')
        spinbox2a = Spinbox(menuProj2, from_=0, to=100,
                            width=8, state="readonly")
        button2 = Button(
            menuProj2, text="Generuj graf - randomizuj zadane wierzchołki", command=lambda: self.selectRandomGraphLogicalSeq(int(spinbox2a.get())))

        # 3
        label3 = Label(menuProj2, text='Zadanie 3', foreground="red")
        button3 = Button(
            menuProj2, text="Generuj graf - znajdź największą wspólną składową grafu", command=self.selectFindConnectedComponent)

        # 4
        label4 = Label(menuProj2, text='Zadanie 4', foreground="red")
        label4a = Label(
            menuProj2, text='Liczba wierzchołków (dla n=0 losowa ilość)')
        spinbox4a = Spinbox(menuProj2, from_=0, to=100,
                            width=8, state="readonly")
        button4 = Button(
            menuProj2, text="Generuj graf - graf eulerowski z cyklem Eulera", command=lambda: self.selectEulerGraph(int(spinbox4a.get())))

        # 5
        label5 = Label(menuProj2, text='Zadanie 5', foreground="red")
        label5a = Label(
            menuProj2, text='Podaj jako 1. liczbe wierzchołków oraz 2. stopień wierzchołków')
        spinbox5b = Spinbox(menuProj2, from_=0, to=100,
                            width=8, state="readonly")
        spinbox5c = Spinbox(menuProj2, from_=0, to=100,
                            width=8, state="readonly")
        button5 = Button(
            menuProj2, text="Generuj graf - losowy k-reguralny", command=lambda: self.selectKReguralGraph(int(spinbox5b.get()), int(spinbox5c.get())))

        # 6
        label6 = Label(menuProj2, text='Zadanie 6', foreground="red")
        button6a = Button(
            menuProj2, text="Sprawdź, czy graf jest hamiltonowski - z pliku", command=lambda: self.selectCheckHamiltonGraph(True))
        button6b = Button(
            menuProj2, text="Sprawdź, czy graf jest hamiltonowski - losowy", command=lambda: self.selectCheckHamiltonGraph(False))

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
