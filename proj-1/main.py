from graph import *


if __name__ == '__main__':

    root = tk.Tk()
    root.title("Grafy - projekt 1")
    canvas = tk.Canvas(root, width=1200, height=900)
    canvas.pack()

    v = Graph(canvas)

    v.NM_to_NL(canvas, "neighbour_matrix.txt")     
    v.PrintGraph()

    v.Draw(canvas)



    root.update()






    root.mainloop()



