import numpy as np
import csv

DIR = "data/"
LINKS = "Links_"
TITLES = "Titles_"
FILE_TYPE = ".txt"

class Parser:

    def __init__(self, suffix):
        self.links_file = DIR + LINKS + suffix + FILE_TYPE
        self.titles_file = DIR + TITLES + suffix + FILE_TYPE
        self.links_size = self.get_links_size()
        self.links, self.size = self.link_read()
        self.titles = self.title_read()
        print "Parser: \t got", self.links_size, "pages along with", self.titles_size, "titles."
        print "Parser: \t got", self.size, "links."

    def get_links_size(self):
        max_val = 0
        with open(self.links_file, "rb") as csv_file:
            f = csv.reader(csv_file, delimiter=" ", quotechar='|')
            for line in f:
                if int(max(line)) > max_val:
                    max_val = int(max(line))
        csv_file.close()
        return max_val

    def link_read(self):
        size = (int(self.links_size), int(self.links_size))
        data = np.zeros(size, dtype = np.int)
        rows = []
        cols = []
        lines = 0
        with open(self.links_file, "rb") as csv_file:
            f = csv.reader(csv_file, delimiter=" ", quotechar='|')
            for line in f:
                lines += 1
                cols.append(int(line[0]) - 1)
                rows.append(int(line[1]) - 1)
        csv_file.close()
        data[rows, cols] = 1
        return data, lines

    def title_read(self):
        data = []
        with open(self.titles_file, "rb") as csv_file:
            f = csv.reader(csv_file, delimiter=" ", quotechar='|')
            for line in f:
                data.append(line)
        csv_file.close()
        self.titles_size = len(data)
        return data
