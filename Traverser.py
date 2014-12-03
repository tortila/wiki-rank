import numpy as np

class Traverser:

    def __init__(self, adjacency_matrix, N1):
        self.unreachable = self.bfs1(adjacency_matrix, N1)
        print "Traverser: \t unreachable nodes calculated"
        self.paths = [False] * adjacency_matrix.shape[0]
        for i in range(adjacency_matrix.shape[0]):
            print i, " \t / ", adjacency_matrix.shape[0]
            self.paths[i] = [x + 1 for x in self.bfs(adjacency_matrix, N1, i)] if i not in self.unreachable else []
        print "Traverser: \t shortest paths calculated"
        self.diameter = len(max(self.paths, key = len))
        print "Traverser: \t diameter calculated"

    def bfs1(self, G, start):
        visited = [False] * G.shape[0]
        queue = []
        queue.append(start)
        while queue:
            v = queue.pop(0)
            if not visited[v]:
                visited[v] = True
                neighbours = np.ravel(np.nonzero(G[v]))
                for neighbor in neighbours:
                    queue.append(neighbor)
        return [i for i, elem in enumerate(visited) if not elem]

    def bfs(self, G, N1, dest):
        queue = []
        queue.append([N1])
        while queue:
            # get the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            # path found
            if node == dest:
                path.pop(0)
                return path
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            neighbours = np.ravel(np.nonzero(G[node]))
            for adjacent in neighbours:
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)