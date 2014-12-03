import numpy as np

# damping factor
ALPHA = 0.85
# maximum number of iterations
MAX_ITER = 1

class PageRanker:

    def __init__(self, matrix, method):
        self.size = matrix.shape[1]
        self.x_ranks = np.zeros((self.size, 1), dtype='float64')
        self.k_out = self.get_k_out(matrix)
        print "PageRanker: \t k_out vector calculated!"

        if method == "EV":
            self.x_ranks = self.solve_eigenvector(matrix)
        else:
            self.x_ranks = self.solve_linear(matrix)

        print "PageRanker: \t x vector calculated!"

    def get_k_out(self, matrix):
        return np.reshape(map(sum, zip(*matrix)), (self.size, 1))

    def get_normalized_matrix(self, matrix):
        A = np.ndarray((self.size, self.size))
        for i in range(self.size):
            A[:, i] = matrix[:, i] / float(self.k_out[i, 0]) if matrix[:, i].sum() != 0 else 1 / float(self.size)
        return A

    def solve_linear(self, matrix):
        C = np.eye(self.size, self.size) - ALPHA * self.get_normalized_matrix(matrix)
        b = np.array([1] * self.size, dtype = 'float64') / self.size
        return np.reshape(np.linalg.solve(C, b), (self.size, 1))

    def get_google_matrix(self, normalized_matrix):
        S = np.ones((self.size, self.size)) / self.size
        return ALPHA * normalized_matrix + (1 - ALPHA) * S

    def solve_eigenvector(self, matrix):
        google_matrix = self.get_google_matrix(self.get_normalized_matrix(matrix))
        _, vectors = np.linalg.eig(google_matrix)
        return np.reshape(np.absolute(np.real(vectors[:self.size, 0]) / np.linalg.norm(vectors[:self.size, 0], 1)), (self.size, 1))
