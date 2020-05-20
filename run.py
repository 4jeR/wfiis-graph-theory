from graph import *


graph = Graph()

graph.FillFromCoordinatesFile("./examples", "input.dat")

graph.PrintGraph()

graph.PrintEdgesWithWeights()

cycle = graph.AnnealingAlgorithm()

print(cycle)