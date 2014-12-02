import numpy as np

# damping factor
ALPHA = 0.85
# maximum number of iterations
MAX_ITER = 1

class PageRanker:

    def __init__(self, matrix):
        self.size = matrix.shape[1]
        self.x_ranks = np.zeros((self.size, 1), dtype=float)
        self.k_out = self.get_k_out(matrix)
        print "PageRanker: \t k_out vector calculated!"
        self.x_ranks = self.get_max_eigenvector(matrix)
        print "PageRanker: \t x vector calculated!"
        print self.x_ranks

    def get_k_out(self, matrix):
        return np.reshape(map(sum, zip(*np.copy(matrix))), (self.size, 1))

    def get_normalized_matrix(self, matrix):
        A = np.ndarray((self.size, self.size))
        for i in range(self.size):
            for j in range(self.size):
                A[i, j] = matrix[i, j] / float(self.k_out[j, 0]) if matrix[i, j] != 0 else 0
        return A

    def get_google_matrix(self, normalized_matrix):
        S = np.ones((self.size, self.size)) / self.size
        return ALPHA * normalized_matrix + (1 - ALPHA) * S

    def get_max_eigenvector(self, matrix):
        google_matrix = self.get_google_matrix(self.get_normalized_matrix(matrix))
        _, vectors = np.linalg.eig(google_matrix)
        return np.reshape(np.absolute(np.real(vectors[:self.size, 0]) / np.linalg.norm(vectors[:self.size, 0], 1)), (self.size, 1))

    def solve_linear_equations(self, matrix):
        C = np.eye(self.size, self.size) - ALPHA * self.get_normalized_matrix(matrix)
        b = np.array([1] * self.size, dtype = 'float64') / self.size
        return np.reshape(np.linalg.solve(C, b), (self.size, 1))
