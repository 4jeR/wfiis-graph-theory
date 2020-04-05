# [filename]       | [meaning of tuple: rows,cols]
#  ----------------|-------------------------------------------
# neighbour_matrix | rows,cols = node count
# incidence_matrix | rows,cols = node count, connections count


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


# for no-diredted graph Adjacency Matrix == symetric matrix
def isNoDiredtedAdjacencyMatrix(filename):
    mat, rows, cols = FileToMatrix(filename)
    N = rows
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != mat[j][i]):
                return False
    return True


# def isNeighbourList():

# def isIncidenceMatrix():
