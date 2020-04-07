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
        # self.addProject2Widgets(root)

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

    #################### PROJECT 1 ##########################

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

    def selectRandomGraphNL(self, n, l):
        g = Graph()
        if(l > (n * (n-1) / 2)):
            messagebox.showerror(
                title="Błąd", message="[selectRandomGraphNL] Złe wartości argumentów")
        else:
            g.FillRandomizeGraphGNL(self.canvas, n, l)
            self.Draw(g)

    def selectRandomGraphNP(self, n, p):
        print(p)
        g = Graph()
        g.FillRandomizeGraphGNP(self.canvas, n, p)
        self.Draw(g)

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
            menuProj1, text='Podaj n - liczba węzłów oraz l - liczba krawędzi / p - prawdopodobieństwo połączenia')

        labelN = Label(menuProj1, text='n: ')
        N = Spinbox(menuProj1, from_=0, to=200, width=8, state="readonly")

        labelLP = Label(menuProj1, text='l/p: ')
        LP = Spinbox(menuProj1, from_=0, to=100, width=8, state="readonly")

        buttonRandomGraphNL = Button(
            menuProj1, text="Generuj graf - losowy G(n,l)", command=lambda: self.selectRandomGraphNL(int(N.get()), int(LP.get())))

        buttonRandomGraphNP = Button(
            menuProj1, text="Generuj graf - losowy G(n,p)", command=lambda: self.selectRandomGraphNP(int(N.get()), float(int(LP.get()))/100.0))

        label1.grid(column=1, row=0)

        buttonIM.grid(column=0, row=1, sticky="nsew")
        buttonNL.grid(column=1, row=1, sticky="nsew")
        buttonNM.grid(column=2, row=1, sticky="nsew")

        label2.grid(column=1, row=2)

        buttonCircleGraphNL.grid(column=0, row=3, sticky="nsew")
        buttonCircleGraphIM.grid(column=1, row=3, sticky="nsew")
        buttonCircleGraphNM.grid(column=2, row=3, sticky="nsew")

        label3.grid(column=1, row=4)

        labelToValues.grid(column=0, row=5, sticky="nsew")

        labelN.grid(column=0, row=6, sticky="nse")
        N.grid(column=1, row=6, sticky="nsew")

        labelLP.grid(column=0, row=7, sticky="nse")
        LP.grid(column=1, row=7, sticky="nsew")

        buttonRandomGraphNL.grid(column=1, row=8, sticky="nsew")
        buttonRandomGraphNP.grid(column=2, row=8, sticky="nsew")

        menuProj1.pack(fill=Y)

    #################### POJECT 2 #########################

    def addProject2Widgets(self, root):
        print()
