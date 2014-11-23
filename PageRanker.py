import numpy as np

ALPHA = 0.85

class PageRanker:

    def __init__(self, matrix):
        self.size = len(matrix)
        self.k_out = np.zeros((self.size, 1), dtype=int)
        self.x_ranks = np.zeros((self.size, 1), dtype=float)
        self.get_k_out(matrix)
        print "PageRanker: \t k_out vector calculated!"
        self.get_ranks(matrix)
        print "PageRanker: \t x vector calculated!"

    def get_k_out(self, matrix):
        # calculate sum over columns
        for i in range(0, len(matrix)):
            self.k_out[i, 0] = matrix[i].sum()

    def get_ranks(self, matrix):
        for i in range(0, self.size):
            temp_sum = 0
            for j in range(0, self.size):
                if self.k_out[j, 0] == 0:
                    continue
                else:
                    temp_sum += matrix[i, j] * self.x_ranks[j, 0] / float(self.k_out[j, 0])
            self.x_ranks[i, 0] = ALPHA * temp_sum + 1 / float(self.size)
