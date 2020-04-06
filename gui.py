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

    # add only widgetsfor 1 projects
    def ClearCanvas(self):
        self.canvas.delete("all")

    def Draw(self, graph, inCircle=False):
        self.ClearCanvas()
        if inCircle:
            self.DrawCircleTrace(graph)
        for e in graph.edges:
            e.Draw(self.canvas)
        for n in graph.nodes:
            n.Draw(self.canvas)

    def DrawCircleTrace(self, graph):
        xmin = min([n.x for n in graph.nodes])
        ymin = min([n.y for n in graph.nodes])
        xmax = max([n.x for n in graph.nodes])
        ymax = max([n.y for n in graph.nodes])

        self.canvas.create_oval(xmin, ymin, xmax, ymax,
                                dash=(15, 20), outline='red', width=2)

    def selectIM(self, inCircle=False):
        filepath = filedialog.askopenfilename(filetypes=(
            ("Text files", "IM_*.txt"), ("all files", "*.*")))
        g = Graph()
        g.FillGraphFromIM(filepath, self.canvas, inCircle)
        self.Draw(g, inCircle)

        g.PrintNeighbourList()
        g.PrintNeighbourMatrix()

    def selectNL(self, inCircle=False):
        filepath = filedialog.askopenfilename(filetypes=(
            ("Text files", "NL_*.txt"), ("all files", "*.*")))
        g = Graph()
        g.FillGraphFromNL(filepath, self.canvas, inCircle)
        self.Draw(g, inCircle)

        g.PrintIncidenceMatrix()
        g.PrintNeighbourMatrix()

    def selectNM(self, inCircle=False):
        filepath = filedialog.askopenfilename(filetypes=(
            ("Text files", "NM_*.txt"), ("all files", "*.*")))
        g = Graph()
        g.FillGraphFromNM(filepath, self.canvas, inCircle)
        self.Draw(g, inCircle)

        g.PrintIncidenceMatrix()
        g.PrintNeighbourList()

    def addProject1Widgets(self, root):
        menuProj1 = Frame(self.tab1, width=1200, height=30)

        # 1
        label1 = Label(menuProj1, text='Zadanie 1', foreground="red")
        buttonIM = Button(
            menuProj1, text="Generuj graf - macierz incydencji", command=self.selectIM)
        buttonNL = Button(
            menuProj1, text="Generuj graf - liste sąsiedztwa", command=self.selectNL)
        buttonNM = Button(
            menuProj1, text="Generuj graf - macierz sąsiedztwa", command=self.selectNM)

        # 2
        label2 = Label(menuProj1, text='Zadanie 2', foreground="red")
        buttonCircleGraphNM = Button(
            menuProj1, text="Graf Macierz sąsiedztwa - równomiernie rozłożone wierzchołki", command=lambda: self.selectNM(True))
        buttonCircleGraphIM = Button(
            menuProj1, text="Graf Macierz incydencji - równomiernie rozłożone wierzchołki", command=lambda: self.selectIM(True))
        buttonCircleGraphNL = Button(
            menuProj1, text="Graf Lista sąsiedztw - równomiernie rozłożone wierzchołki", command=lambda: self.selectNL(True))

        # 3
        label3 = Label(menuProj1, text='Zadanie 3',  foreground="red")
        labelToValues = Label(
            menuProj1, text='Podaj n - liczba węzłów oraz l - liczba krawędzi / p - liczba prawdopodobieństwa')

        labelN = Label(menuProj1, text='n: ')
        N = Spinbox(menuProj1, from_=1, to=100, width=8, state="readonly")

        labelLP = Label(menuProj1, text='l/p: ')
        LP = Spinbox(menuProj1, from_=1, to=100, width=8, state="readonly")

        # buttonRandomGraphNL = Button(
        #     menuProj1, text="Generuj graf - losowy G(n,l)", command=self.selectRandomGraphNL)

        # buttonRandomGraphNP = Button(
        #     menuProj1, text="Generuj graf - losowy G(n,p)", command=self.selectRandomGraphNP)

        label1.grid(column=1, row=0)

        buttonIM.grid(column=0, row=1, sticky="nsew")
        buttonNL.grid(column=1, row=1, sticky="nsew")
        buttonNM.grid(column=2, row=1, sticky="nsew")

        label2.grid(column=1, row=4)

        buttonCircleGraphNL.grid(column=0, row=5, sticky="nsew")
        buttonCircleGraphIM.grid(column=1, row=5, sticky="nsew")
        buttonCircleGraphNM.grid(column=2, row=5, sticky="nsew")

        label3.grid(column=1, row=6)

        labelToValues.grid(column=0, row=7, sticky="nsew")

        labelN.grid(column=0, row=8, sticky="nse")
        N.grid(column=1, row=8, sticky="nsew")

        labelLP.grid(column=0, row=9, sticky="nse")
        LP.grid(column=1, row=9, sticky="nsew")

        # buttonRandomGraphNL.grid(column=2, row=10, sticky="nsew")
        # buttonRandomGraphNP.grid(column=1, row=10, sticky="nsew")

        menuProj1.pack(fill=Y)
