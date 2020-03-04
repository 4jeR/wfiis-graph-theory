# [filename]       | [meaning of tuple: rows,cols]
#  ----------------|-------------------------------------------
# neighbour_matrix | rows,cols = node count 
# neighbour_list   | rows,cols = node count, indexes of nodes connected
# incidence_matrix | rows,cols = node count, connections count

def GetFileRowsCols(self, filename):
    f = open(filename, "r")
    matrix = f.read()
    rows = len(matrix.split("\n"))
    cols = len(matrix.split("\n")[0].split(" "))
    f.seek(0)
    return f,rows,cols