from graph import *
import random


if __name__ == '__main__':

    # Tworzenie okna, 1200x900
    root = tk.Tk()
    root.title("Grafy - projekt 1")
    canvas = tk.Canvas(root, width=1200, height=900)
    canvas.pack()

    v = Graph(canvas)
    for i in range(10):
        v.AddNode(Node(i*i + 2, random.randint(100,300) * i, random.randint(100,200) * i))


    v.PrintGraph()    
    v.Draw(canvas)



    # glowna petla okna
    # caly kod idzie powyzej tej linijki
    root.mainloop()



