from graph import *

def main():
    root = tk.Tk()
    root.title("Grafy - projekt 1")
    canvas = tk.Canvas(root, width=1200, height=900)
    canvas.pack()

    v = Graph(canvas)
    
    # v.IM_to_NM("incidence_matrix.txt")     
    # v.IM_to_NL("incidence_matrix.txt")
    # v.NL_to_NM("neighbour_list.txt")
    # v.NL_to_IM("neighbour_list.txt")
    # v.NM_to_IM("neighbour_matrix.txt")
    # v.NM_to_NL("neighbour_matrix.txt")
    v.Draw()

    
    root.update()
    root.mainloop()
    
if __name__ == '__main__':
    main()
    