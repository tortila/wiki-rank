import numpy as np
import networkx as nx
class Traverser:

    def __init__(self, adjacency_matrix, N1):
        self.unreachable, pred = self.get_unreachable(adjacency_matrix, 0)
        print "Traverser: \t unreachable nodes calculated"
        self.paths = self.get_shortest_paths(adjacency_matrix, N1)
        print "Traverser: \t shortest paths calculated"
        self.diameter = len(max(self.paths, key = len))
        print "Traverser: \t diameter calculated"

    # computes a list of nodes unreachable from N1
    def get_unreachable(self, G, start):
        visited = [False] * G.shape[0]
        prev = [-1] * G.shape[0]
        queue = []
        paths = [[]]
        queue.append(start)
        while queue:
            v = queue.pop(0)
            if not visited[v]:
                visited[v] = True
                neighbours = np.ravel(np.nonzero(G[v]))
                for neighbor in neighbours:
                    prev[neighbor] = v
                    queue.append(neighbor)
        prev[start] = -1
        return [i for i, elem in enumerate(visited) if not elem], prev

    # computes the number of shortest paths from N1 to N2
    def get_shortest(self, G, N1, dest):
        return np.linalg.matrix_power(G, self.diameter)[dest, N1]

    # computes shortest paths from N1 to all other reachable nodes
    def get_shortest_paths(self, A, N1):
        G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
        paths = [[]] * A.shape[0]
        for i in range(A.shape[0]):
            paths[i] = [] if i in self.unreachable else nx.dijkstra_path(G, N1, i)
            paths[i].pop(0)
        paths[N1] = []
        return paths
