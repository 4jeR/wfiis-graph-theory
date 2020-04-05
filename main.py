from tkinter import *
from tkinter.ttk import *
import proj_1.guiProj1 as GP1
from graph import *


def main():
    root = Tk()
    root.title("WARTOWNICY: Grafy - projekty!")
    root.geometry("1400x900")
    root.minsize(1400, 900)
    addMenuOfProjects(root)

    canvas = tk.Canvas(root, width=1200, height=800, bg="blue")
    canvas.pack(fill=X, padx=10, pady=10)

    v = Graph(canvas)

    # v.IM_to_NM("examples/incidence_matrix.txt")
    # v.IM_to_NL("examples/incidence_matrix.txt")
    # v.NL_to_NM("examples/neighbour_list.txt")
    # v.NL_to_IM("examples/neighbour_list.txt")
    # v.NM_to_IM("examples/neighbour_matrix.txt")
    # v.NM_to_NL("examples/neighbour_matrix.txt")
    v.Draw()

    root.update()
    root.mainloop()


def addMenuOfProjects(root):
    allTabs = Notebook(root)
    tab1 = Frame(allTabs)
    tab2 = Frame(allTabs)
    tab3 = Frame(allTabs)
    tab4 = Frame(allTabs)
    tab5 = Frame(allTabs)
    tab6 = Frame(allTabs)

    allTabs.add(tab1, text="Projekt 1")
    allTabs.add(tab2, text="Projekt 2")
    allTabs.add(tab3, text="Projekt 3")
    allTabs.add(tab4, text="Projekt 4")
    allTabs.add(tab5, text="Projekt 5")
    allTabs.add(tab6, text="Projekt 6")

    GP1.addProject1(tab1)
    # GUI.addProject2(self)
    # GUI.addProject3(self)
    # GUI.addProject4(self)
    # GUI.addProject5(self)
    # GUI.addProject6(self)

    allTabs.pack(expand=1, fill='both')


if __name__ == '__main__':
    main()
