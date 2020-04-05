from tkinter import *
from tkinter.ttk import *
from graph import *
from tkinter import filedialog
from tkinter import messagebox
import helping_funcs as hf


def addProject1(tab1):
    menuProj1 = Frame(tab1, width=1400, height=30)

    # 1a
    label1 = Label(menuProj1, text='Zadanie 1',
                   foreground="red")
    buttonIM = Button(
        menuProj1, text="Generuj graf - macierz incydencji", command=selectMI)
    buttonNL = Button(
        menuProj1, text="Generuj graf - liste sąsiedztwa", command=selectNL)
    buttonNM = Button(
        menuProj1, text="Generuj graf - macierz sąsiedztwa", command=selectNM)

    # 1b
    buttonNM_to_NL = Button(
        menuProj1, text="Kodowanie: Macierz sąsiedztwa -> Lista sąsiedztwa", command=selectMI)
    buttonNM_to_IM = Button(
        menuProj1, text="Kodowanie: Macierz sąsiedztwa -> Macierz incydencji", command=selectMI)

    buttonIM_to_NL = Button(
        menuProj1, text="Kodowanie: Macierz incydencji -> Lista sąsiedztwa", command=selectMI)
    buttonIM_to_NM = Button(
        menuProj1, text="Kodowanie: Macierz incydencji -> Macierz sąsiedztwa", command=selectMI)

    buttonNL_to_IM = Button(
        menuProj1, text="Kodowanie: Lista sąsiedztwa -> Macierz incydencji", command=selectMI)
    buttonNL_to_NM = Button(
        menuProj1, text="Kodowanie: Lista sąsiedztwa -> Macierz sąsiedztwa", command=selectMI)

    # 2
    label2 = Label(menuProj1, text='Zadanie 2',
                   foreground="red")
    buttonCircleGraph = Button(
        menuProj1, text="Generuj graf - równomiernie rozłożone wierzchołki", command=selectMI)

    # 3
    label3 = Label(menuProj1, text='Zadanie 3',
                   foreground="red")
    labelToValues = Label(
        menuProj1, text='Podaj n - liczba węzłów oraz l - liczba .... / p - liczba ....')

    labelN = Label(menuProj1, text='n: ')
    N = Spinbox(menuProj1, from_=0, to=100, width=8)

    labelLP = Label(menuProj1, text='l/p: ')
    LP = Spinbox(menuProj1, from_=0, to=100, width=8)

    buttonRandomGraph1 = Button(
        menuProj1, text="Generuj graf - losowy G(n,l)", command=selectMI)

    buttonRandomGraph2 = Button(
        menuProj1, text="Generuj graf - losowy G(n,p)", command=selectMI)

    # add all widgets
    label1.grid(column=1, row=0)

    buttonIM.grid(column=0, row=1, sticky="nsew")
    buttonNL.grid(column=1, row=1, sticky="nsew")
    buttonNM.grid(column=2, row=1, sticky="nsew")

    buttonNM_to_NL.grid(column=0, row=2, sticky="nsew")
    buttonNM_to_IM.grid(column=0, row=3, sticky="nsew")
    buttonIM_to_NL.grid(column=1, row=2, sticky="nsew")
    buttonIM_to_NM.grid(column=1, row=3, sticky="nsew")
    buttonNL_to_IM.grid(column=2, row=2, sticky="nsew")
    buttonNL_to_NM.grid(column=2, row=3, sticky="nsew")

    label2.grid(column=1, row=4)

    buttonCircleGraph.grid(column=1, row=5, sticky="nsew")

    label3.grid(column=1, row=6)

    labelToValues.grid(column=0, row=7, sticky="nsew")

    labelN.grid(column=0, row=8, sticky="nse")
    N.grid(column=1, row=8, sticky="nsew")

    labelLP.grid(column=0, row=9, sticky="nse")
    LP.grid(column=1, row=9, sticky="nsew")

    buttonRandomGraph1.grid(column=2, row=10, sticky="nsew")
    buttonRandomGraph2.grid(column=1, row=10, sticky="nsew")

    menuProj1.pack(fill=BOTH)


def selectMI():
    file = filedialog.askopenfilename(filetypes=(
        ("Text files", "*.txt"), ("all files", "*.*")))
    if(isNoDiredtedAdjacencyMatrix(file)):
        info = 'Przed:\n'
        info += ....
        info += 'Po:\n'
        info += ....
        messagebox.showinfo('Informacja', info)
    else:
        messagebox.showerror(
            ' Błąd ', 'Wybrany plik nie jest w formacie macierzy incydencji dla grafu nieskierowanego!!')


def selectNL():
    file = filedialog.askopenfilename(filetypes=(
        ("Text files", "*.txt"), ("all files", "*.*")))


def selectNM():
    file = filedialog.askopenfilename(filetypes=(
        ("Text files", "*.txt"), ("all files", "*.*")))
