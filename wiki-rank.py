import numpy as np
import matplotlib.pyplot as plt
from Parser import Parser
from PageRanker import PageRanker
from Traverser import Traverser
import sys

TEST = "Test"
REAL_DATA = "oligo854"
EXAMPLE = "Example"

def main():
    f = open('results.txt', 'w')
    print "---\nWelcome to wiki-rank!"
    # parse text files containing links and titles
    parser = Parser(REAL_DATA)
    # calculate PageRank for articles
    page_rank = PageRanker(parser.links)

    # get top5 articles (rank, index and title)
    indices = get_top(page_rank.x_ranks, 5)
    top_ranks = []
    for index in indices:
        top_ranks.append((page_rank.x_ranks[index, 0], index + 1, parser.titles[index]))
    top_ranks.sort(reverse = True)
    print "Top 5 articles:"
    for item in top_ranks:
        print "\t", item

    # N1 is the index of the most popular article
    N1 = top_ranks[0][1] - 1
    print "N1:", N1 + 1, parser.titles[N1]

    # find unreachable nodes, diameter and shortest paths
    traverser = Traverser(parser.links.T, N1)
    print "---\nNodes unreachable from N1:\t", len(traverser.unreachable), [(x + 1, parser.titles[x]) for x in traverser.unreachable]
    print "Diameter:\t", traverser.diameter
    # find all nodes that are on the diameter
    diameter_indices = [index for index, path in enumerate(traverser.paths) if len(path) == traverser.diameter]
    diameter_titles = []
    for index in diameter_indices:
        diameter_titles.append(parser.titles[index])
    print "Possible N2:\t", [(x + 1, parser.titles[x]) for x in diameter_indices]
    N2_title = sorted(diameter_titles)[0]
    N2 = parser.titles.index(N2_title)
    print "Actual N2:\t", N2 + 1, parser.titles[N2]
    print "# of shortest paths from N1 to N2:\t", traverser.get_shortest(parser.links, N1, N2)
    print "Shortest path from N1 to N2:\t", [(x + 1, parser.titles[x]) for x in traverser.paths[N2]]
    hist_data = [len(x) for x in traverser.paths]

    # plot a histogram
    hist, bins = np.histogram(hist_data, bins = range(1, 100))
    width = 0.7
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.xlabel('Length of path')
    plt.ylabel('Count')
    plt.title("Histogram of the distribution of the distances from N1 to other nodes")
    plt.grid(True)
    # print additional data for histogram
    print "hist: ", [x for x in hist if x > 0]
    plt.show()

def get_top(ranks, N):
    ind = np.argpartition(ranks, -N, axis = 0)[-N:]
    return ind[::-1].flatten()

if __name__ == "__main__":
    main()