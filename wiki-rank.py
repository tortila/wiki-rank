import numpy as np
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
    parser = Parser(EXAMPLE)
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
    N1 = top_ranks[0][1]
    print "N1:", N1

    traverser = Traverser(parser.links.T, N1 - 1)
    print "---\nNodes unreachable from N1:", [x + 1 for x in traverser.unreachable]



def get_top(ranks, N):
    ind = np.argpartition(ranks, -N, axis = 0)[-N:]
    return ind[::-1].flatten()

if __name__ == "__main__":
    main()