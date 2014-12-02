import numpy as np
from Parser import Parser
from PageRanker import PageRanker
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
    print "Top 5 articles:"
    for item in sorted(top_ranks, reverse = True):
        print item
    print "---\nUnreachable nodes:", page_rank.unreachable

def get_top(ranks, N):
    ind = np.argpartition(ranks, -N, axis=0)[-N:]
    return ind[::-1].flatten()

if __name__ == "__main__":
    main()