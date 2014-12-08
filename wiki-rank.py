import numpy as np
import matplotlib.pyplot as plt
from Parser import Parser
from PageRanker import PageRanker
from Traverser import Traverser
import time
import sys

TEST = "Test"
REAL_DATA = "oligo854"
EXAMPLE = "Example"

def main():
    method = sys.argv[1] if len(sys.argv) > 1 else "LE"
    print "---\nWelcome to wiki-rank!"
    print "Using method ", method, "\n---"
    # parse text files containing links and titles
    parser = Parser(TEST)
    # start timer
    start = time.time()
    # calculate PageRank for articles
    page_rank = PageRanker(parser.links, method)
    # end timer
    end = time.time()
    print "Time elapsed:", end - start, "seconds\n---"

    # get top5 articles (rank, index and title)
    indices = get_top(page_rank.x_ranks, 5)
    top_ranks = []
    for index in indices:
        top_ranks.append((page_rank.x_ranks[index, 0], index + 1, parser.titles[index]))
    top_ranks.sort(reverse = True)
    print "Top 5 articles:"
    for item in top_ranks:
        print item

    # N1 is the index of the most popular article
    N1 = top_ranks[0][1] - 1
    print "N1:", N1 + 1, parser.titles[N1]

    traverser = Traverser(parser.links.T, N1)
    print "---\nNodes unreachable from N1:\t", len(traverser.unreachable), [(x + 1, parser.titles[x]) for x in traverser.unreachable]
    print "Diameter:", traverser.diameter
    # find all nodes that are on the diameter
    diameter_indices = [index for index, path in enumerate(traverser.paths) if len(path) == traverser.diameter]
    diameter_titles = []
    for index in diameter_indices:
        diameter_titles.append(parser.titles[index])
    print "Possible N2:\t"
    print [(x + 1, parser.titles[x]) for x in diameter_indices]
    N2_title = sorted(diameter_titles)[0]
    N2 = parser.titles.index(N2_title)
    print "Actual N2:", N2 + 1, parser.titles[N2]
    # print "All paths:", traverser.find_all_shortest_paths(parser.links, N1, N2)
    print "# of shortest paths:\t", traverser.get_shortest(parser.links, N1, N2)
    print "Shortest path from N1 to N2:\t", [(x + 1, parser.titles[x]) for x in traverser.paths[N2]]
    hist_data = [len(x) for x in traverser.paths]
    hist, bins = np.histogram(hist_data, bins = range(1, 100))
    width = 0.7
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.xlabel('Length of path')
    plt.ylabel('Count')
    plt.title("Histogram of the distribution of the distances from N1 to other nodes")
    plt.grid(True)
    print "hist:", [x for x in hist if x > 0]
    plt.show()

def get_top(ranks, N):
    ind = np.argpartition(ranks, -N, axis = 0)[-N:]
    return ind[::-1].flatten()

if __name__ == "__main__":
    main()