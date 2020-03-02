import tkinter as tk


class Graph:
    def __init__(self, canvas, nodes = []):
        self.nodes = [n for n in nodes]
        self.n = len(nodes) if nodes != None else 0
        self.canvas = canvas
    
    # bez rysowania, 
    def AddNode(self, node):
        self.nodes.append(node)
        self.n += 1 
    
    # bez rysowania 
    def RemoveNode(self, indx):
        new_nodes = [self.nodes[i] for i in range(len(self.nodes)) if i != indx]
        self.nodes = [n for n in new_nodes]
    
    #do testow do konsoli
    def PrintGraph(self):
        i = 0
        for node in self.nodes:
            node.Print(i)
            i += 1
        print("Size of graph: {}.".format(self.n))
        
    #todo
    def Connect(self, begin_node, end_node):
        pass

    # dla kazdego Node woła jego metode Draw
    def Draw(self, canvas):
        for n in self.nodes:
            n.Draw(canvas)

# klasa reprezentujaca wierzcholek, 
class Node:
    def __init__(self, value, x = 0, y = 0, r = 30):
        self.value = value
        self.x = x
        self.y = y 
        self.r = r

    #do testow wypisywania na konsole
    def Print(self, idx):
        print("Node {}, value -> {}".format(idx, self.value))


    # metoda ktora rysuje obecny wierzcholek na glownym canvasie

    def Draw(self, canvas): #center coordinates, radius
        x0 = self.x - self.r
        y0 = self.y - self.r
        x1 = self.x + self.r
        y1 = self.y + self.r
        return canvas.create_oval(x0, y0, x1, y1)
    

        