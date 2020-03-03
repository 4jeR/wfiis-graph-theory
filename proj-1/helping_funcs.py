def GetFileRowsCols(self, filename):
    f = open(filename, "r") 
    rows = len(f.read().split("\n"))
    f.seek(0)
    line = str(f.readline()).split(" ")
    cols = len(line)
    f.seek(0)
    
    # print("{}x{}".format(rows, cols))
    return f,rows,cols