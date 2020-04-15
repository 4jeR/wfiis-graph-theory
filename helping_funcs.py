# [filename]       | [meaning of tuple: rows,cols]
#  ----------------|-------------------------------------------
# neighbour_matrix | rows,cols = node count
# incidence_matrix | rows,cols = node count, connections count
import random


def GetFileRowsCols(self, filename):
    f = open(filename, "r")
    matrix = f.read()
    rows = len(matrix.split("\n"))
    cols = len(matrix.split("\n")[0].split(" "))
    f.seek(0)
    return f, rows, cols


def FileToMatrix(filename):
    with open(filename, 'r') as f:
        matrix = [[int(num) for num in line.split(' ')] for line in f]
    rows = len(matrix)
    cols = len(matrix[0])
    return matrix, rows, cols

def AreUnique(Samples):
    return((Samples[0].node1 != Samples[1].node1) and
           (Samples[0].node1 != Samples[1].node2) and
           (Samples[0].node2 != Samples[1].node1) and
           (Samples[0].node2 != Samples[1].node2))


def RandomizeIndex(a, b, bad_idx_list, seq):
    ok_idx = random.randint(a, b)
    while ok_idx in bad_idx_list or seq[ok_idx-1] <= 0:
        ok_idx = random.randint(a, b) 
    return ok_idx


def NodeFromIndex(graph, idx):
    for n in graph.nodes:
        if n.index == idx:
            return n
        else:
            continue
