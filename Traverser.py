import numpy as np

class Traverser:

    def __init__(self, adjacency_matrix, N1):
        self.unreachable = self.get_unreachable_nodes(adjacency_matrix, N1)

    def get_unreachable_nodes(self, G, start):
        print G
        print start
        visited = [False] * G.shape[0]
        stack = []
        stack.append(start)
        while stack:
            v = stack.pop()
            if not visited[v]:
                print "visiting:", v
                visited[v] = True
                neighbours = np.ravel(np.nonzero(G[v]))
                print "neighbours", neighbours
                for neighbor in neighbours:
                    stack.append(neighbor)
                print "stack:", stack
        print visited
        res = [i for i, elem in enumerate(visited) if not elem]
        print res
        return res

