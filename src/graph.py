# NAMA  : SAUL SAYERS
# NIM   : 13520094
# TASK 7 SELEKSI ASISTEN IRK

# FILE INI MERUPAKAN FILE UNTUK CLASS GRAPH

import os.path
import time
from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.Nodes = []
        self.Edges = {}
        self.Solution = []
        self.Iterations = 0
        self.ExecTime = 0

    def readFile(self):
        """ This method is used to fill the Nodes
        and Edges of the Graph from a file.
        """       

        while True:  # Looping until filename exists
            filename = input("Input filename here (dengan .txt): ")
            path = "test/" + filename
            if (os.path.isfile(path)):
                break
            else :
                print("Filename doesnt exist! Please re-input filename.")

        file = open(path)
        mode = 0
        for line in file:
            if "NODE:" in line:
                mode = 0
            elif "EDGE:" in line:
                mode = 1
                for i in range(len(self.Nodes)):
                    self.Edges[self.Nodes[i]] = []
            elif line == "" or line == "\n":
                pass
            elif mode == 0:
                self.Nodes.append(line.strip())
            elif mode == 1:
                edge = line.strip().split()
                self.Edges[edge[0]].append([edge[1],edge[2]])

    def Djiktra(self, start, end):
        """ This method is used to find the shortest path
        from start to end using djiktra algorithm.
        """
        waktuawal = time.time()
        self.Iterations = 0
        visited = [] # List of visited nodes
        shortest = {} # Dictionary of shortest path and the node to get it
        for node in self.Nodes:
            shortest[node] = [-1, '-']
        shortest[start] = [0, '-'] # Set the start node to 0

        queue = PriorityQueue()
        queue.put((0,start)) # Put the start node into the queue

        while not queue.empty() : # Loop until the queue is empty
            currentnode = queue.get()[1]
            visited.append(currentnode)
            self.Iterations = self.Iterations + 1

            for edge in self.Edges[currentnode]: # Loop through all the edges of the current node
                if edge[0] not in visited: 
                    if shortest[edge[0]][0] == -1 or shortest[edge[0]][0] > shortest[currentnode][0] + int(edge[1]): # If the shortest path is not found or the current path is shorter than the shortest path
                        shortest[edge[0]] = [shortest[currentnode][0] + int(edge[1]), currentnode] # Set the shortest path to the current path + edge weight
                    queue.put((shortest[edge[0]][0], edge[0]))

        if shortest[end][0] == -1:
            self.Solution = []
        else :
            self.Solution = [end]
            while shortest[self.Solution[0]][1] != '-':
                self.Solution.insert(0, shortest[self.Solution[0]][1])

        waktuakhir = time.time()
        self.ExecTime = waktuakhir - waktuawal

# INI DRIVERNYA
'''
graf = Graph()
graf.readFile()
graf.Djiktra('surabaya','semarang')
print("NODES: ", graf.Nodes)
print("EDGES: ", graf.Edges)
print("SOLUTION: ", graf.Solution)

print()
graf.readFile()
graf.Djiktra('A','F')
print("NODES: ", graf.Nodes)
print("EDGES: ", graf.Edges)
print("SOLUTION: ", graf.Solution)
'''