import numpy as np

class Traverser:

    def __init__(self, adjacency_matrix, N1):
        self.unreachable, pred = self.get_unreachable(adjacency_matrix, 0)
        print "Traverser: \t unreachable nodes calculated"
        self.paths = [[]] * adjacency_matrix.shape[0]
        for i in range(adjacency_matrix.shape[0]):
            print "Path:", i, "\t/", adjacency_matrix.shape[0]
            self.paths[i] = [] if i in self.unreachable else self.bfs(adjacency_matrix, N1, i)
        print "Traverser: \t shortest paths calculated"
        self.diameter = len(max(self.paths, key = len))
        print "Traverser: \t diameter calculated"


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

    def report_paths(self, start, predecessors):
        paths = [[]] * len(predecessors)
        for current in range(len(predecessors)):
            if current in self.unreachable or current == start:
                continue
            print "\t calculating path to: \t", current, "with pred:", predecessors[current],
            current_path = []
            i = current
            while predecessors[current] != -1:
                if predecessors[current] != start:
                    current = predecessors[current]
                else:
                    break # break while
                current_path.insert(0, current)

            paths[i] = current_path
            print i, paths[i]
        return paths


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

    def find_all_shortest_paths(self, G, N1, dest):
        path  = []
        paths = []
        queue = [(N1, dest, path)]
        while queue:
            N1, dest, path = queue.pop()
            path = path + [N1]
            if N1 == dest and path not in paths and len(path) - 1 == self.diameter:
                paths.append(path)
            for node in G[N1]:
                if node not in path:
                    queue.append((node, dest, path))
        return paths